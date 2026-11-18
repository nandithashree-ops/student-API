from flask  import Flask,request,jsonify
import sqlite3
app = Flask(__name__)
def get_db_connection():
    conn=sqlite3.connect('students.db')
    conn.row_factory=sqlite3.Row
    return conn
# GET all students
@app.route('/students',methods=['GET'])
def get_students():
    conn=get_db_connection()
    students=conn.execute(
        'SELECT*FROM students'
    ).fetchall()
    conn.close()
    result=[]
    for student in students:
        result.append({
            "id":student["id"],
            "name":student["Name"],
            "email":student["email"]
        })
        return jsonify(result)
    #UPDATE student name by id
    @app.route('/students/<int:id>',methods=['put'])
    def update_student(id):
        data=request.get_json()
        if not data or not data.get('name'):
            return jsonify({
                "error":"student name is required"
            }),400
        new_name=data.get('name')
        conn=get_db_connnection()
        student=conn.execute(
            'SELECT*FROM students WHERE id=?',
            (id,)
        ).fetchone()
        if student is None:
            conn.close()
            return josnify({
                "error":"student not found"
            }),404
        conn.execute(
            'UPDATE students SET name=? WHERE id=?',
            (new_name,id)
        )
        conn.commit()
        conn.close()
        return jsonify({
            "message":"student name update successfully",
            "id":id,
            "name":name_name
        })
    #DELETE student by ID
    @app.route('/students/<int:id>',methods=['DELETE'])
    def dlete_student(id):
        conn=get_db_connection()
        student=conn.execute(
        'SELeCT*FROM students WHERE id=?',
        (id,)
        ).fetchone()
        if student is None:
            conn.close()
            return jsonify({
                "error":"student not found"
            }),404
        conn.execute(
            'DELETE FROM student WHERE id=?',
            (id,)
        )
        conn.commit()
        conn.close()
        return jsonify({
            "message":"student deleted successfully"
        })
if __name__=='__main__':
 app.run(debug=True)