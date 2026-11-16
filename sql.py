import mysql.connector


def manage_users():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='user_manager',
            password='1234',
            database='users'
        )
        cursor = connection.cursor()
        print("etesal movafagh bood")

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_information(
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                password VARCHAR(50),
                status VARCHAR(50)
            );
        """)
        print("jadval sakhte shod")

        
        sql = """
            INSERT INTO user_information (username, password, status)
            VALUES (%s, %s, %s)
        """
        values = ("ali", "12345", "active")
        cursor.execute(sql, values)
        connection.commit()
        print("etelaat ba movafaghiyat sabt shod")

        
        cursor.execute("SELECT * FROM user_information")
        result = cursor.fetchall()
        for row in result:
            print(row)

    except mysql.connector.Error as error:
        print(f"khata: {error}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("etesal baste shod")


if __name__ == "__main__":
    manage_users()
