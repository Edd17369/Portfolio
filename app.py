from flask import Flask, request, render_template, url_for, redirect, flash
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message

load_dotenv() 

app = Flask(__name__) # An instance of this class will be our WSGI application.
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


@app.route('/')
def index():
    return render_template("index.html")





