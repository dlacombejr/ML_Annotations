import pymssql
import pandas as pd

#TODO: Replace with your SQL Connection
def get_conn():
    return pymssql.connect(server='SERVER.database.windows.net',
                            user='USER',
                            password='PASSWORD',
                            database='DATABASE')

def get_session_names():
    conn = get_conn()
    cursor = conn.cursor()
    #TODO: Replace with your query for session names
    cursor.execute("SELECT DISTINCT SessionId from TABLE")
    row = cursor.fetchone()
    data = []
    while row:
        data.append(row)
        row = cursor.fetchone()
    conn.close()
    return data

#TODO: Ensure you need everything here.
def get_session_data(sess_id):
    conn = get_conn()
    cursor = conn.cursor()
    #TODO: Replace with your data selection query
    cursor.execute("SELECT TimeStamp, Value FROM Table WHERE SessionId = %s", sess_id)
    row = cursor.fetchone()
    data = []
    while row:
        data.append(row)
        row = cursor.fetchone()
    conn.close()
    data = pd.DataFrame(data, columns = ['time', 'data'])
    data['time'] = pd.to_datetime(data['time'])
    data = data.drop_duplicates(['time'], keep='last')
    data['time'] = data['time'].dt.strftime('%Y-%m-%d %I:%M:%S')
    data = data.sort(['time'])
    return data
