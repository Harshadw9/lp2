def evaluate_employee():
    print("Welcome to the Employee Performance Evaluation System")
    name = input("Enter employee's name: ")

    print("\nRate the following parameters from 1 (Poor) to 5 (Excellent):")
    punctuality = int(input("1. Punctuality: "))
    task_completion = int(input("2. Task Completion: "))
    teamwork = int(input("3. Teamwork: "))
    communication = int(input("4. Communication Skills: "))

    total_score = punctuality + task_completion + teamwork + communication
    avg_score = total_score / 4

    print(f"\nEvaluation Report for {name}:")
    
    # Rule-based classification
    if avg_score >= 4.5:
        print("Rating: Outstanding")
        print("Recommendation: Promotion and bonus")
    elif avg_score >= 3.5:
        print("Rating: Very Good")
        print("Recommendation: Eligible for bonus")
    elif avg_score >= 2.5:
        print("Rating: Satisfactory")
        print("Recommendation: Improvement suggested")
    else:
        print("Rating: Needs Improvement")
        print("Recommendation: Performance improvement plan required")

# Run the system
evaluate_employee()
