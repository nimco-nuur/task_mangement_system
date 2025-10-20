from flask import Flask


app = Flask(__name__)
app.config["123nimco"] = "123nimco"



# ............ modules
from app.models import users_db



# ............ views

from  app.views import user
