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
    register_user = users_object.register_user(user_name,user_email, hash ,user_gender,user_role)

    if register_user:
        return jsonify({"status" : "sucess" , "message" : "user registered sucess"})
    else:
        return jsonify({"status" : "error" , "message" : "use does not registered"})





   
     


    