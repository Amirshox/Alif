import sys
import query
import utils

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            if sys.argv[1] == 'users':
                print("| id | name | mail | phone |")
                for user in query.get_all_users():
                    print(f"| {user[0]} | {user[1]} | {user[2]} | {user[3]} |")
            elif sys.argv[1] == 'rooms':
                print("| id | name |")
                for room in query.get_all_rooms():
                    print(f"| {room[0]} | {room[1]} |")
            elif sys.argv[1] == 'reserve_rooms':
                for user_room in query.get_all_reserve_rooms():
                    print(f"{user_room[7]} reserved during from {user_room[1]} to {user_room[2]} by {user_room[9]}")

        elif len(sys.argv) == 3:
            if sys.argv[1] == 'user' and sys.argv[2].isdigit():
                pk = sys.argv[2]
                user = query.get_user(pk)
                print("| id | name | mail | phone |")
                print(f"| {user[0]} | {user[1]} | {user[2]} | {user[3]} |")
            elif sys.argv[1] == 'room' and sys.argv[2].isdigit():
                pk = sys.argv[2]
                room = query.get_room(pk)
                print("| id | name |")
                print(f"| {room[0]} | {room[1]} |")
            elif sys.argv[1] == 'check_room' and sys.argv[2].isdigit():
                pk = sys.argv[2]
                is_reservation = query.is_reservation(pk)
                if is_reservation:
                    print("Room is Free")
                else:
                    print("Room reserved")

        elif len(sys.argv) == 6:
            if sys.argv[1] == 'reservation' and sys.argv[4].isdigit() and sys.argv[5].isdigit():
                start_time, end_time = utils.date_validator(sys.argv[2], sys.argv[3])
                user_id = sys.argv[4]
                room_id = sys.argv[5]
                if start_time is not False and end_time is not False:
                    query.reservation_by_user(start_time, end_time, user_id, room_id)
                    print(f"Reserved Success")
                else:
                    print("Please input correct date format like this (25-03-2022/12:45)")
        else:
            print("Undefined Command")
    except TypeError:
        print("Not Found")
