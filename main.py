# https://github.com/asalnorouzzade/Practice-38-Student-Grade-Analysis-and-Report-Generation.git
import csv
students = []

with open("students.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        name = row[0]
        score = float(row[1])
        students.append({"name": name, "score": score})
        
total_score = sum(s["score"] for s in students)
average_score = total_score / len(students)
highest_score = max(s["score"] for s in students)
lowest_score = min(s["score"] for s in students)
highest_student = next(s["name"] for s in students if s["score"] == highest_score)
lowest_student = next(s["name"] for s in students if s["score"] == lowest_score)
failed_students = [s for s in students if s["score"] < 12]
top_students = [s for s in students if s["score"] > 17]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

def save_csv(filename, data):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "score"])
        for s in data:
            writer.writerow([s["name"], s["score"]])
            
save_csv("failed_students.csv", failed_students)
save_csv("top_students.csv", top_students)
save_csv("sorted_students.csv", sorted_students)

print("Failed Students:")
for s in failed_students:
    print(f"{s['name']}, {s['score']:.1f}")
print("Top Students:")
for s in top_students:
    print(f"{s['name']}, {s['score']:.1f}")
print("========== Class Report ==========")
print(f"Total Students: {len(students)}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_student}, {highest_score}")
print(f"Lowest Score: {lowest_student}, {lowest_score}")
print(f"Number of Failed Students: {len(failed_students)}")
print(f"Number of Top Students: {len(top_students)}")
