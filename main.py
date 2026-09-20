import csv
import json   # 👈 add this at top

# CSV functions
def add_student(name, age):
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age])
    print("Student saved")

def view_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No data found")

# JSON example
def save_json():
    data = {"name": "Vennela", "age": 20}
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("JSON file created")

# Menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Save JSON")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        add_student(name, age)

    elif choice == "2":
        view_students()

    elif choice == "3":
        save_json()

    elif choice == "4":
        break

    else:
        print("Invalid choice")