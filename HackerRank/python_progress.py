from pathlib import Path
from datetime import datetime, timedelta

path = Path("./Python")
module_num = len(list(path.glob("*.py")))

print(f"You have solved {module_num} problems on HackerRank/Python.")
print(f"{115-module_num} problems left.\n")

days = int((115-module_num)/3)
print(f"If you keep solving 3 problems per day, {days} days have left.")

current_date = datetime.now()
delta = timedelta(days = days)
finish_date = current_date + delta

print(f"It will be finished by {finish_date:%d %B %Y}")