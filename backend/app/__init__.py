


# app/__init__.py
from flask import Flask

app = Flask(__name__)

app.config["123nimco"] = "123nimco"




# ............ modules
from app.models import users_db
from app.models import taskdb
from app.models import dashboaddb



# ............ views

from  app.views import user
from app.views import tasks
from app.views import dashboard
