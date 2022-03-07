import sys
import query
import utils

if __name__ == '__main__':
    if sys.argv[1] == 'users':
        for user in query.get_all_users():
            print(f"{user[0]} {user[1]}")
    elif sys.argv[1] == 'user' and sys.argv[2].isdigit():
        pk = sys.argv[2]
        print(pk)
        print(query.get_user(pk))
    elif sys.argv[1] == 'rooms':
        for room in query.get_all_rooms():
            print(f"{room[0]} {room[1]}")
    elif sys.argv[1] == 'room' and sys.argv[2].isdigit():
        pk = sys.argv[2]
        print(pk)
        print(query.get_room(pk))
    elif sys.argv[1] == 'check_room' and sys.argv[2].isdigit():
        pk = sys.argv[2]
        print(query.is_reservation(pk))
    elif sys.argv[1] == 'reservation':
        start_time, end_time = utils.date_validator(sys.argv[2], sys.argv[3])
        user_id = sys.argv[4]
        room_id = sys.argv[5]
        if start_time is not False and end_time is not False:
            print(query.reservation_by_user(start_time, end_time, user_id, room_id))
        else:
            print("Please input correct date format like this (25-03-2022/12:45)")
