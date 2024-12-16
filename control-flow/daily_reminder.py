def main():
    # Step 1: Prompt the user for task, priority, and time-bound info
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Process the task based on priority and time sensitivity
    match priority:
        case "high":
            priority_msg = "high priority"
        case "medium":
            priority_msg = "medium priority"
        case "low":
            priority_msg = "low priority"
        case _:
            priority_msg = "unknown priority"

    # Step 3: Check if the task is time-bound
    if time_bound == "yes":
        time_msg = "that requires immediate attention today!"
    else:
        time_msg = "You can consider completing it when you have free time."

    # Step 4: Print the customized reminder
    print(f"Reminder: '{task}' is a {priority_msg} task {time_msg}")

# Run the main function
if __name__ == "__main__":
    main()
