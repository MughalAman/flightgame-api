import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='admin',
         autocommit=True
         )



def get_countries():
    cursor = connection.cursor()
    cursor.execute(f"Select * from countries")
    result = cursor.fetchall()
    return result

