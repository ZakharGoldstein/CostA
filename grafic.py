import flet as ft
from main import backend




Backend = backend()

def main(page):
    tasks = {}  # Словарь для хранения задач и их счетчиков

    def add_clicked(e):
        if new_task.value and new_count.value.isdecimal():
            task_name = new_task.value.lower()
            task_count = int(new_count.value)
            tasks[task_name] = task_count  # Добавляем задачу в словарь
            Backend.new_purchase(task_count, task_name)
            Backend.insert_purchase_when0()
            new_task.value = ""
            new_count.value = ""
            new_task.focus()
            new_task.update()
            new_count.update()

    def show_count_clicked(e):
        answ = Backend.serching(task_to_show.value)
        print(task_to_show.value)
        if answ:
            count = answ
            all_answ = "\n".join([f"{i[0]}" for i in count])
            page.add(ft.Text(f"Счетчик для \n{all_answ}", color='white', size=24))
        else:
            page.add(ft.Text("Задача не найдена.", color='white', size=24))

    def show_all_clicked(e):
        chek = Backend.check_today_purchases()

        if chek:
            all_tasks = "\n".join([f"{count}: {task}" for task, date, count in chek])
            page.add(ft.Text(value=f"Все покупки:\n{all_tasks}", color='white', size=24))

        else:
            page.add(ft.Text("Нет покупок", color='white', size=24))

    new_task = ft.TextField(hint_text="ПОкупОчка", width=300)
    new_count = ft.TextField(hint_text="Цена", width=100)
    task_to_show = ft.TextField(hint_text="Введите задачу для показа счетчика", width=300)

    page.add(ft.Row([new_task, new_count, ft.ElevatedButton("Добавить", on_click=add_clicked)]))
    page.add(ft.Row([task_to_show, ft.ElevatedButton("Показать счетчик", on_click=show_count_clicked)]))
    page.add(ft.ElevatedButton("Показать покупки", on_click=show_all_clicked))

    page.theme = ft.theme.Theme(color_scheme_seed="yellow")
    page.update()
try:
    ft.app(main)
except:
    print("ошибочка")
finally:
    Backend.close_connection()