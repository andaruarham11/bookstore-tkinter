"""# importing module
from tkinter import *
import mysql.connector

root = Tk()
root.title("coba")
root.geometry("400x400")

#creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Admin123_"
)

#create a cursor and initialize it
my_cursor = mydb.cursor()

#testing
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

#printing the connection object
#print(mydb)



root.mainloop()"""
# -----------------------------------------------------------------------------------------
"""import json
import requests

r = requests.get('https://reqres.in/api/unknown')
y = json.dumps(r)
print(y)"""
# -----------------------------------------------------------------------------------------
"""import json

person_dict = {'name': 'Bob','age': 12,'children': None}
person_json = json.dumps(person_dict)
#output
print(person_json)"""
# ---------------------------------------------------------------------------------------
# coba ngefetch data dari json
import json
import requests

res = requests.get('https://reqres.in/api/users?page=2')
# print(f'Total users: {res.json().get("total")}')
# json_res = res.json()
# print(json_res.get(data['id']))
data_request = res.json()
for data in data_request['data']:
    id = data['id']
    email = data['email']
    fn = data['first_name']
    ln = data['last_name']
    # print(id)
    # print(email)
    # print(fn)
    # print(ln)
    print(f"{id} {email} {fn} {ln}")
    # print(email)
    # print(data_request['data'][0]['id']['email']['first_name']['last_name']['avatar'])
    # parsed = json.loads(data_request['data'])
    # print(json.dumps(parsed, indent=2, sort_keys=True))
