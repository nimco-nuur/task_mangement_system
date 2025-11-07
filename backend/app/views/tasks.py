from app import app

from flask import Flask , request ,jsonify
from app.models.taskdb import Tasks,check_task_connection
from flask import Flask





@app.route("/task", methods=["POST"])
def new_task():
    task_name = request.json.get("task_name")
    task_description =  request.json.get("task_description")
    task_status =  request.json.get("task_status")
    task_priority =  request.json.get("task_priority")
    assigned_to = request.json.get("assigned_to")

    due_date =  request.json.get("due_date")
    if not all ([task_name,task_description,task_status,task_priority,assigned_to,due_date]):
        return jsonify({"status": "error" , "message" : "all fields are required"})
    db_conn,task_object= check_task_connection()
    if not db_conn:
         return jsonify({"status": "error" , "message" : "db error"})

    create_task = task_object.new_task(task_name,task_description,task_status,task_priority,assigned_to,due_date)
    if create_task:
            return jsonify({"status": "sucess" , "message" : "task created sucess"})
    else:
         return jsonify({"status": "error" , "message" : "task creation error"})

@app.route("/all-tasks" , methods = ["GET"])
def display_task():
      db_conn,task_object= check_task_connection()
      if not db_conn:
           return jsonify({"status": "error" , "message" : "db error"})
      task_sucess,all_task = task_object.display_all_task()
      if not task_sucess:
           return jsonify({"status": "error" , "message" : "no task found"})
      else:
           return jsonify({"status": "sucess" , "message" : "all tasks are" , "data" : all_task})
      

           
     
@app.route("/update-task" , methods = ["PUT"])
def update_task():
     task_name = request.json.get("task_name")
     task_description =  request.json.get("task_description")
     task_status =  request.json.get("task_status")
     task_priority =  request.json.get("task_priority")
     due_date =  request.json.get("due_date")
     id =  request.json.get("id")
     db_conn,task_object= check_task_connection()
     if not db_conn:
          return jsonify({"status": "error" ,"message" :"db error"})
     update_tasks = task_object.update_task(task_name,task_description,task_status,task_priority,due_date,id)
     print(f"value of update_task  {update_tasks}")
     if update_tasks:
          return  jsonify({"status": "sucess" ,"message" :"task updated sucess"})
     else:
          return  jsonify({"status": "error" ,"message" :"failed to update task"})
     
@app.route("/delete-task" , methods = ["delete"])
def delete_task():
     id =  request.json.get("id")
     db_conn,task_object= check_task_connection()
     if not db_conn:
          return jsonify({"status":"error" ,"message":"db connection error"})
     task_delate = task_object.delete_task(id)
     print(f"value of delate_tasks:{task_delate}")
     if task_delate:
          return jsonify({"status":"sucess" ,"message":"task delated sucees"})
     else:
          return jsonify({"status":"error" ,"message":"failed to delete task"})






 





