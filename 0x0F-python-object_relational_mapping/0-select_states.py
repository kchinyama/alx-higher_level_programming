#!/usr/bin/python3
"""
demo script that displays all cities in database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    mycur = db.cursor()

    mycur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = mycur.fetchall()

    for k in rows:
        print(k)

    mycur.close()
    db.close()
