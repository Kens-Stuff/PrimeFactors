import sqlite3
import random
#import thousandPrimes
import morePrimes

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('morePrimeFactors.db')
cursor = conn.cursor()

# Function to create a table and populate it with data
def create_and_populate_table(table_name, base):
    # Create the table
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        unitsValue INTEGER
    )
    ''')
    conn.commit()
    spots = 20 #compute for this many place values
    for N in range(spots):
        pv = 10**N
        units_from_place_value = ((10**N) % base)
        
        #IF there is concern over correctness, call for bases below 26 ONLY
        # digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
        # result = ""
        # n = pv
        # while n > 0:
            # remainder = n % base
            # result = digits[remainder] + result
            # n //= base
            
        # print(f"{pv} in base {base} is: {result}")
        cursor.execute(f'''
        INSERT INTO {table_name} (unitsValue)
        VALUES (?)
        ''', [units_from_place_value])
    
    # Commit the transaction
    conn.commit()

# Create and populate tables for prime bases >=2.
for i in morePrimes.things:
    table_name = f'table_for_base_{i}'
    create_and_populate_table(table_name, i)
    print(f'{table_name} created and populated with {20} entries.')

# Close the connection

conn.close()