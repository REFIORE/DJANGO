import random
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def monday(request):
    monday_tasks = ["Сделать зарядку", "Выпить кофе", "Начать работу",]
    todo_list = monday_tasks.copy()
    random.shuffle(todo_list)
    return render(request, 'monday.html',
                  {'day_name': 'Понедельник', 'todo_list': todo_list})


def tuesday(request):
    tuesday_tasks = ["Провести встречу", "Написать отчет", "Почитать книгу",]
    todo_list = tuesday_tasks.copy()
    random.shuffle(todo_list)
    return render(request, 'tuesday.html',
                  {'day_name': 'Вторник', 'todo_list': todo_list})


def wednesday(request):
    wednesday_tasks = ["Сходить в спортзал", "Купить продукты", "Помыть посуду",]
    todo_list = wednesday_tasks.copy()
    random.shuffle(todo_list)
    return render(request, 'wednesday.html',
                  {'day_name': 'Среда', 'todo_list': todo_list})


def thursday(request):
    thursday_tasks = ["Изучить Django", "Сделать домашнее задание", "Позвонить другу",]
    todo_list = thursday_tasks.copy()
    random.shuffle(todo_list)
    return render(request, 'thursday.html',
                  {'day_name': 'Четверг', 'todo_list': todo_list})


def friday(request):
    friday_tasks = ["Закончить проект", "Убраться дома", "Посмотреть фильм",]
    todo_list = friday_tasks.copy()
    random.shuffle(todo_list)
    return render(request, 'friday.html',
                  {'day_name': 'Пятница', 'todo_list': todo_list})


def saturday(request):
    saturday_tasks = ["Отдохнуть", "Погулять в парке", "Приготовить ужин",]
    todo_list = saturday_tasks.copy()
    random.shuffle(todo_list)
    return render(request, 'saturday.html',
                  {'day_name': 'Суббота', 'todo_list': todo_list})


def sunday(request):
    sunday_tasks = ["Планирование недели", "Йога", "Ранний сон",]
    todo_list = sunday_tasks.copy()
    random.shuffle(todo_list)
    return render(request, 'sunday.html',
                  {'day_name': 'Воскресенье', 'todo_list': todo_list})
