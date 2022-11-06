import profile
from flask import Flask, jsonify, request
from flask_restful import Resource, Api , reqparse 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


db = SQLAlchemy(app)
