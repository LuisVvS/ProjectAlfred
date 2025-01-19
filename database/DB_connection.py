import psycopg2

def connection():

                        conn = psycopg2.connect(database="DiscordTodo",
                                                host="localhost",
                                                user="postgres",
                                                password="123456",
                                                port="5432")

                        return conn


