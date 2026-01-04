def add_student(students_list):
    name = input("Enter full name: ").title()
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")
    
    fav_subjects = input("Enter 3 favorite subjects (comma-separated): ").split(',')
    fav_subjects = [s.strip() for s in fav_subjects]
    
    marks_dict = {}
    for sub in fav_subjects:
        while True:
            try:
                score = float(input(f"Enter marks of {sub}: "))
                if 0 <= score <= 100:
                    marks_dict[sub] = score
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                
    skills_input = input("Enter technical skills (comma-separated): ").split(',')
    skills_set = {s.strip() for s in skills_input if s.strip()}
    
    student = {
        "name": name,
        "roll": roll,
        "branch": branch,
        "subjects": sorted(fav_subjects),
        "marks": marks_dict,
        "skills": list(skills_set)
    }
    
    students_list.append(student)
    print(f"\n{name} added successfully!")

def view_all_students(students_list):
    if not students_list:
        print("\nNo student records found.")
        return

    print("\n--- All Students ---")
    for s in students_list:
        total = sum(s['marks'].values())
        avg = total / len(s['marks']) if s['marks'] else 0
        highest_sub = max(s['marks'], key=s['marks'].get) if s['marks'] else "N/A"
        
        print(f"\nName: {s['name']}")
        print(f"Roll & Branch: {s['roll']}, {s['branch']}")
        print(f"Favorite Subjects (sorted): {s['subjects']}")
        print(f"Marks: {s['marks']}")
        print(f"Total Marks: {total}, Average: {avg:.2f}")
        print(f"Highest Scoring Subject: {highest_sub}")
        print(f"Technical Skills: {s['skills']}")

def run_analytics(students_list):
    if not students_list:
        print("\nNo data available for analytics.")
        return

    print("\n--- Top Students by Total Marks ---")
    ranked = sorted(students_list, key=lambda x: sum(x['marks'].values()), reverse=True)
    for i, s in enumerate(ranked, 1):
        print(f"{i}. {s['name']} - Total Marks: {sum(s['marks'].values())}")

    print("\n--- Subject-wise Toppers ---")
    all_subjects = set()
    for s in students_list:
        all_subjects.update(s['marks'].keys())
    
    for sub in all_subjects:
        topper = None
        max_score = -1
        for s in students_list:
            if sub in s['marks'] and s['marks'][sub] > max_score:
                max_score = s['marks'][sub]
                topper = s['name']
        if topper:
            print(f"{sub}: {topper} ({max_score} marks)")

    print("\n--- Most Common Technical Skills ---")
    skill_counts = {}
    for s in students_list:
        for skill in s['skills']:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1
    
    for skill, count in sorted(skill_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{skill}: {count} student(s)")

def main():
    students = []
    while True:
        print("\nStudent Performance Tracker")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Analytics")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            run_analytics(students)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()