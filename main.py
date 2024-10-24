from __future__ import print_function
from mysql.connector import connect, Error
from datetime import datetime

'''TABLES['transactions'] = (
                                "CREATE TABLE `transactions` ("
                                "  `purchase` int(11) NOT NULL "
                                "  `date_of_transaction` date NOT NULL,"
                                "  `name` varchar(14) NOT NULL,"
                                ") ENGINE=InnoDB")

                            cursor.execute(TABLES['transactions'])
                            connection.commit()
                            print('Таблица загружена!')'''

class backend:
    def __init__(self):
        self.connection = None
        self.new_purchase_data = None
        self.con_with_base()

    def con_with_base(self):
        try:
            self.connection = connect(
                host="localhost",
                user="root",
                password="1D6)aTM/089",
                database="costs",
                port=3307
            )
            if self.connection.is_connected():
                print("Соединение с базой данных установлено")
        except Error as e:
            print(f"Ошибка подключения: {e}")

    def close_connection(self):
        """Закрывает соединение с базой данных."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Соединение с базой данных закрыто")

    def new_purchase(self, price, name):
        """Получает данные о новой покупке от пользователя."""
        try:
            self.new_purchase_data = (int(price), datetime.date(datetime.now()), name)
            print("Данные новой покупки сохранены.")
            return self.new_purchase_data
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректные данные.")
            return None

    def insert_purchase_when1(self):
        if self.new_purchase_data is None:
            print("Нет данных для новой покупки.")
            return

        try:
            with self.connection.cursor() as cursor:
                insert_query = (
                    "INSERT INTO transactions (purchase, date_of_transaction, name) "
                    "VALUES (%s, _, %s)"
                )
                cursor.execute(insert_query, self.new_purchase_data)
                self.connection.commit()
                print("Новая покупка успешно добавлена в базу данных.")
        except Error as e:
            print(e)

    def insert_purchase_when0(self):
        if self.new_purchase_data is None:
            print("Нет данных для новой покупки.")
            return

        try:
            with self.connection.cursor() as cursor:
                insert_query = (
                    "INSERT INTO transactions (purchase, date_of_transaction, name) "
                    "VALUES (%s, %s, %s)"
                )
                cursor.execute(insert_query, self.new_purchase_data)
                self.connection.commit()
                print("Новая покупка успешно добавлена в базу данных.")
        except Error as e:
            print(e)

    def check_today_purchases(self):
        """Проверяет, есть ли покупки за сегодняшний день."""
        try:
            connection = self.connection
            if connection:
                with self.connection.cursor() as cursor:
                    today_date = datetime.now().strftime('%Y-%m-%d')
                    check_query = "SELECT * FROM transactions WHERE date_of_transaction = %s"
                    cursor.execute(check_query, (today_date,))
                    results = cursor.fetchall()


                    if results:
                        return results
                    else:
                        return False
        except Error as e:
            print(f"Ошибка при проверке покупок: {e}")

    def serching(self, req):
        try:
            nowday = datetime.now().strftime('%Y-%m-%d')
            connection = self.connection
            if connection:
                with self.connection.cursor() as cursor:
                    chek = "SELECT `purchase` FROM transactions WHERE `name` = %s AND date_of_transaction = %s;"
                    cursor.execute(chek, (req, nowday))
                    results = cursor.fetchall()

                    if results:
                        return results
                    else:
                        return False
        except Error as e:
            print(f'error in base: {e}')

    def registration_logging(self, username, password, telephone_number, email=None):
        pass

    def checking_purchases_from_date_to_date(self, date1=datetime.now().strftime('%Y-%m-%d'), date2=datetime.now().strftime('%Y-%m-%d')):
        connection = self.connection
        if connection:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT * 
                    FROM transactions 
                    WHERE date_of_transaction BETWEEN %s AND %s;
                    """
                cursor.execute(query, (date1, date2))
                results = cursor.fetchall()
            return results


'''Backend = backend()
Backend.new_purchase(12, 'хлеб')  # Сначала вводим новую покупку
Backend.insert_purchase_when0()  # Затем сохраняем её в базе данных
print(Backend.check_today_purchases())  # Проверяем покупки за сегодняшний день
Backend.close_connection()'''


