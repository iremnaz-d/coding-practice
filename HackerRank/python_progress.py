from pathlib import Path

path = Path("./Python")
module_num = len(list(path.glob("*.py")))

print(f"You have solved {module_num} problems on HackerRank/Python.")
print(f"{115-module_num} problems left.\n")

print(f"If you keep solving 3 problems per day, {int((115-module_num)/3)} days have left.")
