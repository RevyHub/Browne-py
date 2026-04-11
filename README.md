Overview
The Habit Tracker is a Python-based command-line application designed to help users monitor and manage their weekly habits. Users can add habits, set weekly targets, log daily completions, view progress summaries, and save or load their data using text and JSON files.
The program is modular, user-friendly, and demonstrates key Python programming concepts including functions, loops, branching, lists, dictionaries, file handling, and basic statistics.

Features
Greet the user and load previously saved habits

Add new habits with weekly targets

Log daily habit completions

View all habits with targets, totals, and progress percentages

Receive performance feedback (e.g., “Excellent progress!”)

Save reports in both text and JSON formats

Reload saved data automatically on startup

Input validation and error handling for a smooth user experience

How It Works
When the program starts, the user enters their name. The system attempts to load any existing JSON report associated with that name.
The user is then presented with a menu:

View Summary

Add New Habit

Log Habit Completion

Save Reports

Read Saved Reports

Exit

Each option triggers a dedicated function that performs the required task.

Data Structure
Habits are stored as a list of dictionaries, where each dictionary contains:

python
{
    "name": "exercise",
    "target_per_week": 3,
    "total": 1
}
This structure allows:

Easy iteration

Clear organisation

Efficient updates

Simple JSON serialization

Key Functions
add_habit(habits)
Prompts the user for a habit name and weekly target, validates input, and appends a new habit to the list.

log_today(habits)
Displays all habits and allows the user to increment the completion count for a selected habit.

show_summary(habits)
Prints a formatted table showing:

Habit name

Weekly target

Total completions

Percentage progress

Feedback message

save_report_text(name, habits)
Creates a readable .txt report summarising all habits.

save_report_json(name, habits)
Saves the habit list in structured JSON format for future loading.

read_report(name)
Displays previously saved text and JSON reports.

load_habits(name)
Loads habit data from a JSON file if it exists.

get_int_input(prompt, min_val, max_val)
Ensures the user enters a valid integer within a specified range.

progress_feedback(rate)
Returns a feedback message based on percentage completion.

File Handling
The program uses two file formats:

Text Report
Human-readable

Saved using open(filename, "w")

Includes habits, targets, totals, and progress

JSON Report
Machine-readable

Saved using json.dump()

Used to reload habits when the program restarts

Example Workflow
User enters their name

Program loads existing habits (if available)

User adds a habit:

Name: “Exercise”

Target: 3 times per week

User logs completions

User views summary:

Exercise: 2/3 → 66.7% → “Keep going!”

User saves reports

User exits the program

Error Handling
The application includes:

Input validation for integers

Menu validation

Range checking for habit selection

Graceful handling of missing files

This prevents crashes and ensures a smooth user experience.

Requirements
Python 3.x

No external libraries required (uses only built-in modules)

Running the Program
Run the script using:

bash
python habit_tracker.py
The program will start immediately and guide the user through the menu.

Future Improvements
Add a graphical interface (Tkinter)

Add charts or graphs for visual progress

Support daily or monthly targets

Add reminders or notifications


