# Your Age Full details 



age = int(input('what\'s your age ').strip())
print(f"your age is : {age}")

months = age *12 
weaks = months*4
days = age *365
hours = days *24
minutes = hours*60
seconds = minutes*60

print(f" {months:,} months".strip()) 
print(f"{weaks:,} weaks".strip())
print(f"{days:,} days".strip())
print(f" {hours:,} hours".strip()) 
print(f" {minutes:,} minutes".strip())
print(f"{seconds:,} second".strip())
