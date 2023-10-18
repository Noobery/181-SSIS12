from website import mysql

class CollegeModel:
    @classmethod
    def create_college(cls, name, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", (code, name))
            mysql.connection.commit()
            return "College created successfully"
        except Exception as e:
            return f"Failed to create college: {str(e)}"

    @classmethod
    def get_colleges(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT code, name FROM college")
        colleges = cur.fetchall()
        return colleges

    @classmethod
    def delete_college(cls, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            # Delete courses associated with the college
            cur.execute("DELETE FROM course WHERE college_code = %s", (code,))
            # Delete the college
            cur.execute("DELETE FROM college WHERE code = %s", (code,))
            mysql.connection.commit()
            return "College and its courses deleted successfully"
        except Exception as e:
            return f"Failed to delete college: {str(e)}"

    def update_college(cls, code, new_name):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE college SET name = %s WHERE code = %s", (new_name, code))
            mysql.connection.commit()
            return "College updated successfully"
        except Exception as e:
            return f"Failed to update college: {str(e)}"