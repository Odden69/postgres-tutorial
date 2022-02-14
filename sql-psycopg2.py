import psycopg2


# connect to "chinook" database (could include username, password, host etc)
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the Artist table
# The query MUST be wrapped in single quotes, double quotes for values
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the name column from the Artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only Queen from the Artist table,
# %s is a Python string place holder
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only no 51 from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', ["51"])

# Query 5 - select only the albums from the Album table with ArtistId 51
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["270"])

# Query 6 - select all tracks from the Track table with Composer Queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results from the cursor
results = cursor.fetchall()

# To fetch a single result
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
