from database.DB_connection import connection
def create_task(arg):
                        cursor = connection().cursor()

                        cursor.execute("INSERT INTO Todo(nome) VALUES(%s)", (arg))

                        connection().commit()

def update_task(arg):
                        ...
def delete_task(arg):
                        ...
def show_task(arg):
                        ...
