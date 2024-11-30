import sqlite3

def read_accounts_db(file_path):
    """Read and extract email accounts from an SQLite database."""
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tables found: {tables}")

        cursor.execute("SELECT * FROM accounts;")  # Replace 'accounts' with the actual table name
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
    except Exception as e:
        print(f"Error: {str(e)}")
