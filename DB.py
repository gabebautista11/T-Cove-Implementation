import psycopg2


class DB:
    def __init__(self):
        try:
            self.db_connection = psycopg2.connect(database="tcove", user='postgres', password='', host='127.0.0.1', port='5432')
            print("Connected to DB")
        except:
            print("Failed to connect to the db")

    def test_query(self):
        with self.db_connection.cursor() as curs:
                # simple single row system query
                curs.execute("SELECT * FROM Presence")
                #get the rows returned
                pg_rows = curs.fetchall()
                print(pg_rows)
