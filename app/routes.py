from app import api, web
from app.controllers import MyController, MyViewController, MySumController
from app.controllers.api import ApiTodoController

# def index():
#     return "Hello World!"

# API
api.add_resource(ApiTodoController.TodoController, "/todo","/todo/<string:id>")
api.add_resource(MyController.MyController, "/")

# WEB
web.add_resource(MyViewController.MyViewController, "/")
web.add_resource(MyViewController.MySecondViewController, "/myname")

# TASK
web.add_resource(MySumController.show_num, "/shownum")

