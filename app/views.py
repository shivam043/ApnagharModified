from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, \
    login_required,UserMixin
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User,Places
from oauth import OAuthSignIn
import sqlite3,re
from twilio.rest import TwilioRestClient
from random import randint


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

@app.route('/index1')
def index1():
    
    return render_template('index1.html')

@app.route('/profile')
@login_required
def profile():
    
    return render_template('profile.html')	
	
	
	
@app.route('/profile',methods=['POST','GET'])
@login_required
def profile1():
    if request.method=='POST':
        if request.form['btn']=="Send OTP":        
            user=User.query.get(g.user.id)
            c=randint(99999,1000000)
            d=0
    # Find these values at https://twilio.com/user/account
            account_sid = "ACcf810e4cc297d92113c8b896c29a0581"
            auth_token = "822c0918f867d81f1b2c5aac26dcde48"
            client = TwilioRestClient(account_sid, auth_token)
            string="+91"
            user.temp=request.form['mobile']
            string=string+str(user.temp)
    #if user.mobile !='':
            d=1
            user=User.query.get(g.user.id)
            user.otp=c
            db.session.commit()
            message = client.messages.create(to=string, from_="+12765944002", body=("Hi,{0} is your One Time password on APNAGHAR . Please use this password to complete your phone verification").format(c))
            
	
        elif request.form['btn']=="Verify":
    #if request.method=='POST':
            a="aman1"
            c1=request.form['otp']
            user=User.query.get(g.user.id)
            d=0
            if (int(c1) == int(user.otp)):
                f=user.temp
                a="aman"
                user.mobile=f
                db.session.commit()
                
        else:
            user=User.query.get(g.user.id)
            currpass=request.form['currentpassword']
            newpass=request.form['newpassword']			
            cnfpass=request.form['confirmpassword']
            d=0
            if user.password==currpass and newpass==cnfpass:
                user.password=newpass
                d=0
                db.session.commit()
            else:
                flash('Password does not match')

    return render_template('profile.html',d=d)
    #rows = cur.fetchall()

	
	
@app.route('/index1',methods=['GET', 'POST'])
def index1post():
    if request.method=='POST':
        if request.form['btn']=="Log In":
            email=request.form['email'] 
            password=request.form['password']
            user=User.query.filter_by(email=email,password=password).first() 
            if user is not None:
                login_user(user)
                return redirect(url_for('index1'))
            else: 
                flash('Username or Password is invalid' )
                return redirect(url_for('index1'))
        else:
            name1=request.form['name1']
            email1=request.form['email1']
            password1=request.form['password1']
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email1)
            match1=re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password1)
            if match1==None and match==None:
                flash('Invalid credentials')
                return redirect(url_for('index1'))
            else:
                if match1 == None:
                    flash('Length of password must be 8 character long')
                    return redirect(url_for('index1'))
                if match == None:
                    flash('Invalid email type.')
                    return redirect(url_for('index1'))
            user1 = User(name=name1,email=email1 ,password=password1)
            db.session.add(user1)
            db.session.commit()
            flash('User successfully registered')
            return redirect(url_for('index1'))
            '''  if name1 !='' and email1!='' and password1!='':
                     #flash('User successfully registered')
                      return redirect(url_for('index1'))'''
    
    
  
    
    #return render_template('index1.html')


	
@app.route('/logina')
def logina():
    
    return render_template('logina.html')	

@app.route('/index')
@login_required
def index():
    user = g.user
    
    #con = sqlite3.connect("app.db")
    #con.row_factory = sqlite3.Row
   
    #cur = con.cursor()
    #cur.execute("select link from links")
   
    #rows = cur.fetchall()
   
    return render_template('index2.html',
                           title='Home',
                           user=user,
               
						   )


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
	
    #con = sqlite3.connect("app.db")
    #con.row_factory = sqlite3.Row
   
    #cur = con.cursor()
    #cur.execute("select place from places")
   
    #rows = cur.fetchall()	
    #pqrs=cur.fetchall()
	
    return render_template('login2.html',
                           title='Sign In',
                           form=form,
                           
						   othproviders=app.config['OAUTH_CREDENTIALS'],
						   rows=rows,
						   pqrs=pqrs)
						   





@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index1'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index1'))
	
	
@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index1'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index1'))
    oauth = OAuthSignIn.get_provider(provider)
    username, email,name = oauth.callback()
    if email is None:
        flash('Authentication failed.')
        return redirect(url_for('index1'))
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User( email=email,name=name,password="qwertyiso1234567890_sdasd_ewdsdsdfvds")
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index1'))
