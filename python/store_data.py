import os
import json
from  db import cursor,conn,mariadb


# read JSON file which is in the next parent folder
file = os.path.abspath('products.json')
json_data=open(file).read()
json_obj = json.loads(json_data)


def validate_data(val):
   if val != None:
        if type(val) is str:
            return str(val).encode('utf-8')
        else:
            return val
   else:
        return 0

def check_customer(customer_id):
     if customer_id != None:
        try:
            cursor.execute("SELECT EXISTS(SELECT * FROM customers WHERE  id =?)",
                        (customer_id,))
            data = cursor.fetchall()
            if data[0][0] == 0:
                return 0
            else:
                return 1
            
        except mariadb.Error as e:
             print(f"Error adding entry to database: {e}")



def create_customer(customer_id,customer_name):
        if customer_name != None:
            try:
                cursor.execute("INSERT INTO customers (id,name)  VALUES(?,?)",
                                (customer_id,customer_name,))
                return cursor.lastrowid
            
            except mariadb.Error as e:
                print(f"Error adding entry to database: {e}")


def store_product(customer_id,	product_name,	product_price, product_description):
        if customer_id != None:
            try:
                 cursor.execute("INSERT INTO products (customer_id, name, price, description) VALUES (?,?,?,?)",
                                (customer_id,	product_name,	product_price, product_description))
                 
                 print("Product Data inserted Successfully")
            
            except mariadb.Error as e:
                print(f"Error adding entry to database: {e}")
                   
        else:
           return "customer_id does not exist in database"



# inserting  one by one
for i, item in enumerate(json_obj): 
            customer_id = validate_data(item.get("customer_id", None))
            customer_name = validate_data(item.get("customer_name", None))
            product_name = validate_data(item.get("product_name", None))
            product_price = validate_data(item.get("product_price", None))
            product_description = validate_data(item.get("product_description", None))

            if check_customer(customer_id) == 0:
                customer_id = create_customer(customer_id,customer_name)
                store_product(customer_id,	product_name,	product_price, product_description)
            else:
                store_product(customer_id,	product_name,	product_price, product_description)
                
conn.commit()
conn.close()




# inserting  multiple columns          
# def store_multiple_product(product_data):
#             try:
#                  cursor.executemany("INSERT INTO products (customer_id, name, price, description) VALUES (?,?,?,?)",
#                                 (product_data))
                 
#                  print("Product Data inserted Successfully")
            
#             except mariadb.Error as e:
#                 print(f"Error adding entry to database: {e}")
                
#             finally:
#                if conn:
#                     conn.commit()
#                     conn.close()
#                     print("The mariadb connection is closed")



# product_data = []
# for i, item in enumerate(json_obj): 
#          del item["customer_name"]
#          product_data.append(tuple(item.values()))
# store_multiple_product(list(product_data)) 