import os
import json
from  db import cursor,conn,mariadb
       
def fetch_data(customer_id):
            try:
                 cursor.execute("SELECT * FROM products INNER JOIN customers ON products.customer_id = customers.id where customer_id=?",
                                (customer_id,))
                 data = cursor.fetchall()
                 for row in data:

                    print("Customer Id: ", row[1])
                    print("Customer Name: ", row[6])
                    print("Product Id: ", row[0])
                    print("Product Name: ", row[2])
                    print("Product Price: ", row[3])
                    print("Product Description: ", row[4])
                    print("\n")
                    
            except mariadb.Error as e:
                 print(f"Error adding entry to database: {e}")
            finally:
               if conn:
                    conn.close()
                    print("The mariadb connection is closed")
          
          
          
fetch_data(1004)