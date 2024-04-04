print("Hello World")

import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'example', password = 'r0.#V1a?TH@r$N')


cursor = connection.cursor()


addData = ('INSERT INTO favs(Ranking, Name, Genre, Fav_Song) VALUES (5, "NCT", "K-Pop", "Jet Lag")')


cursor.execute(addData)


testQuery = ('SELECT * FROM favs')


cursor.execute(testQuery)


for item in cursor:

    print(item)

 

cursor.close()

connection.close()
