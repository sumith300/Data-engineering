from flask import Flask
import pymysql

app = Flask(__name__)




@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/insert')
def insert():
    connection = pymysql.connect(
        host='mysql-container',
        user='root',
        password='root',
        database='flask-test'
    )
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (city, temperature) VALUES ('New York', 25.5)")
    connection.commit()
    cursor.close()
    connection.close()
    return 'Data inserted successfully!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  