from flask import request, redirect, flash, render_template
from flask_login import login_user, current_user, logout_user
from flask_bcrypt import check_password_hash
from services import user_service

def index_web_login():
    if current_user.is_authenticated:
        return redirect('/')

    return render_template('login.html')

def web_login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = user_service.get_user_by_email(email)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your email and password and try again.')
        return redirect('/login')

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember = remember)
    return redirect('/')

def web_logout():
    logout_user()
    return redirect('/')

def web_signup():
    email = request.form.get('email')
    password = request.form.get('password')

    user = user_service.get_user_by_email(email)

    if user:
        flash('Email already exists')
        return redirect('/login#pills-register')
    else:
        user_service.create_user_by_email_and_password(email, password)

        return redirect('/login')
