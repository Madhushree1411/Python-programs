file = open("notes.txt", "w")
file.write("Hello Python")
file.close()

marks = [90, 70, 95, 60]
marks.sort()
print(marks)

students = {
    "Arun": 90,
    "Priya": 95,
    "Kavin": 88
}

print(students)

if "Arun" in students:
    print("Found") 
