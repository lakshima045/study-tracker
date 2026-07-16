study_log = [
    {"subject": "Math", "hours": 2},
    {"subject": "Science", "hours": 1.5},
    {"subject": "English", "hours": 1},
]

def total_hours(log):
    return sum(entry["hours"] for entry in log)

def hours_by_subject(log):
    summary = {}
    for entry in log:
        summary[entry["subject"]] = summary.get(entry["subject"], 0) + entry["hours"]
    return summary

if __name__ == "__main__":
    print("Total hours studied:", total_hours(study_log))
    print("Breakdown by subject:")
    for subject, hours in hours_by_subject(study_log).items():
        print(f"  {subject}: {hours} hrs")
