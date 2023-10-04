from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
      host='localhost',
      user='root',
      password='Srinivas@8',
      database='python_users'
    )

@app.route('/users', methods=['GET'])
def getUsers():
    cursor = db.cursor()
    sqlQuery = 'SELECT * FROM users'
    cursor.execute(sqlQuery)
    users = cursor.fetchall()
    cursor.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def createUsers():
    data = request.json
    cursor = db.cursor()
    sqlQuery = 'INSERT INTO users (name, email) VALUES (%s, %s)'
    cursor.execute(sqlQuery, (data['name'], data['email']))
    db.commit()
    cursor.close()
    return jsonify({'message':'User created successfully...'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    data = request.json
    cursor = db.cursor()
    sqlQuery = 'UPDATE users SET name = %s, email = %s WHERE id = %s'
    cursor.execute(sqlQuery, (data['name'], data['email'], user_id))
    db.commit()
    cursor.close()
    return jsonify({'message':'User updated successfully...'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    cursor = db.cursor()
    sqlQuery = 'DELETE FROM users WHERE id = %s'
    cursor.execute(sqlQuery, (user_id,))
    db.commit()
    cursor.close()
    return jsonify({'message':'User Deleted successfully...'})

if __name__ == '__main__':
    app.run(debug=True)