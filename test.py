import psycopg2

def connect_to_postgres(host, dbname, user, password, port=5432):
    """Connects to a PostgreSQL database and returns the connection object."""

    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        print("Connected to PostgreSQL database")
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

if 1 == 1:
    # Replace with your actual database credentials

    conn = connect_to_postgres("localhost", "kajal", "postgres", "kajal")

    if conn:
        # Do something with the connection
        cursor = conn.cursor()
        #cursor.execute("SELECT version()")
        #cursor.execute("SELECT * FROM pg_catalog.pg_tables where schemaname = 'public' ")
        cursor.execute("SELECT * FROM public.employees;")
        #cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'public.employees;' "

        mydata = cursor.fetchone()
        print("PostgreSQL database data:", mydata)

        # Close the connection when done
        conn.close()
    else:
        print("Failed to connect to the database.")
