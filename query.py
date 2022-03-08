import sqlite3
import services
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


def get_all_occupied_rooms():
    cursor.execute(
        '''UPDATE user_room SET is_active=false WHERE end_time < DATETIME('now', 'localtime') and is_active=true;''')
    connection.commit()
    cursor.execute(
        '''SELECT * FROM user_room LEFT JOIN room ON user_room.room_id = room.id LEFT JOIN user ON user_room.user_id = user.id WHERE is_active=true''')
    user_rooms = cursor.fetchall()
    return user_rooms


def is_occupy(room_id):
    cursor.execute('''SELECT id, end_time FROM user_room WHERE is_active=? and room_id=?''',
                   [True, room_id])
    user_room = cursor.fetchone()
    if user_room is not None:
        pk = user_room[0]
        end_time = user_room[1]
        if end_time is int:
            end_time = datetime.fromtimestamp(end_time / 1000)
        else:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        if datetime.now() > end_time:
            cursor.execute('''UPDATE user_room SET is_active=false WHERE id=?''', [pk])
            connection.commit()
            return True
        return False
    return True


def occupied_by_user(start_time, end_time, user_id, room_id):
    # sending mail and checking ids
    cursor.execute('''SELECT username, email FROM user WHERE id=?''', [user_id])
    user = cursor.fetchone()
    if user is None:
        return "Please enter the valid data (user_id is incorrect)."
    cursor.execute('''SELECT title FROM room WHERE id=?''', [room_id])
    room = cursor.fetchone()
    if room is None:
        return "Please enter the valid data (room_id is incorrect)."
    services.send_mail(user, start_time, end_time, room)

    if is_occupy(room_id=room_id):
        cursor.execute(
            '''INSERT INTO user_room (start_time, end_time, is_active, user_id, room_id) 
            VALUES (?, ?, ?, ?, ?)''', [start_time, end_time, True, user_id, room_id])
        connection.commit()

        return "Occupied Success"
    else:
        cursor.execute('''SELECT * FROM user_room WHERE is_active=? and room_id=?''', [True, room_id])
        user_room = cursor.fetchone()
        return user_room
