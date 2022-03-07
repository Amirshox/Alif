import sqlite3
from datetime import datetime

connection = sqlite3.connect('alif.db')
cursor = connection.cursor()


def get_all_users():
    cursor.execute('''SELECT * FROM user''')
    users = cursor.fetchall()
    return users


def get_user(pk):
    cursor.execute('''SELECT * FROM user WHERE id=?''', [pk])
    user = cursor.fetchone()
    return user


def get_all_rooms():
    cursor.execute('''SELECT * FROM room''')
    rooms = cursor.fetchall()
    return rooms


def get_room(pk):
    cursor.execute('''SELECT * FROM room WHERE id=?''', [pk])
    room = cursor.fetchone()
    return room


def get_all_user_room():
    cursor.execute('''SELECT * FROM user_room''')
    user_room = cursor.fetchall()
    return user_room


def get_user_room(pk):
    cursor.execute('''SELECT * FROM user_room WHERE id=?''', [pk])
    user_room = cursor.fetchone()
    return user_room


def is_reservation(room_id):
    cursor.execute('''SELECT id, end_time FROM user_room WHERE is_active=? and room_id=?''',
                   [True, room_id])
    user_room = cursor.fetchone()
    pk = user_room[0]
    end_time = user_room[1]
    end_time = datetime.fromtimestamp(end_time / 1000)
    if datetime.now() > end_time:
        cursor.execute('''UPDATE user_room SET is_active=false WHERE id=?''', [pk])
        connection.commit()
        return True
    return False


def reserve_by_user(user_id, room_id, **kwargs):
    if is_reservation(room_id=room_id):
        cursor.execute(
            '''INSERT INTO user_room (start_time, end_time, is_active, user_id, room_id) 
            VALUES (?, ?, ?, ?, ?)''', [])


print(get_all_users())
print(get_user(pk=2))
print(get_all_rooms())
print(get_room(pk=2))
print(get_all_user_room())
print(get_user_room(pk=1))
print(is_reservation(room_id=1))
