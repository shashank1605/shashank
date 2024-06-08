from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'newconnection'
app.config['MYSQL_PASSWORD'] = 'Yashsai07@'
app.config['MYSQL_DB'] = 'yourdatabase'

mysql = MySQL(app)

@app.route('/')
def home():
    # Example query
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)