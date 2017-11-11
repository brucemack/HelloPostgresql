# Demonstration of PostgreSQL access.
#
# You need to install the psycopg2 package for this to work.
#
# Connecting to a remote database from the command line:
# psql -h demo.ckhdu5ktphcw.us-east-1.rds.amazonaws.com -p 5432 -U bruce app
#
# Connecting to the local database from the command line:
# psql postgres
#
import psycopg2

#hostname = 'localhost'
#username = 'app'
#password = 'app'
#database = 'hackdb'

hostname = 'demo.ckhdu5ktphcw.us-east-1.rds.amazonaws.com'
username = 'bruce'
password = 'brucebruce'
database = 'app'

# Simple routine to run a query on a database and print the results:
def doQuery(conn) :
    cur = conn.cursor()
    cur.execute("SELECT * FROM t1")
    for a, b in cur.fetchall():
        print(a,b)

myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

doQuery( myConnection )
myConnection.close()
