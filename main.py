from database import init_db
from habits import add_habit, list_habits, mark_habit
from analytics import habit_stats, best_day

init_db()


def menu():
    print("""
1. Create habit
2. List habits
3. Mark habit as done
4. View statistics
5. Best day
0. Exit
""")


while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        name = input("Habit name: ")
        add_habit(name)

    elif choice == "2":
        habits = list_habits()
        for h in habits:
            print(f"{h[0]} - {h[1]}")

    elif choice == "3":
        habit_id = int(input("Habit ID: "))
        mark_habit(habit_id)

    elif choice == "4":
        habit_id = int(input("Habit ID: "))
        print(habit_stats(habit_id))

    elif choice == "5":
        print(best_day())

    elif choice == "0":
        break

    else:
        print("Invalid option")
