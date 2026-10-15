# TutorTrack GradeBook - Final Project (Day 9)
# Concepts used: Variables, Operators, If/Elif/Else, Loops, Functions,
# Nested Dictionaries, String Methods, File Handling, Try/Except (Days 1-8).

from typing import Dict, List, Tuple

DATA_FILE = "gradebook.txt"


def load_gradebook() -> Dict[str, Dict[str, float]]:
    """Reads gradebook data from file into a nested dictionary structure.

    Returns a mapping of student name -> (mapping of subject -> score).
    """
    gradebook: Dict[str, Dict[str, float]] = {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                parts = cleaned_line.split("|")
                if len(parts) == 3:
                    student, subject, score_str = parts[0], parts[1], parts[2]
                    try:
                        score = float(score_str)
                        if student not in gradebook:
                            gradebook[student] = {}
                        gradebook[student][subject] = score
                    except ValueError:
                        continue
    except FileNotFoundError:
        # File will be created automatically upon saving
        pass
    return gradebook


def save_gradebook(gradebook: Dict[str, Dict[str, float]]) -> None:
    """Saves the current gradebook dictionary to a text file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            for student, subjects in gradebook.items():
                for subject, score in subjects.items():
                    file.write(f"{student}|{subject}|{score}\n")
        print("[✓] All records successfully saved to file.")
    except Exception as e:
        print(f"[X] Error saving data: {e}")


def add_student_or_score(gradebook: Dict[str, Dict[str, float]]) -> None:
    """Adds a new student score or updates an existing subject score."""
    print("\n--- RECORD / UPDATE STUDENT SCORE ---")
    student = input("Enter student name: ").strip().title()
    if not student:
        print("[!] Student name cannot be empty.")
        return

    subject = input("Enter subject name: ").strip().title()
    if not subject:
        print("[!] Subject name cannot be empty.")
        return

    try:
        score_input = float(input(f"Enter score for {student} in {subject} (0-100): "))
        if score_input < 0 or score_input > 100:
            print("[!] Score must be between 0 and 100.")
            return
    except ValueError:
        print("[!] Invalid input. Please enter a numerical score.")
        return

    if student not in gradebook:
        gradebook[student] = {}

    gradebook[student][subject] = score_input
    print(f"[✓] Recorded: {student} -> {subject}: {score_input:.1f}")
    save_gradebook(gradebook)


def view_student_summaries(gradebook: Dict[str, Dict[str, float]]) -> None:
    """Displays each student's subject breakdown and overall average."""
    print("=========================================")
    print("        STUDENT GRADE SUMMARIES          ")
    print("=========================================")

    if not gradebook:
        print("No student records found.")
        return

    for student, subjects in gradebook.items():
        print(f"\nStudent: {student}")
        print("-" * 35)
        
        if not subjects:
            print("  No subjects recorded.")
            continue

        total_score = 0.0
        for subject, score in subjects.items():
            print(f"  • {subject:<15}: {score:>5.1f}")
            total_score += score

        count = len(subjects)
        average = total_score / count
        print("-" * 35)
        print(f"  Overall Average : {average:.2f}%")


def view_subject_analytics(gradebook: Dict[str, Dict[str, float]]) -> None:
    """Calculates class average per subject and identifies top performers."""
    print("=========================================")
    print("    SUBJECT ANALYTICS & TOP PERFORMERS   ")
    print("=========================================")

    if not gradebook:
        print("No student records found.")
        return

    # Collect all scores grouped by subject
    subject_map: Dict[str, List[Tuple[str, float]]] = {}
    for student, subjects in gradebook.items():
        for subject, score in subjects.items():
            if subject not in subject_map:
                subject_map[subject] = []
            subject_map[subject].append((student, score))

    if not subject_map:
        print("No subject data available.")
        return

    for subject, entries in subject_map.items():
        total = sum(score for _, score in entries)
        class_avg = total / len(entries)

        # Identify top performer(s) in this subject
        top_student = None
        highest_score = -1.0
        for student, score in entries:
            if score > highest_score:
                highest_score = score
                top_student = student

        print(f"Subject: {subject}")
        print(f" • Enrolled Students : {len(entries)}")
        print(f" • Class Average     : {class_avg:.2f}%")
        print(f" Top Performer    : {top_student} ({highest_score:.1f}%)")
        print("-" * 40)


def main():
    gradebook = load_gradebook()

    while True:
        print("=========================================")
        print("    TUTORTRACK MULTI-STUDENT GRADEBOOK   ")
        print("=========================================")
        print("1. Record / Update Student Score")
        print("2. View Student Grade Summaries")
        print("3. View Subject Analytics & Top Performers")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            add_student_or_score(gradebook)
        elif choice == "2":
            view_student_summaries(gradebook)
        elif choice == "3":
            view_subject_analytics(gradebook)
        elif choice == "4":
            print("Thank you for using TutorTrack GradeBook. Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()

