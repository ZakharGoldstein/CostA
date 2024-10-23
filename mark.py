import flet as ft
from main import backend

Backend = backend()

def main(page: ft.Page):
    tasks = {}  # Словарь для хранения задач и их счетчиков

    # Настройка страницы
    #page.bgcolor = "purple"   Фон страницы (для контраста с белым текстом)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Центрирование по горизонтали
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    # Центрирование по вертикали

    # Функция добавления задачи
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

    # Функция показа счетчика для задачи
    def show_count_clicked(e):
        answ = Backend.serching(task_to_show.value)
        if answ:
            count = answ
            all_answ = "\n".join([f"{i[0]}" for i in count])
            page.add(ft.Text(f"Счетчик для \n{all_answ}", color='white', size=24, text_align=ft.TextAlign.CENTER))
        else:
            page.add(ft.Text("Задача не найдена.", color='white', size=24, text_align=ft.TextAlign.CENTER))

    # Функция показа всех задач
    def show_all_clicked(e):
        chek = Backend.check_today_purchases()
        if chek:
            all_tasks = "\n".join([f"{count}: {task}" for task, date, count in chek])
            page.add(ft.Text(value=f"Все покупки:\n{all_tasks}", color='white', size=24, text_align=ft.TextAlign.CENTER))
        else:
            page.add(ft.Text("Нет покупок", color='white', size=24, text_align=ft.TextAlign.CENTER))

    # Поля ввода и кнопки
    new_task = ft.TextField(hint_text="ПОкупОчка", width=300)
    new_count = ft.TextField(hint_text="Цена", width=100)
    task_to_show = ft.TextField(hint_text="Введите задачу для показа счетчика", width=300)

    # Главная колонка для всех элементов
    page.add(
        ft.Column(
            [
                ft.Row([new_task, new_count, ft.ElevatedButton("Добавить", on_click=add_clicked)], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([task_to_show, ft.ElevatedButton("Показать счетчик", on_click=show_count_clicked)], alignment=ft.MainAxisAlignment.CENTER),
                ft.ElevatedButton("Показать покупки", on_click=show_all_clicked),
            ],
            alignment=ft.MainAxisAlignment.START,  # Центрирование содержимого по вертикали
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Центрирование по горизонтали
        )
    )

# Запуск приложения
try:
    ft.app(target=main)
except:
    print("ошибочка")
finally:
    Backend.close_connection()



'''def check_today_purchases(self):
    """Проверяет, есть ли покупки за сегодняшний день."""
    try:
        connection = self.con_with_base()
        if connection:
            with self.connection.cursor() as cursor:
                today_date = datetime.now().strftime('%Y-%m-%d')
                check_query = "SELECT * FROM transactions WHERE date_of_transaction = %s"
                cursor.execute(check_query, (today_date,))
                results = cursor.fetchall()

                if results:
                    print(f"Найдены покупки за сегодня ({today_date}):")
                    for row in results:
                        print(row)
                else:
                    print("За сегодня покупок не найдено.")
    except Error as e:
        print(f"Ошибка при проверке покупок: {e}")'''