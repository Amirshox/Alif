import sqlite3

connection = sqlite3.connect('alif.db')

crsr = connection.cursor()

create_user_table = """CREATE TABLE IF NOT EXISTS user (
    id INTEGER  PRIMIRY KEY,
    username VARCHAR(20),
    email VARCHAR(20),
    phone_number VARCHAR(20)
)"""

create_room_table = """CREATE TABLE IF NOT EXISTS room (
    id INTEGER PRIMIRY KEY,
    title VARCHAR(20)
)"""

create_user_room_table = """CREATE TABLE IF NOT EXISTS user_room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    is_active BOOLEAN,
    
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES room(id) ON DELETE CASCADE
)"""

crsr.execute(create_user_table)
crsr.execute(create_room_table)
crsr.execute(create_user_room_table)

connection.close()
