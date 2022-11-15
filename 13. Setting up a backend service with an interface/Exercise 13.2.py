# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format.
# The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

import mysql.connector
from flask import Flask

app = Flask(__name__)
@app.route('/airport/<code>')
def airport(code):
    code = str(code)
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident= '" + code + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            response = {
                "ICAO": code,
                "Name": row[1],
                "Location": row[2]
            }
            return response

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='python_13.2',
         user='root',
         password='MariaDB',
         autocommit=True
         )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)