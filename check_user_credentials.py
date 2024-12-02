import sqlite3


def check_user_credentials(username, password):
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()

        # Query to find user by username and password
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()  # Fetch the first result

        conn.close()

        if user:
            return True  # User found and credentials are correct
        else:
            return False  # Invalid credentials
    except Exception as e:
        print(f"Error checking user credentials: {e}")
        return False
