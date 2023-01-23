import mysql.connector

# Koneksi ke database
cnx = mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="database_name"
)

cursor = cnx.cursor()

# Membuat tabel
create_table = """
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
"""
cursor.execute(create_table)

# Menambahkan data
add_user = "INSERT INTO users (name, email) VALUES (%s, %s)"
user_data = ("Khoirudin", "Khoirudin@example.com")
cursor.execute(add_user, user_data)
cnx.commit()

# Mengambil data
query = "SELECT * FROM users"
cursor.execute(query)

for (id, name, email) in cursor:
    print("ID: {}, Name: {}, Email: {}".format(id, name, email))

# Menutup koneksi
cursor.close()
cnx.close()