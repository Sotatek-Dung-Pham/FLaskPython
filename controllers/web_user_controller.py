from flask import request, redirect, flash, render_template
from flask_login import login_user, current_user, logout_user
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from flask import session
from services import user_service
from services import cart_service
from services import product_service

def web_index():
    cart = None

    if current_user.is_authenticated:
        cart = cart_service.count_cart_item(current_user.id)

    products = product_service.get_all_product()

    return render_template('index.html', products = products, cart = cart)

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

    # generates the JWT Token
    session["access_token"] = create_access_token(identity = user.public_id)

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember = remember)

    return redirect('/')

def web_logout():
    logout_user()

    if "access_token" in session:
        session.pop("access_token")

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

def web_cart():
    if not current_user:
        return render_template('login.html')

    cart_items = cart_service.get_all_cart_item_isfalse_by_user_id(current_user.id)

    total = 0
    for cart_item in cart_items:
        total += cart_item.Product.price * cart_item.Product.discount / 100

    return render_template('cart.html', cart_items = cart_items, total = total)
