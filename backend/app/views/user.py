from app import app

from flask import Flask , request ,jsonify
from app.models.users_db import Users,check_user_connection
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()






@app.route("/register" , methods = ["POST"])
def register():
    user_name = request.json.get("user_name")
    user_email = request.json.get("user_email")
    user_password = request.json.get("user_password")
    user_gender = request.json.get("user_gender")
    user_role = request.json.get("user_role")

    if not all([user_name,user_email,user_password,user_gender,user_role]):
        return jsonify({"status": "Error" , "message" : "soo geli fields dhaman"})
    db_conn,users_object= check_user_connection()
    if not db_conn:
        return jsonify({"status":"Error" , "message" : "db connection error"})
    # ka dhig hash password
    hash = bcrypt.generate_password_hash(user_password).decode("utf-8")
    check_email = users_object.check_user_email(user_email)
    if check_email:
        return jsonify({"status" : "error" , "message" : "user email already exists"})
    register_user = users_object.register_user(user_name,user_email, hash ,user_gender,user_role)

    if register_user:
        return jsonify({"status" : "sucess" , "message" : "user registered sucess"})
    else:
        
        return jsonify({"status" : "error" , "message" : "use does not registered"})
    
# @app.route("/register" , methods = ["POST"])
@app.route("/login" , methods = ["POST"])
def login():
    user_email = request.json.get("user_email")
    user_password = request.json.get("user_password")

    if not user_email or not user_password:
            return jsonify({"status":"error" ,"message":"user_email and user_password are required"})
    db_conn,users_object= check_user_connection()
    if db_conn:
        make_login = users_object.login(user_email,user_password)
        if make_login and make_login[0] == True:
            return jsonify({"status":"sucess" ,"message":"sucessfuly login" ,"data" : make_login})
        else:
             return  jsonify({"status":"error" ,"message":"email or password incorect"})

        
    else:
            return jsonify({"status":"error" ,"message":"database error"})
@app.route("/profile-apdate" ,methods = ["PUT"])
def udate_user():
    id = request.json.get("id")
    user_name = request.json.get("user_name")
    user_email = request.json.get("user_email")
    user_password = request.json.get("user_password")
    user_gender = request.json.get("user_gender")


    db_conn,users_object= check_user_connection()
    if not db_conn:
         return jsonify({"status": "error" ,"message":"db connection error"})
    hash = bcrypt.generate_password_hash(user_password).decode("utf-8")

    apdate_profile = users_object.profile_update(user_name,user_email,hash,user_gender,id)
    if apdate_profile:
         return jsonify({"status": "sucess" , "message" : "user profile apdated sucess"})
    else:
         return jsonify({"status": "error" ,"message" : "user profile update something wrong"} )


    








   
     


    