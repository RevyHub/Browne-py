import json

def save_report_text(name, habits):
    filename = f"{name}_habit_report.txt"
    with open(filename, "w") as file:
        file.write(f"Habit Tracker Summary for {name}\n")
        file.write("=" * 50 + "\n")
        for h in habits:
            target = h["target_per_week"]
            achieved = h["total"]
            rate = (achieved / target) * 100 if target > 0 else 0
            status = progress_feedback(rate)
            file.write(f"{h['name']}: Target={target}, Done={achieved}, Rate={rate:.1f}% - {status}\n")
    print(f"\nYour text report has been saved as {filename}.")

def save_report_json(name, habits):
    filename = f"{name}_habit_report.json"
    with open(filename, "w") as file:
        json.dump({"name": name, "habits": habits}, file, indent=4)
    print(f"Your JSON report has been saved as {filename}.")

def read_report(name):
    print("\n--- Checking for saved reports ---")
    try:
        with open(f"{name}_habit_report.txt", "r") as file:
            print("\nTEXT REPORT:")
            print(file.read())
    except FileNotFoundError:
        print("No text report found.")
    try:
        with open(f"{name}_habit_report.json", "r") as file:
            print("\nJSON REPORT:")
            print(json.load(file))
    except FileNotFoundError:
        print("No JSON report found.")

def load_habits(name):
    try:
        with open(f"{name}_habit_report.json", "r") as file:
            data = json.load(file)
            return data["habits"]
    except FileNotFoundError:
        return []

def progress_feedback(rate):
    if rate >= 80:
        return "Excellent progress!"
    elif rate >= 50:
        return "Keep going!"
    else:
        return "Needs improvement."

def get_int_input(prompt, min_val=0, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if (max_val is not None and value > max_val) or value < min_val:
                print(f"Please enter a number between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("That wasn’t a number, try again.")

def show_summary(habits):
    print("\nNo.  Habit       Target     Done   Rate       Status")
    print("-" * 60)
    for i, h in enumerate(habits, start=1):
        target = h["target_per_week"]
        achieved = h["total"]
        rate = (achieved / target) * 100 if target > 0 else 0
        status = progress_feedback(rate)
        print(f"{i:<5}{h['name']:<12}{target:<11}{achieved:<7}{rate:.1f}%   {status}")

def add_habit(habits):
    name_new = input("Enter the name of your new habit: ")
    target_new = get_int_input("How many times per week do you want to do it? ", min_val=1)
    habits.append({"name": name_new, "target_per_week": target_new, "total": 0})
    print(f"Great! Habit '{name_new}' added with target {target_new} per week.")

def log_today(habits):
    if not habits:
        print("You don’t have any habits yet. Add one first!")
        return
    show_summary(habits)
    pick = get_int_input("Which habit did you complete today? Enter number: ", min_val=1, max_val=len(habits))
    habits[pick - 1]["total"] += 1
    print(f"Nice work! You logged progress for '{habits[pick - 1]['name']}'.")

def habit_tracker():
    print("Welcome to your Habit Tracker!")
    name = input("What’s your name? ")
    habits = load_habits(name)

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Summary")
        print("2. Add New Habit")
        print("3. Log Habit Completion")
        print("4. Save Reports")
        print("5. Read Saved Reports")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_summary(habits)
        elif choice == "2":
            add_habit(habits)
        elif choice == "3":
            log_today(habits)
        elif choice == "4":
            save_report_text(name, habits)
            save_report_json(name, habits)
        elif choice == "5":
            read_report(name)
        elif choice == "6":
            print("Goodbye! Keep up your habits!")
            break
        else:
            print("That’s not a valid choice, try again.")

habit_tracker()
