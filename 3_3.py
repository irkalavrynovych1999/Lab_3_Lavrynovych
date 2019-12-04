with open('lessons.txt') as file:
    days = file.readlines()

different_lessons = []
lections_count = 0
labs_count = 0
prakt_count = 0

for day in days:
    lessons = day.split(' ')[1:]
    for lesson in lessons:
        lesson_name = lesson.split('(')[0]
        if lesson_name not in different_lessons:
            different_lessons.append(lesson_name)

        if lesson.endswith('\n'):
            lesson = lesson[:-1]
        lesson_type = lesson.split('(')[1][:-1]
        if lesson_type == 'практична':
            prakt_count += 1
        if lesson_type == 'лекція':
            lections_count += 1
        if lesson_type == 'лабораторна':
            labs_count += 1

print('Кількість предметів:', len(different_lessons))
print('Кількість практичних:', prakt_count)
print('Кількість лекцій:', lections_count)
print('Кількість лабораторних:', labs_count)