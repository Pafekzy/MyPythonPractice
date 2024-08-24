from datetime import datetime

birth_date = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
today = datetime.today()
age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print(f"Age: {age_years} years")


#Calculate Age from Birth Date