n = int(input())
student_birth = []
for _ in range(n):
    name, day, month, year = input().split()
    day, month, year = map(int,(day, month, year))
    student_birth.append((year, month, day, name))
student_birth.sort()
print(student_birth[-1][3])
print(student_birth[0][3])
