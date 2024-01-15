import mysql.connector

try:
    conn =mysql.connector.connect(
        user ="pma",
        passwd="",
        database ="test"
        )
    print(conn)
except mysql.connectoe.Error as e:
    print(e)
    
