
import mysql.connector

class MyConfiguration:
    SECRET_KEY = '123nimco'
    DB_HOSTNAME = 'localhost'
    DB_USERNAME = 'root'
    DB_NAME = 'task_managment'
    DB_PASSWORD = '123456789'
    



class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def make_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
    

    def my_cursor(self):
        return self.cursor
 

