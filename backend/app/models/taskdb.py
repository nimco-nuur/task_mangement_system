
import mysql.connector


from app.dbconnection import MyConfiguration,Database

class Tasks:
   
   def __init__(self, connection):
        """
        The constructor requires a database connection object.
        """
        if not connection:
            raise ValueError("Database connection object is required.")
        try:
            self.connection = connection
            self.cursor = connection.cursor(dictionary=True) # Use dictionary=True to get results as dicts
        except Exception as err:
            print(f'Error initializing Users model: {err}')
            raise


   def new_task(self,task_name,task_description,task_status,task_priority,assigned_to,due_date):
       sql = """
            INSERT INTO tasks(task_name,task_description,task_status,task_priority,assigned_to,due_date)
            VALUES(%s,%s,%s,%s,%s,%s)

         """
       try:
           self.cursor.execute(sql,(task_name,task_description,task_status,task_priority,assigned_to,due_date))
           self.connection.commit()
           return True
           
       except Exception as e:
           print(f"error:{e}")
           return True
       
   def display_all_task(self):
       sql = "SELECT * FROM tasks"
       try:
           self.cursor.execute(sql)
           all_task = self.cursor.fetchall()
           if not all_task:
               return [],'no task found'
           return  True,all_task
           
       except Exception as e:
           print(f"value of e {e}")
           return False
   def update_task(self,task_name,task_description,task_status,task_priority,due_date,id):
    sql =  """
          UPDATE tasks SET task_name = %s,task_description = %s , task_status = %s ,
          task_priority = %s ,due_date = %s  WHERE id = %s
         """
    try:
        self.cursor.execute(sql,(task_name,task_description,task_status,task_priority,due_date,id))
        self.connection.commit()
        return True
    except Exception as e:
        print(f"value of e in update  task :{e}")
        return False
    
   def delete_task(self,id):
       sql = "DELETE from tasks WHERE id = %s"
       try:
           self.cursor.execute(sql,(id,))
           self.connection.commit()
           return True
       except Exception as e :
           print(f"value of e in delet task {e}")
           




def check_task_connection():
    """
    Establishes a database connection and returns a configured Users object.
    """
    try:
        my_configuration = MyConfiguration()
        mysql_connect = Database(
            host=my_configuration.DB_HOSTNAME,
            port=3306,
            user=my_configuration.DB_USERNAME,
            password=my_configuration.DB_PASSWORD,
            database=my_configuration.DB_NAME
        )
        mysql_connect.make_connection()
        # Create an instance of the Users class correctly, with the connection
        task_object = Tasks(mysql_connect.connection)
        return True, task_object
    except Exception as e:
        print(f'Failed to connect to the database: {e}')
        return False, f'Error: {e}'
