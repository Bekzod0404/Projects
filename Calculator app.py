import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def clear():
    entry.delete(0, tk.END)


def operate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Kalkulyator")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=operate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val,
                                                                                                      column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()


# def qoshish(x, y):
#     return x + y
#
#
# def ayirish(x, y):
#     return x - y
#
# def kopaytrish(x, y):
#     return x * y
#
# def bolish(x, y):
#     if y == 0:
#         return '0 ga bolib bolmaydi'
#     return x / y
#
# while True:
#     print('Amallar')
#     print("'Qoshish' deb yozing qoshish uchun")
#     print("'Ayirish' deb yozing ayirish uchun")
#     print("'Kopaytirish' deb yozing kopaytirish uchun")
#     print("'Bolish' deb yozing bolish uchun")
#     print("'Quit' deb kiriting chiqish uchun")
#
#     user_input = input(": ")
#
#     if user_input == quit:
#         break
#     elif user_input in ['Qoshish', 'Ayirish', 'Kopaytrish', 'Bolish']:
#         son1 = float(input("1-chi sonni kiriting:"))
#         son2 = float(input("2-chi sonni kiriting:"))
#
#         if user_input == 'Qoshish':
#             print("Natija: ", qoshish(son1, son2))
#         elif user_input == 'Ayirish':
#             print("Natija: ", ayirish(son1, son2))
#         elif user_input == 'Kopaytirish':
#             print("Natija: ", kopaytrish(son1, son2))
#         elif user_input == 'Bolish':
#             print("Natija: ", bolish(son1, son2))
#         else:
#             print("Invalidmisan")
