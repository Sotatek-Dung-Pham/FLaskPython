from app import app, render_template
from controllers import web_user_controller

@app.route('/', methods = ['GET'])
def index():
    return web_user_controller.web_index()

@app.route('/cart', methods = ['GET'])
def cart():
    return web_user_controller.web_cart()

@app.route('/login', methods = ['GET'])
def login():
    return web_user_controller.index_web_login()

@app.route('/login', methods = ['POST'])
def login_post():
    return web_user_controller.web_login()

@app.route('/logout', methods = ['GET'])
def logout():
    return web_user_controller.web_logout()

@app.route('/signup', methods = ['POST'])
def signup():
    return web_user_controller.web_signup()
