import mysql.connector


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='admin',
         autocommit=True
         )



def get_countries(country_ident):
    sql_name = f"SELECT airport.name, country.name, airport.ident, airport.iso_country, latitude_deg, longitude_deg " \
             f"from airport LEFT JOIN country ON airport.iso_country = country.iso_country " \
             f"where airport.continent = 'EU' and airport.type = 'large_airport' " \
             f"order BY country.name, airport.name ASC ;"

    cursor = connection.cursor()
    cursor.execute(sql_name)
    result = cursor.fetchall()

    return result


