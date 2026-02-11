import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(
        user='root',
        password='task3030',
        host='127.0.0.1',
        database='logistics'
    )
    
cursor = cnx.cursor()
cursor.execute('''select l.truck_id,  (sum(l.gross_amount) - sum(f.gallons * f.price_per_gallon))  as Profit from loads as l 
join fuel_transactions as f on   l.truck_id = f.truck_id
group by l.truck_id''')

# 3. Fetch all rows and column names
rows = cursor.fetchall()
columns = [column[0] for column in cursor.description] # Extract column names

# 4. Create the DataFrame
df = pd.DataFrame(rows, columns=columns)

# 5. Close connections
cursor.close()
cnx.close()

print(df.head())