# Demonstration of PostgreSQL access.
#
import psycopg2

# hostname = 'localhost'
# username = 'app'
# password = 'app'
# database = 'hackdb'

hostname = 'demo.ckhdu5ktphcw.us-east-1.rds.amazonaws.com'
username = 'bruce'
password = 'brucebruce'
database = 'app'


# Simple routine to run a query on a database and print the results:
def doquery(conn) :
    cur = conn.cursor()
    cur.execute("SELECT * FROM t1")

    r = cur.fetchall();

    print("The raw cursor:");
    print(type(r));

    print(r);
    print("Iterating across the list");
    for a, b in r:
        print(a,b)


myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

doquery( myConnection )

myConnection.close()
