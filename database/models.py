from logging import exception
from discord import errors
from database.DB_connection import connection

def create_task(arg):
                        try:
                                                con = connection()
                                                cursor = con.cursor()

                                                cursor.execute("INSERT INTO Todo(nome) VALUES(%s)", (arg, ))

                                                con.commit()
                        except Exception as a:
                                                print(f"Error while creating a task: {a}")
                                                raise
                        finally:

                                                if cursor:
                                                                        cursor.close()
                                                if con:
                                                                        con.close()

def update_task(arg,nome):
                        try:
                                                con = connection()
                                                cursor = con.cursor()

                                                cursor.execute("UPDATE Todo SET nome = %s WHERE taskid = %s", (nome, arg))
                                                con.commit()

                        except Exception as a:
                                                print(f"Error while trying to update the task {a}")
                                                raise
                        finally:
                                                if con:
                                                                        con.close()
                                                if cursor:
                                                                        cursor.close()

def delete_task(arg):
                        try:
                                                con = connection()
                                                cursor = con.cursor()

                                                cursor.execute("DELETE FROM Todo WHERE taskid = %s", (arg, ))
                                                con.commit()
                        except Exception as a:
                                                print(f"Error while deleting the task: {a}")
                                                raise 
                        finally:
                                                if con:
                                                                        con.close()
                                                if cursor:
                                                                        cursor.close()

def show_task():
                        cursor = connection().cursor()

                        cursor.execute("SELECT * FROM Todo")

                        rows = cursor.fetchall()

                        return rows
                        
