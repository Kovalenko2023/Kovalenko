"""
Задача №1 Знайти кількість відрізків b, розміщених на відрізку a,
і довжину незайнятої частини на відрізку a.
Користувачем вводиться довжина відрізка a, а потім довжина відрізка b на
окремих рядках. Відповідь виводиться в одному рядку: кількість відрізків b
і довжина незайнятої частини відрізка a.

Автор: Коваленко Катерина
"""

a = float(input("Яка довжина відрізка a?"))
b = float(input("Яка довжина відрізка b?"))


    
if b <= a:
    Кількість = a//b
    Незайнята = a%b
    print(f"Кількість відрізків b: {Кількість}, довжина незайнятої частини відрізка a: {Незайнята}")

else:
    print("Відрізок b не поміщується у відрізок a")


