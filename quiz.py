def display_scoreboard(scoreboard_list):
    """Sorts and displays the scoreboard."""
    print("\n" + "="*35)
    print(f"{'🏆 QUIZ SCOREBOARD 🏆':^35}")
    print("="*35)
    sorted_board = sorted(scoreboard_list, key=lambda student: student[1], reverse=True)
    print(f"{'Rank':<6} | {'Student Name':<15} | {'Score':<5}")
    print("-" * 35)
    for rank, entry in enumerate(sorted_board, start=1):
        name = entry[0]
        score = entry[1]
        print(f"{rank:<6} | {name:<15} | {score:<5}")
    print("="*35 + "\n")
def main():
    scoreboard = []
    print("Welcome to the Quiz Scoreboard Manager!")
    while True:
        print("Menu:")
        print("1. Add a student's score")
        print("2. View Scoreboard")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            name = input("Enter the student's name: ")
            try:
                score = float(input(f"Enter {name}'s score: "))
                scoreboard.append([name, score])
                print(f"✅ Successfully added {name} with a score of {score}.\n")
                
            except ValueError:
                print("❌ Invalid input! Please enter a numerical value for the score.\n")
                
        elif choice == '2':
            if len(scoreboard) == 0:
                print("\n⚠️ The scoreboard is currently empty. Add some scores first!\n")
            else:
                display_scoreboard(scoreboard)
                
        elif choice == '3':
            print("Exiting the Scoreboard Manager. Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
