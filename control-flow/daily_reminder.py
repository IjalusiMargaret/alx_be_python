def main():
    # Step 1: Prompt for user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Process the task based on priority and time sensitivity using match-case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += " but can be done later today."
        case "medium":
            reminder = f"'{task}' is a medium priority task"
            if time_bound == "yes":
                reminder += " that should be done soon."
            else:
                reminder += " and can be done when possible."
        case "low":
            reminder = f"'{task}' is a low priority task"
            if time_bound == "yes":
                reminder += " but can be postponed until later."
            else:
                reminder += " and should be completed when you have free time."

        case _:
            reminder = "Invalid priority level entered."

    # Step 3: Provide the customized reminder
    print(reminder)

if __name__ == "__main__":
    main()
