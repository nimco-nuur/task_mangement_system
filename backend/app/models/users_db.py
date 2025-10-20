
import mysql.connector


from app.dbconnection import MyConfiguration,Database


class Users:
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



    def register_user(self,user_name,user_email,user_password,user_gender,user_role):
        sql = "INSERT INTO users(user_name,user_email,user_password,user_gender,user_role) VALUE(%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,(user_name,user_email,user_password,user_gender,user_role))
            self.connection.commit()
            return True 
        
        except Exception as e:
            print(f"error while registering user {e}")
            return False

def check_user_connection():
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
        users_object = Users(mysql_connect.connection)
        return True, users_object
    except Exception as e:
        print(f'Failed to connect to the database: {e}')
        return False, f'Error: {e}'