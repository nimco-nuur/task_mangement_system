
import mysql.connector


from app.dbconnection import MyConfiguration,Database
from  flask_bcrypt  import Bcrypt
bycript = Bcrypt()


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
    def check_user_email(self,user_email):
        sql = "select id, user_name,user_email,user_password,user_gender,user_role from users WHERE user_email = %s"
        try:
            self.cursor.execute(sql,(user_email,))
            found_email = self.cursor.fetchone()
            print(f"value of check email {found_email}")
            if found_email:
                return True
            else:
                return False
        except Exception as e:
            return False,e        
    def login(self,user_email,user_password):
        sql = "select id, user_name,user_email,user_password,user_gender,user_role  from users  where user_email = %s"
        try:
            self.cursor.execute(sql,(user_email,))
            get_user = self.cursor.fetchone()
            hashed_password = get_user["user_password"]
            if not get_user:
                return False ,'user not fund '
            
            if bycript and bycript.check_password_hash(hashed_password,user_password):
                print(f"user_password : {user_password}  hashad_password:{hashed_password}")
                print("successfully login")
                del get_user['user_password']
                return True,get_user

        except Exception as e:
            return False , 'error while login'
        


    def profile_update(self,user_name,user_email,user_password,user_gender,id):
        sql = """

          UPDATE  users set user_name = %s , user_email = %s ,user_password = %s , user_gender = %s
          WHERE id = %s

          """
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql,(user_name,user_email,user_password,user_gender,id))
            self.connection.commit()
            print("Updating user:")
            return True
        except Exception as e:
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