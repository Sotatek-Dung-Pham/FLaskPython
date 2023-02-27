from app import app
from flask_jwt_extended import jwt_required
from controllers import api_user_controller

@app.route('/api/login', methods = ['POST'])
def api_login():
    return api_user_controller.api_login()

@app.route('/api/protected', methods = ['GET'])
@jwt_required()
def api_protected():
    return api_user_controller.api_protected()

# `refresh=True` options in jwt_required to only allow
@app.route('/api/refreshToken', methods = ['POST'])
@jwt_required(refresh = True)
def api_refresh_access_token():
    return api_user_controller.api_refresh_access_token()

@app.route('/api/signup', methods = ['POST'])
def api_signup():
    return api_user_controller.api_signup()

@app.route('/api/logout', methods = ['DELETE'])
@jwt_required(verify_type = False)
def api_logout():
    return api_user_controller.api_logout()

# User Database Route
# this route sends back list of users
@app.route('/api/user', methods = ['GET'])
@jwt_required()
def api_get_all_users():
    return api_user_controller.api_get_all_users()

@app.route('/api/cart/add', methods = ['POST'])
@jwt_required()
def api_cart_add():
    return api_user_controller.api_cart_add()
