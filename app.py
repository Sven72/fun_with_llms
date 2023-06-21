from flask import Flask, render_template, request, jsonify
import sqlite3
from llm import test

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    emotions = conn.execute('SELECT * FROM emotions ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.tpl', gradioserver_url='http://127.0.0.1:7860', emotions=emotions)



if __name__ == '__main__':
    app.run(debug=True)