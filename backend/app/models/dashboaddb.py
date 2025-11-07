import mysql.connector
from app.dbconnection import MyConfiguration, Database

class Dashboard:
    def __init__(self, connection):
        """
        The constructor requires a database connection object.
        """
        if not connection:
            raise ValueError("Database connection object is required.")
        try:
            self.connection = connection
            self.cursor = connection.cursor(dictionary=True)  # results as dicts
        except Exception as err:
            print(f'Error initializing Dashboard model: {err}')
            raise

    # Task 1: Total tasks
    def total_task(self):
        sql = "SELECT COUNT(*) AS total_tasks FROM tasks"
        try:
            self.cursor.execute(sql)
            get_total = self.cursor.fetchone()["total_tasks"]
            return True, get_total
        except Exception as e:
            print(f"Error: {e}")
            return False

    # # Task 2: Total assigned tasks
    def total_assigned_tasks(self):
        sql = "SELECT COUNT(*) AS assigned_tasks FROM tasks WHERE assigned_to IS NOT NULL"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()["assigned_tasks"]
        except Exception as e:
            print(f"Error: {e}")
            return False

    # Task 3: Total tasks completed
    def total_tasks_completed(self):
        sql = "SELECT COUNT(*) AS completed_tasks FROM tasks WHERE task_status = 'completed'"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()["completed_tasks"]
        except Exception as e:
            print(f"Error: {e}")
            return False



    # Task 4: Total tasks pending
    def total_tasks_pending(self):
        sql = "SELECT COUNT(*) AS pending_tasks FROM tasks WHERE task_status = 'pending'"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()["pending_tasks"]
        except Exception as e:
            print(f"Error: {e}")
            return False

    # Task 5: Total tasks open
    def total_tasks_open(self):
        sql = "SELECT COUNT(*) AS open_tasks FROM tasks WHERE task_status = 'open'"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()["open_tasks"]
        except Exception as e:
            print(f"Error: {e}")
            return False

    # Task 6: Total users
    def total_users(self):
        sql = "SELECT COUNT(*) AS total_users FROM users"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()["total_users"]
        except Exception as e:
            print(f"Error: {e}")
            return False
        
  

  

    # Task 7: 10 recent tasks
    def recent_tasks(self):
        sql = "SELECT * FROM tasks ORDER BY created_date DESC LIMIT 10"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            return False

    # Task 8: 10 recent users
    def recent_users(self):
        sql = "SELECT * FROM users ORDER BY created_date DESC LIMIT 10"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            return False


# Function to establish connection and return dashboard instance
def check_dashboard_connection():
    """
    Establishes a database connection and returns a configured Dashboard object.
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
        task_dashboard = Dashboard(mysql_connect.connection)
        return True, task_dashboard
    except Exception as e:
        print(f'Failed to connect to the database: {e}')
        return False, f'Error: {e}'

 













