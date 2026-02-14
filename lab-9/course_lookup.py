n = int(input())

courses = {}

for _ in range(n):
    line = input().strip()
    parts = line.split()
    course_name = parts[0]
    course_code = parts[1]
    courses[course_name] = course_code

m = int(input())

for _ in range(m):
    query = input().strip()
    if query in courses:
        print(courses[query])
    else:
        print("Not Found")
