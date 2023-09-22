import unittest
import tkinter as tk
from main import validate_input

class TestValidateInput(unittest.TestCase):

    def setUp(self):
        # Создаем окно Tkinter для тестирования
        self.root = tk.Tk()

    def tearDown(self):
        # Уничтожаем окно Tkinter после каждого теста
        self.root.destroy()

    def test_valid_positive_integer(self):
        # Тестирование ввода допустимого положительного целого числа
        input_num = "42"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertTrue(result)
        #error_label.cget("text") используется для получения текущего текста, который отображается на этой метке
        self.assertEqual(error_label.cget("text"), "")  # Проверка, что текст метки пуст

    def test_negative_integer(self):
        # Тестирование ввода отрицательного целого числа
        input_num = "-5"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Введите целое положительное число больше 0")

    def test_zero_input(self):
        # Тестирование ввода нуля
        input_num = "0"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Введите целое положительное число больше 0")

    def test_letters_input(self):
        # Тестирование ввода нечисловых данных
        input_num = "abc"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Введите числовое значение")
    def test_symbols_input(self):
        # Тестирование ввода нечисловых данных
        input_num = "@!&^%"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Введите числовое значение")

if __name__ == '__main__':
    unittest.main()