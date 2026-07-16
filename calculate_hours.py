import json
import os

LOG_FILE = "study_log.json"

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

def total_hours(log):
    return sum(entry["hours"] for entry in log)

def hours_by_subject(log):
    summary = {}
    for entry in log:
        summary[entry["subject"]] = summary.get(entry["subject"], 0) + entry["hours"]
    return summary

def add_session(log):
    subject = input("Subject: ").strip()
    hours = float(input("Hours studied: ").strip())
    log.append({"subject": subject, "hours": hours})
    save_log(log)
    print(f"Added: {subject} - {hours} hrs\n")

def show_summary(log):
    print("Total hours studied:", total_hours(log))
    print("Breakdown by subject:")
    for subject, hours in hours_by_subject(log).items():
        print(f"  {subject}: {hours} hrs")

if __name__ == "__main__":
    log = load_log()
    while True:
        print("\n1. Add a study session")
        print("2. Show summary")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_session(log)
        elif choice == "2":
            show_summary(log)
        elif choice == "3":
            break
        else:
            print("Invalid option, try again.")
