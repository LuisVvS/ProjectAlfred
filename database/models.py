from database.DB_connection import connection
def create_task(arg):
                        con = connection()
                        cursor = con.cursor()

                        cursor.execute("INSERT INTO Todo(nome) VALUES(%s)", (arg, ))

                        con.commit()

                        cursor.close()
                        con.close()

def update_task(arg,nome):
                        con = connection()
                        cursor = con.cursor()

                        cursor.execute("UPDATE Todo SET nome = %s WHERE taskid = %s", (nome, arg))
                        con.commit()

                        con.close()
                        cursor.close()

def delete_task(arg):
                        con = connection()
                        cursor = con.cursor()

                        cursor.execute("DELETE FROM Todo WHERE taskid = %s", (arg, ))
                        con.commit()

                        con.close()
                        cursor.close()

def show_task():
                        cursor = connection().cursor()

                        cursor.execute("SELECT * FROM Todo")

                        rows = cursor.fetchall()

                        return rows
                        
