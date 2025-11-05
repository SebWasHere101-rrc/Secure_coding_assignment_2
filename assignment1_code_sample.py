import os
import pymysql
from urllib.request import urlopen

"""
The password in general is in plain text. It can be compromised because 
the password is stored in a plain text on a application's properties or a configuration file.
"""
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

"""
On the send_email section this could potentially be some Identification and authentication failures because the attacker
needed a confirmation of the user's identity, its authentications, and the session management.
"""
def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

"""
On the get_data section this url is trying to redirect the user onto that website meaning this is a DOM Based XSS.
The page itself does not change, but the client side code could contain the pages to execute unexpectedly or differently
possibly leading to a malicious modifications that can occured in the DOM environment.
"""
def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

"""
On the save_to_db this type of vulnerability is called an Sql injection. its like a database query
that can use a string concatenation and user supplied input. It exploits the sensitive data from the database,
executing the administration operations on the database.
"""
def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
