import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)
    balls={}
    for student in students:
        balls[student["name"]] = student["grade"]
best_name = max(balls, key=balls.get)        
best = {"name": best_name,"grade": balls[best_name]}

worst_name = min(balls, key=balls.get)        
worst = {"name": worst_name,"grade": balls[worst_name]}

average=sum(balls.values()) / len(balls)

print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")