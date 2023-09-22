import tkinter as tk

# Переменные для хранения размеров последнего удаленного прямоугольника
last_deleted_hx = None
last_deleted_hy = None

def validate_input(input_num, error_label):
    if input_num == "":
        error_label.config(text="")
        return True
    try:
        # Преобразуем строку в число и сохраняем в переменную value
        value = int(input_num)
        if value > 0:  # Проверяем, является ли число положительным
            error_label.config(text="")  # Очищаем метку с ошибкой и возвращаем true
            return True
        else:
            # Выводим сообщение об ошибке и возвращаем false
            error_label.config(text="Введите целое положительное число больше 0")
            return False
    except ValueError:
        # Если происходит ошибка преобразования строки в число, выводим сообщение об ошибке и возвращаем false
        error_label.config(text="Введите числовое значение")
        return False

def validate_input_wrapper(P):
    return validate_input(P, error_label)

def can_draw_rectangle(x, y):
    min_size = 0  # Минимальный размер прямоугольника
    # Проверка размерности сторон x и y на минимальные допустимые значения
    if min_size < x and min_size < y:
        return True
    else:
        return False

def draw_rectangle():
    global x, y, canvas, rectangles, hx_increment, hy_increment, last_deleted_hx, last_deleted_hy
    # Инициализация значений x и y
    # размер первого прямоугольника всегда один и тот же
    if x is None:
        x = width_canvas - 10
    if y is None:
        y = height_canvas - 10
    # Если введенные значения hx и hy еще не были использованы, сохраняем их
    if hx_increment is None:
        hx_increment = int(hx_entry.get())
    if hy_increment is None:
        hy_increment = int(hy_entry.get())
    # Очищаем текстовые поля
    hx_entry.delete(0, tk.END)
    hy_entry.delete(0, tk.END)
    # Запрещаем редактирование текстовых полей
    hx_entry.config(state=tk.DISABLED)
    hy_entry.config(state=tk.DISABLED)
    # Если есть сохраненные размеры последнего удаленного прямоугольника, используем их
    if last_deleted_hx is not None and last_deleted_hy is not None:
        x = last_deleted_hx
        y = last_deleted_hy
        last_deleted_hx = None
        last_deleted_hy = None
    if can_draw_rectangle(x, y):
        # Отрисовываем прямоугольник с текущими значениями x и y
        x1 = (width_canvas - x) / 2
        y1 = (height_canvas - y) / 2
        x2 = x1 + x
        y2 = y1 + y
        rectangle = canvas.create_rectangle(x1, y1, x2, y2)
        # Добавляем прямоугольник в список rectangles
        rectangles.append(rectangle)
        # Уменьшаем значения x и y на заданный шаг
        x -= hx_increment
        y -= hy_increment
    else:
        error_label.config(text="Прямоугольник еще меньше построить уже нельзя")

def delete_rectangle():
    global canvas, rectangles, last_deleted_hx, last_deleted_hy
    if len(rectangles) > 0:
        # Получаем ID последнего нарисованного прямоугольника
        last_rectangle = rectangles[-1]
        # Получаем и сохранеям размеры последнего удаленного прямоугольника
        x1, y1, x2, y2 = canvas.coords(last_rectangle)
        last_deleted_hx = x2 - x1
        last_deleted_hy = y2 - y1
        # Проверяем, нужно ли скрыть предупреждение
        if can_draw_rectangle(last_deleted_hx, last_deleted_hy):
            error_label.config(text="")
        # Удаляем прямоугольник из холста и из списка rectangles
        canvas.delete(last_rectangle)
        rectangles.pop()

def on_key_press(event):
    if event.keysym == "Return":
        # Если нажата клавиша Enter, отрисовываем прямоугольник
        draw_rectangle()
    elif event.keysym == "d":
        # Если нажата клавиша 'd', удаляем последний прямоугольник
        delete_rectangle()
    elif event.keysym == "Escape":
        # Если нажата клавиша Esc, закрываем окно
        root.destroy()

if __name__ == "__main__":
    # Создаем окно приложения
    root = tk.Tk()
    root.title("Лабораторная работа 1 вариант 7")
    width_canvas = 600
    height_canvas = 600
    # Создаем холст
    canvas = tk.Canvas(root, width=width_canvas, height=height_canvas)
    canvas.pack(side=tk.LEFT)
    # Создаем метку и текстовые поля для ввода шага hx и hy
    input_frame = tk.Frame(root)
    input_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    data_label = tk.Label(input_frame, text="Введите данные и нажмите enter для отрисовки")
    data_label.grid(row=0, columnspan=4, padx=5, pady=5)

    # Создаем метку для вывода ошибки и передаем ее в функцию validate_input
    error_label = tk.Label(input_frame, fg="red")
    error_label.grid(row=4, columnspan=2, padx=5, pady=5)

    # Добавляем валидацию к текстовому полю
    validate_input_cmd = root.register(validate_input_wrapper)
    hx_label = tk.Label(input_frame, text="Величина hx:")
    hx_label.grid(row=2, column=0, padx=5, pady=5)
    hx_entry = tk.Entry(input_frame, validate="key")
    hx_entry.config(validatecommand=(validate_input_cmd, "%P"))
    hx_entry.grid(row=2, column=1, padx=5, pady=5)
    hy_label = tk.Label(input_frame, text="Величина hy:")
    hy_label.grid(row=3, column=0, padx=5, pady=5)
    hy_entry = tk.Entry(input_frame, validate="key")
    hy_entry.config(validatecommand=(validate_input_cmd, "%P"))
    hy_entry.grid(row=3, column=1, padx=5, pady=5)

    # Создаем список для хранения прямоугольников
    rectangles = []
    # Переменные для хранения значений hx и hy
    x = None
    y = None
    # Переменные для хранения значений приращений hx и hy
    hx_increment = None
    hy_increment = None

    # Привязываем обработчик нажатия клавиш к окну
    root.bind("<Key>", on_key_press)

    # Запускаем главный цикл обработки событий
    root.mainloop()