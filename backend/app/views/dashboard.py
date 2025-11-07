from app import app

from flask import Flask , request ,jsonify
from app.models.dashboaddb import Dashboard,check_dashboard_connection
from flask import Flask

# 1 total task
@app.route("/total-task" , methods = ["GET"])
def get_total_task():
          db_conn,task_dashboard= check_dashboard_connection()
          if not db_conn:
               return jsonify({"status": "error" , "message" : "db error"})
          total_task = task_dashboard.total_task()
          if not total_task:
                return jsonify({"status": "error" , "message" : "no task found"})
          else:
               return jsonify({ "status": "sucess"  ,  "message" : "total tasks are" , "data" : total_task ,})
# 2:total assined task   
@app.route("/total-assined-task", methods = ["GET"])
def get_assigned_task():
      db_conn,task_dashboard = check_dashboard_connection()
      if not db_conn:
            return jsonify({"status" : "error" , "message" :"db error"})
      total_assign_task = task_dashboard.total_assigned_tasks()
      if total_assign_task:
            return jsonify({"status" : "success" , "message" : "total assigned task are","data": total_assign_task})
      else:
            return jsonify({"status" : "error" , "message":"no assigned task found" })
# 3:total_task completed
@app.route("/completed-task" , methods = ["GET"])
def get_completed_task():
      db_conn,task_dashboard = check_dashboard_connection()
      if not db_conn:
            return jsonify({"status" :"error" , "message": "db connection error"})
      task_comleted = task_dashboard.total_tasks_completed()
      if task_comleted:
            return jsonify({"status":"success" , "message" : "total comleted  tasks are " , "data":task_comleted})
      else:
            return jsonify({"status" : "error" , "message":"no task comleted found" })
#   4:total pending task    
@app.route("/pending-task" , methods = ["GET"])
def get_pending_task():
      db_conn,task_dashboard = check_dashboard_connection()
      if not db_conn:
            return jsonify({"status" :"error" , "message": "db connection error"})
      task_pending = task_dashboard.total_tasks_pending()
      if task_pending:
            return jsonify({"status":"success" , "message" : "total pending  tasks are " , "data":task_pending})
      else:
            return jsonify({"status" : "error" , "message":"no task pending found" })
      #   5:total opening task    
@app.route("/opening-task" , methods = ["GET"])
def get_opening_task():
      db_conn,task_dashboard = check_dashboard_connection()
      if not db_conn:
            return jsonify({"status" :"error" , "message": "db connection error"})
      task_opening= task_dashboard.total_tasks_open()
      if task_opening:
            return jsonify({"status":"success" , "message" : "total opening  tasks are " , "data":task_opening})
      else:
            return jsonify({"status" : "error" , "message":"no task opening found" })
      
      
      
# Task 6: Total users
@app.route("/total-users" , methods = ["GET"])
def get_total_users():
      db_conn,task_dashboard = check_dashboard_connection()
      if not db_conn:
            return jsonify({"status" :"error" , "message": "db connection error"})
      total_users = task_dashboard.total_users()
      if total_users:
            return jsonify({"status":"success" , "message" : "total users   are " , "data":total_users})
      else:
            return jsonify({"status" : "error" , "message":"no users  found" })
      
# Task 7: 10 recent tasks
@app.route("/recent-tasks" , methods = ["GET"])
def get_recent_task():
      db_conn,task_dashboard = check_dashboard_connection()
      if not db_conn:
            return jsonify({"status" :"error" , "message": "db connection error"})
      recent_task = task_dashboard.recent_tasks()
      if recent_task:
            return jsonify({"status":"success" , "message" : "recent tasks are   are " , "data":recent_task})
      else:
            return jsonify({"status" : "error" , "message":"no recent task  found" })
 # Task 8: 10 recent users     
@app.route("/recent-users" , methods = ["GET"])
def get_recent_users():
      db_conn,task_dashboard = check_dashboard_connection()
      if not db_conn:
            return jsonify({"status" :"error" , "message": "db connection error"})
      recent_users = task_dashboard.recent_users()
      if recent_users:
            return jsonify({"status":"success" , "message" : "recent tasks are   are " , "data":recent_users})
      else:
            return jsonify({"status" : "error" , "message":"no recent users   found" })






    





