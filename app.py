import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from prompter import Prompter, new_emotions_prompt
from llm import test

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
# def first(): 
#     return render_template('index.tpl', gradioserver_url='http://127.0.0.1:7860')
    
def index():
    conn = get_db_connection()
    emotions = conn.execute('SELECT * FROM emotions').fetchall()
    conn.close()
    return render_template('index.tpl', gradioserver_url='http://127.0.0.1:7860', emotions = emotions)

@app.route('/emotions/')
def emos():
    conn = get_db_connection()
    emotions = conn.execute('SELECT * FROM emotions').fetchall()
    conn.close()
    return render_template('emotions.tpl', emotions = emotions)