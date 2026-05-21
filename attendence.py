def display_attendance(attendance_data):
    print("\n" + "="*45)
    print(f"{'📋 ATTENDANCE REPORT 📋':^45}")
    print("="*45)
    if len(attendance_data) == 0:
        print("⚠️ No students found. Please add students first.")
        print("="*45 + "\n")
        return
    print(f"{'Student Name':<15} | {'Present':<7} | {'Absent':<7} | {'Attendance %':<12}")
    print("-" * 45)
    for name, stats in attendance_data.items():
        present = stats['present']
        absent = stats['absent']
        total_days = present + absent
        if total_days > 0:
            percentage = (present / total_days) * 100
        else:
            percentage = 0.0
        print(f"{name:<15} | {present:<7} | {absent:<7} | {percentage:.1f}%")
    print("="*45 + "\n")
def main():
    attendance_data = {}
    print("Welcome to the Attendance Tracker!")
    while True:
        print("Menu:")
        print("1. Add a new student")
        print("2. Mark attendance for today")
        print("3. View Attendance Report")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            name = input("Enter the student's name: ").strip()
            if name in attendance_data:
                print(f"⚠️ '{name}' is already in the system.\n")
            else:
                attendance_data[name] = {'present': 0, 'absent': 0}
                print(f"✅ Successfully added '{name}' to the tracker.\n")
        elif choice == '2':
            if not attendance_data:
                print("\n⚠️ No students in the system. Add students first.\n")
                continue  
            print("\n--- Marking Today's Attendance ---")
            for name in attendance_data:
                while True:
                    status = input(f"Is {name} Present (P) or Absent (A)? ").strip().upper()
                    if status == 'P':
                        attendance_data[name]['present'] += 1
                        break
                    elif status == 'A':
                        attendance_data[name]['absent'] += 1
                        break
                    else:
                        print("❌ Invalid input. Please enter 'P' or 'A'.")
            print("✅ Attendance marked for all students!\n")
        elif choice == '3':
            display_attendance(attendance_data) 
        elif choice == '4':
            print("Exiting the Attendance Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
