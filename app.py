
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tools = conn.execute('SELECT * FROM tools').fetchall()
    conn.close()
    return render_template('index.html', tools=tools)

@app.route('/category/<category>')
def category(category):
    conn = get_db_connection()
    tools = conn.execute('SELECT * FROM tools WHERE category = ?', (category,)).fetchall()
    conn.close()
    return render_template('index.html', tools=tools)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        link = request.form['link']
        category = request.form['category']
        conn.execute('INSERT INTO tools (name, description, link, category) VALUES (?, ?, ?, ?)', 
                     (name, description, link, category))
        conn.commit()
    tools = conn.execute('SELECT * FROM tools').fetchall()
    conn.close()
    return render_template('admin.html', tools=tools)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tools WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
