import flet as ft
from main import backend

Backend = backend()

def main(page):
    page.title = "Учет покупок"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.theme.Theme(color_scheme_seed="yellow")

    # Заголовок приложения
    page.add(ft.Text("Учет покупок", size=32, weight='bold', color='yellow'))

    # Создаем выпадающий список с категориями
    categories = ["Еда", "Одежда", "Техника", "Развлечения", "Другие"]
    category_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(category) for category in categories],
        hint_text="Выберите категорию",
        width=200,
        border_color='yellow',
        color='white'
    )

    new_count = ft.TextField(
        hint_text="Цена",
        width=150,
        border_color='yellow',
        color='black'
    )

    def add_clicked(e):
        if new_count.value.isdecimal() and category_dropdown.value:
            task_count = int(new_count.value)
            category = category_dropdown.value
            Backend.new_purchase(task_count, category)
            Backend.insert_purchase_when0()
            new_count.value = ""
            category_dropdown.value = None
            new_count.focus()
            new_count.update()
            category_dropdown.update()
            page.add(ft.Text("Покупка добавлена!", color='green', size=16))

    def show_count_clicked(e):
        answ = Backend.serching(category_dropdown.value)
        if answ:
            count = answ
            all_answ = "\n".join([f"{i[0]}" for i in count])
            page.add(ft.Text(f"Счетчик для категории '{category_dropdown.value}':\n{all_answ}", color='white', size=24))
        else:
            page.add(ft.Text("Категория не найдена.", color='red', size=24))

    def show_all_clicked(e):
        chek = Backend.checking_purchases_from_date_to_date()
        if chek:
            all_tasks = "\n".join([f"{count}: {task}" for task, date, count in chek])
            page.add(ft.Text(value=f"Все покупки:\n{all_tasks}", color='white', size=24))
        else:
            page.add(ft.Text("Нет покупок", color='red', size=24))

    # Объединяем элементы интерфейса
    page.add(ft.Row([
        category_dropdown,
        new_count,
        ft.ElevatedButton("Добавить", on_click=add_clicked, color='yellow', style=ft.ButtonStyle(elevation=5))
    ], alignment=ft.MainAxisAlignment.CENTER))

    page.add(ft.Row([
        ft.ElevatedButton("Показать счетчик", on_click=show_count_clicked, color='yellow', style=ft.ButtonStyle(elevation=5)),
        ft.ElevatedButton("Показать покупки", on_click=show_all_clicked, color='yellow', style=ft.ButtonStyle(elevation=5))
    ], alignment=ft.MainAxisAlignment.CENTER))

    page.update()

try:
    ft.app(main)
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    Backend.close_connection()