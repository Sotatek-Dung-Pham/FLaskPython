from flask import jsonify, request
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt
from services import user_service
from services import product_service
from services import cart_service
from datetime import timedelta
import redis

def api_login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = user_service.get_user_by_email(email)

    if not user:
        return jsonify({'msg': 'User does not exist'}, 401)

    if check_password_hash(user.password, password):
        # generates the JWT Token
        access_token = create_access_token(identity = user.public_id)
        refresh_token = create_refresh_token(identity = user.public_id)

        return jsonify({'access_token': access_token, 'refresh_token': refresh_token}, 201)
    return jsonify('Wrong Password', 403)

def api_protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    user = user_service.get_user_by_public_id(current_user)

    return jsonify(logged_in_as = user.email), 200

def api_refresh_access_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity = identity)

    return jsonify({'access_token': access_token}, 201)

def api_signup():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = user_service.get_user_by_email(email)

    if not user:
        user_service.create_user_by_email_and_password(email, password)

        return jsonify('Successfully registered.', 201)
    else:
        return jsonify('User already exists.', 202)

def api_logout():
    # Setup our redis connection for storing the blocklisted tokens. You will probably
    # want your redis instance configured to persist data to disk, so that a restart
    # does not cause your application to forget that a JWT was revoked.
    jwt_redis_blocklist = redis.StrictRedis(
        host = 'localhost',
        port = 6379,
        db = 0,
        decode_responses = True
    )
    token = get_jwt()['jti']
    jwt_redis_blocklist.set(token, '', ex = timedelta(hours = 1))

    blacklist_token = user_service.create_blacklist_token_by_token(token)
    if (blacklist_token):
        return jsonify(msg = 'token successfully revoked')
    else:
        return jsonify(msg = 'exitsted token')

def api_get_all_users():
    users = user_service.get_all_user()
    output = []

    for user in users:
        output.append({
            'public_id': user.public_id,
            'email' : user.email
        })

    return jsonify({'users': output})

def api_cart_add():
    product_id = request.json.get('product_id', None)
    quantity = request.json.get('quantity', None)
    user = user_service.get_user_by_public_id(get_jwt_identity())
    product = product_service.get_product_by_id(product_id)

    if product:
        cart_service.add_cart_by_product_id_and_quantity(product_id, quantity, user.id)

        return jsonify({'msg': 'Successfully add to cart.', 'status': 200})
    else:
        return jsonify({'msg': 'Error add to cart', 'status': 204})
