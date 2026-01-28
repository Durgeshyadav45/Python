import sqlite3
import os
import getpass
from datetime import datetime


class CoffeeApp:
    def __init__(self):
        self.menu = {
            "Espresso": 2.00,
            "Piccolo Latte": 3.50,
            "Cappuccino": 4.00,
            "Latte": 2.50,
            "Breve": 2.70,
            "Americano": 6.00
        }

        # 🔐 Owner password
        self.owner_password = "admin123"

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(BASE_DIR, "coffee.db")

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        self.create_tables()

    # ---------- Create DB Table ----------
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT,
                price REAL,
                quantity INTEGER,
                total REAL,
                date TEXT
            )
        """)
        self.conn.commit()

    # ---------- Show Menu ----------
    def show_menu(self):
        print("\n------ Coffee Menu ------")
        for coffee, price in self.menu.items():
            print(f"{coffee:15} : ${price}")

    # ---------- Take Order ----------
    def take_order(self):
        self.show_menu()
        choice = input("Enter coffee name: ")

        if choice not in self.menu:
            print(" Coffee not available!")
            return

        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print(" Invalid quantity!")
            return

        price = self.menu[choice]
        total = price * qty

        self.save_order(choice, price, qty, total)

        print(f"✅ {qty} {choice}(s) served!")

    # ---------- Save Order ----------
    def save_order(self, item, price, qty, total):
        self.cursor.execute("""
            INSERT INTO orders (item, price, quantity, total, date)
            VALUES (?, ?, ?, ?, ?)
        """, (
            item,
            price,
            qty,
            total,
            datetime.now().strftime("%Y-%m-%d %H:%M")
        ))
        self.conn.commit()

    # ---------- Print Receipt ----------
    def print_receipt(self):
        self.cursor.execute("""
            SELECT item, price, quantity, total, date
            FROM orders
            ORDER BY id DESC
            LIMIT 1
        """)
        order = self.cursor.fetchone()

        if not order:
            print(" No order found!")
            return

        item, price, qty, total, date = order

        print("\n====== COFFEE RECEIPT ======")
        print(f"Date     : {date}")
        print(f"Item     : {item}")
        print(f"Quantity : {qty}")
        print(f"Unit     : ${price}")
        print(f"Total    : ${total}")
        print("--------------------------")
        print("Thank you ☕")

    # ---------- View Sales (OWNER ONLY) ----------
    def view_sales(self):
        password = getpass.getpass("Enter owner password: ")

        if password != self.owner_password:
            print(" Access denied! Owner only.")
            return

        self.cursor.execute("SELECT SUM(total) FROM orders")
        total_sales = self.cursor.fetchone()[0]
        total_sales = total_sales if total_sales else 0

        print(f"\n💰 Total Sales : ${total_sales}")

    # ---------- Main Menu ----------
    def run(self):
        while True:
            print("\n===== Coffee App Menu =====")
            print("1. Show Menu")
            print("2. Order Coffee")
            print("3. Print Receipt")
            print("4. View Sales (Owner)")
            print("5. Exit")

            option = input("Choose option: ")

            if option == "1":
                self.show_menu()
            elif option == "2":
                self.take_order()
            elif option == "3":
                self.print_receipt()
            elif option == "4":
                self.view_sales()
            elif option == "5":
                print("👋 Goodbye!")
                break
            else:
                print(" Invalid option!")


# ---------- Start App ----------
app = CoffeeApp()
app.run()
