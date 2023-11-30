import mysql.connector

cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345"
)

cursor = cnx.cursor()

# Create a new database named "passman"
cursor.execute("CREATE DATABASE IF NOT EXISTS passman")

print("Database created successfully.")
cursor.execute("USE passman")

# Create the passwords table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INT AUTO_INCREMENT PRIMARY KEY,
        service VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        `key` VARCHAR(255) NOT NULL
    )
""")

print("Table created successfully.")
# Close the cursor and connection
cursor.close()
cnx.close()



import base64
import pymysql

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet

def encrypt_password(password, key):
    password = password.encode()
    cipher = Fernet(key)
    ct = cipher.encrypt(password)
    return base64.b64encode(ct).decode()

def decrypt_password(hashed_password, key):
    hashed_password = base64.b64decode(hashed_password.encode())
    cipher = Fernet(key)
    password = cipher.decrypt(hashed_password)
    return password.decode()


'''
def add_password(service, username, password):
    cnx = pymysql.connect(user='root', password='12345',
                                  host='localhost',
                                  database='passman')
    cursor = cnx.cursor()
    key = Fernet.generate_key()
    hashed_password = encrypt_password(password, key)
    add_password_query = ("INSERT INTO passwords "
                          "(service, username, password, `key`) "
                          "VALUES (%s, %s, %s, %s)")
    add_password_data = (service, username, hashed_password, key)
    cursor.execute(add_password_query, add_password_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Password added successfully!")'''

def add_password(service, username, password):
    cnx = pymysql.connect(user='root', password='12345',
                                  host='localhost',
                                  database='passman')
    cursor = cnx.cursor()
    get_password_query = ("SELECT COUNT(*) FROM passwords "
                      "WHERE service=%s AND username=%s")
    get_password_data = (service, username)
    cursor.execute(get_password_query, get_password_data)
    count = cursor.fetchone()[0]
    if count > 0:
        print("Credentials already exist for this service and username.")
    else:
        key = Fernet.generate_key()
        hashed_password = encrypt_password(password, key)
        add_password_query = ("INSERT INTO passwords "
                              "(service, username, password, `key`) "
                              "VALUES (%s, %s, %s, %s)")
        add_password_data = (service, username, hashed_password, key)
        cursor.execute(add_password_query, add_password_data)
        cnx.commit()
        print("Password added successfully!")
    cursor.close()
    cnx.close()


def get_password(service, username):
    cnx = pymysql.connect(user='root', password='12345',
                                  host='localhost',
                                  database='passman')
    cursor = cnx.cursor()
    get_password_query = ("SELECT password, `key` FROM passwords "
                      "WHERE service=%s AND username=%s")

    get_password_data = (service, username)
    cursor.execute(get_password_query, get_password_data)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    if result:
        hashed_password, key = result
        return decrypt_password(hashed_password, key)
    else:
        return None

def update_password(service, username, password):
    cnx = pymysql.connect(user='root', password='12345',
                                  host='localhost',
                                  database='passman')
    cursor = cnx.cursor()
    key = Fernet.generate_key()
    hashed_password = encrypt_password(password, key)
    update_password_query = ("UPDATE passwords "
                             "SET password=%s, `key`=%s "
                             "WHERE service=%s AND username=%s")
    update_password_data = (hashed_password, key, service, username)
    cursor.execute(update_password_query, update_password_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Password updated successfully!")

def delete_password(service, username):
    cnx = pymysql.connect(user='root', password='12345',
                                  host='localhost',
                                  database='passman')
    cursor = cnx.cursor()
    delete_password_query = ("DELETE FROM passwords "
                          "WHERE service=%s AND username=%s")
    delete_password_data = (service, username)
    cursor.execute(delete_password_query, delete_password_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Password deleted successfully!")



print("What would you like to do?")
print("1. Add a password")
print("2. Get a password")
print("3. Update password")
print("4. Delete password")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    service = input("Enter service: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    add_password(service, username, password)

elif choice == 2:
    service = input("Enter service: ")
    username = input("Enter username: ")
    password = get_password(service, username)
    if password:
        print("Password:", password)
    else:
        print("No password found.")


elif choice == 3:
    service = input("Enter service: ")
    username = input("Enter username: ")
    password = input("Enter new password: ")
    update_password(service, username, password)

elif choice == 4:
    service = input("Enter service: ")
    username = input("Enter username: ")
    delete_password(service, username)

else:
    print("Invalid choice. Enter a number between 1 and 4.")
