import statistics

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_1 = [float(statistics.mean(grades[0])), (statistics.mean(grades[1])),
            float(statistics.mean(grades[2])), (statistics.mean(grades[3])),
            # почему то не выдавал дробное значение для grades[2]...
            (statistics.mean(grades[4]))]
students_1 = list(sorted(students))
evaluation = dict(zip(students_1, grades_1))
print(evaluation)
