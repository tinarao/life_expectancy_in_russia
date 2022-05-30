from tkinter import *
from tkinter import messagebox

window = Tk()

COLOR=('#aaffaa')
BLACK=('#000000')

# отрисовка

window['bg'] = COLOR # цвет фона
window.title('Сколько мне осталось жить в России?') # название программы
window.geometry('500x300') # размер
window.resizable(width=False, height=False) # не менять размер

# функция подсчёта

def count():
    age_var=age.get()
    if age_var.isdigit():
        if int(age_var) <= 71:
            result = 71 - int(age_var)
            messagebox.showinfo(title=('Не так уж и много!'), message='Тебе осталось жить ' + str(result) + ' лет!')
        else:
            messagebox.showinfo(title='Врунишка!', message='Не ври!')
    else:
        messagebox.showinfo(title=('Неправильные данные!'), message='Введи число!')

# главный цикл

top_text = Label(window, text='Привет!\n Сколько тебе осталось жить в России?\n Давай посчитаем!\n Введи свой возраст:', bg=COLOR, fg=BLACK, font=('Consolas', 18))
top_text.place(x=0.8, y=0.5)

age = Entry(window, font=('Consolas'))
age.place(x=160, y=150)

button_count = Button(window, text='Сколько мне осталось?', command=count, font=('Consolas'))
button_count.place(x=150, y=180)

button_exit = Button(window, text='Выйти', command=window.destroy, font=('Consolas'))
button_exit.place(x=220, y=230)

# вечный цикл
window.mainloop() 