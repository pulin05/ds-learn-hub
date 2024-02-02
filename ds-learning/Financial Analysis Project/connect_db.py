import psycopg2

conn = psycopg2.connect(
database="Financial Analysis",
user="postgres",
password="sql@2023",
host="localhost",
port= '5432'
)

cur = conn.cursor()

# Execute a query
cur.execute("select * from public.nse_company")

# Retrieve query results
records = cur.fetchall()
print(records)