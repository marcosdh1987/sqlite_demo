import sqlite3
from sqlite3 import Error

class DBManage():

    def __init__(self, db_file):
        self.db_file = db_file
        self.create_connection(db_file)

    def create_connection(db_file="./db/sqlite.db"):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
            return conn
        except Error as e:
            print(e)
        # finally:
        #     if conn:
        #         conn.close()

    def create_table(conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    #method to create a new project
    def create_task(conn, task):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """

        sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()

        return cur.lastrowid
        
    #method to create a new task
    def create_project(conn, project):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO projects(name,begin_date,end_date)
                VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        return cur.lastrowid

    def run_query(conn, query):
        """
        :param conn: Connection to the SQLite database
        :param query: Query to run
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(query)
            return c.fetchall()
        except Error as e:
            print(e)