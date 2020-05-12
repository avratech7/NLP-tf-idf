import psycopg2
import logging

# Update connection string information
host = "drona.db.elephantsql.com"
dbname = "lnhiqqex"
user = "lnhiqqex"
password = "iP6W0C7_-6rsUI9dK7JN7WI6qxPVEx-q"

# Construct connection string
def connet_to_host(host,user,dbname,password):
    conn_string = f"host={host} user={user} dbname={dbname} password={password}"
    try:
        conn  = psycopg2.connect(conn_string)
        print("Connection established")
        return conn
    except:
        logging.error("connection failed")


# Create a table
def create_a_table(table_name,list_of_cloum,definition):
    conn = connet_to_host(host, user, dbname, password)
    cursor = conn.cursor()
    try:
        cursor.execute(f"CREATE TABLE  {table_name}({list_of_cloum} {definition});")
        print("Finished creating table")
    except psycopg2.errors.DuplicateTable as p:
        print(p)
    conn.commit()
    cursor.close()
    conn.close()

def add_cloum(table_name, cloum_name, definition):
    conn = connet_to_host(host, user, dbname, password)
    cursor = conn.cursor()
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {cloum_name} {definition};")
    conn.commit()
    cursor.close()
    conn.close()

def drop_table(table_name):
    conn = connet_to_host(host, user, dbname, password)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    print("Finished dropping table (if existed)")
    conn.commit()
    cursor.close()
    conn.close()

def insert(table_name,cloum_name,value):
    conn = connet_to_host(host, user, dbname, password)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} ({cloum_name}) VALUES {value};")
    conn.commit()
    cursor.close()
    conn.close()

def update_were(table_name,cloum_name,value,cloum_to_comp,value_to_comp):
    conn = connet_to_host(host, user, dbname, password)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table_name} SET {cloum_name} = {value} WHERE {cloum_to_comp} = '{value_to_comp}'")
    conn.commit()
    cursor.close()
    conn.close()

def print_tables(select_string):
    conn = connet_to_host(host, user, dbname, password)
    cursor = conn.cursor()
    cursor.execute(select_string)
    colnames = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    result = []
    [result.append(dict(zip(colnames, row))) for row in rows]
    [print(item) for item in result]
    conn.commit()
    cursor.close()
    conn.close()


def select_all(TABLE='NEW_TABLE'):
    try:
        print_tables(f"select * from {TABLE}")
    except psycopg2.errors.UndefinedTable as p:
        print(p)

# if __name__ == '__main__':
#     conn = connet_to_host(host, user, dbname, password)
#     cursur = conn.cursor()




