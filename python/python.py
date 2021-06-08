import os
import json
from  db import cursor,conn

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
          data = cursor.execute("SELECT EXISTS(SELECT * FROM customers WHERE  id =?)",
                       (customer_id,))
          data = cursor.fetchall()
          if len(data) == 0:
              return 0
          else:
              return 1



def create_customer(customer_name):
        if customer_name != None:
            cursor.execute("INSERT INTO customers (name)  VALUES(?)",
                          (customer_name,))
            return cursor.lastrowid



def create_customer(customer_name):
        if customer_name != None:
            cursor.execute("INSERT INTO customers (name)  VALUES(?)",
                          (customer_name,))
            return cursor.lastrowid



for i, item in enumerate(json_obj):
    customer_id = validate_data(item.get("customer_id", None))
    
    customer_name = validate_data(item.get("customer_name", None))
    
    if check_customer(customer_id) == 0:
           customer_id = create_customer(customer_name)
   
    product_name = validate_data(item.get("product_name", None))
    product_price = validate_data(item.get("product_price", None))
    product_description = validate_data(item.get("product_description", None))

    cursor.execute("INSERT INTO products (customer_id, name, price, description) VALUES (?,?,?,?)",
                  (customer_id,	product_name,	product_price, product_description))
conn.commit()
conn.close()