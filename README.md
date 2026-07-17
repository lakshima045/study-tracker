# study-tracker
Track my study sessions and progress by subject

## Subjects
   - Math
   - Science
   - English

## How it works

This tool tracks study sessions by subject and shows a summary of total hours studied.

Data is stored in `study_log.json`. Each entry looks like:
{"subject": "Math", "hours": 2}

## Running it

python calculate_hours.py

You'll see a menu:
1. Add a study session
2. Show summary
3. Exit

**Example output:**
Total hours studied: 4.5
Breakdown by subject:
  Math: 2 hrs
  Science: 1.5 hrs
  English: 1 hrs
  
 ## Notes
   Tracking consistently helps spot which subjects need more time.
