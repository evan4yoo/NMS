import mysql.connector
import settings

mysql_settings=settings.SetConfig()


def dbsetup():
    try:
        print("Connecting to database..)")
        c = mysql.connector.connect(
            host=mysql_settings.dbhost,
            user=mysql_settings.dbuser,
            passwd=mysql_settings.dbpasswd,
            # database=mysql_settings.dbname,
        )
    except ConnectionRefusedError:
        print("Connections Refused")
        exit(2)

    except:
        print("Unknown Error")
        exit(3)

    print(f"Now connected to {mysql_settings.dbhost}")
    return c


def read_db(dbname):
    con = dbsetup()
    dbo = con.cursor()
    if dbname == '':
        print("caught null dbname")
        dbo.execute("SHOW DATABASES WHERE 'testdb'")
        for db in dbo:
            print(db)
        return
    else:
        print("caught dbname")
        print(type(dbo))
        result = dbo.execute(f"SHOW DATABASES WHERE {dbname}")
        print(type(result))
        print(result)
        return result


def read_table(self):
    pass


def write_table(self):
    pass


def setup():
    con = dbsetup()
    dbo = con.cursor()
    # Checking database to see if testdb exists
    dbo.execute("SHOW DATABASES")
    dbfetch = dbo.fetchall()
    dbstate = False
    if "testdb" in dbfetch:
        print("Found testdb!")
        dbstate = True
    else:
        print(dbfetch)
        pass
    # if dbstate is true, database exists proceed to checking table
    if dbstate == True:
        pass
    elif dbstate == False:
        print("Corrupt/Missing database rerun setup")
        exit(0)
    else:
        print("This can't happen.")
        exit(1)








