################################################################
#THis is it. i'm commiting to this idea.
#Here we try to break things. mostly numbers but brains occasionally as well.
#Objective: functionally show divisibility of very large numbers using partial base conversion.
#Ken Smith 8/12/2024
#original concept september 2020
################################################################
import sqlite3
import morePrimes

#print("Let's get down to business!!")
print("WELCOME! to the FACTOR-INATOR!!\nWith this device I will determine all prime factors less than 130,000 accross the TRI-STATE AREA!!!")

# Define the path to your SQLite database
database_path = 'morePrimeFactors.db'

# Connect to the SQLite database
connection = sqlite3.connect(database_path)

# Create a cursor object using the connection
cursor = connection.cursor()

#752 place values to be useful.......
#well. shoot. i figured that in attempt at doing this would be tough. and intense from the computational standpoint.
#For proof of concept we will prove it out with numbers form 1 - 100;

num = input("Enter a large number (20 digit max):\n")
#consider the number as a string of place values, and not as a single entity.
mun = num[::-1]

#for a given number N we want to know if it is divisible by a second number B
#therefore, it will be for and repeated lookups.
divisors = []
try:
    #print(f"lets determine if {num} is divisible by anything 1-1000!\n");
    for i in morePrimes.things:
        if(i > int(num)):
            break;
        print(f"looking for divisibility of {num} by {i}")
        units = 0
        query = f'SELECT id, unitsValue FROM table_for_base_{i}'# WHERE id={n+1}' #table for the factor we are trying, where id is the placevalue in question
        print(query)
        # Execute the SQL query
        cursor.execute(query)
    
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
        for n in range(len(mun)):
            #print(f"checking the {10**n}s place, value of {mun[n]}")
            #look up each place value in a DB table pre-populated in the following manner.
            #for the primary quantity of the place value (1, 10, 100, 1000, ...) know how that value converts to the number system in base B

            # Define the SQL query to retrieve data from the 'users' table
            
    
            # Iterate over the rows
            #the value gained from the DB is multiplied by the place values value, the sum of the resulting products is then calculated.
            #for row in rows:
                #print(query)
            print(f"ID: {rows[n][0]}, Units: {rows[n][1]}")
            units += (int(rows[n][1]) * int(mun[n]))
            if(units >= i):
                units = units % i
        #print(f"total converted units place value of {units}")
        if(units == 0):#if that sum (in base B) end in a 0
            #print(f"found a divisor: {i}")#then it is divisible. if it is not, then it is not divisible.
            divisors.append(i)
        
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Close the cursor and connection
finally:
    cursor.close()
    connection.close()

#final output!
print(f"Found Factors for {num}!\n")
print(divisors)#1,2,4,8,16,17,34,68,136,272