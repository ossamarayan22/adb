import sqlite3

def create_db():
    """إنشاء قاعدة بيانات SQLite جديدة."""
    conn = sqlite3.connect('proflash.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS devices
                      (id INTEGER PRIMARY KEY, device_name TEXT, serial_number TEXT)''')
    conn.commit()
    conn.close()

def insert_device(device_name, serial_number):
    """إدخال معلومات جهاز في قاعدة البيانات."""
    conn = sqlite3.connect('proflash.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO devices (device_name, serial_number)
                      VALUES (?, ?)''', (device_name, serial_number))
    conn.commit()
    conn.close()

def get_device_info():
    """استرجاع معلومات الأجهزة المخزنة في قاعدة البيانات."""
    conn = sqlite3.connect('proflash.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM devices''')
    devices = cursor.fetchall()
    conn.close()
    return devices
