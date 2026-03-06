import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="Radha@108MADHAV",
    host="db.bypisleryofkpwbneoms.supabase.co",
    port="5432",
    dbname="postgres"
)

print("Connected successfully")