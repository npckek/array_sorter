import random

# Функция для ввода массива с клавиатуры
def input_custom_array():
    while True:
        try:
            arr = input("Введите элементы массива через пробел: ").split()
            return [int(num) for num in arr]
        except:
            print("Некорректный ввод. Введите число.")
            continue

# # Функция для генерации случайного массива чисел
def generate_random_array(size, min_value=-100 , max_value=100 ):
    return [random.randint(min_value, max_value) for _ in range(size)]

# Функция сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Функция вызова вопросов
def get_user_array(): 
    array_choice = input("Хотите ввести массив вручную? (y/n): ")
    original_array = []
    if array_choice.lower() == "y":
        original_array = input_custom_array()
    else:
        size_choice = input("Хотите выбрать размер массива вручную? (y/n): ")
        if size_choice.lower() == "y":
            while True:
                try: 
                    size = int((input("Выберите размер массива от 2 до 30: ")))
                except ValueError: 
                    print("Некорректный ввод. Введите число.")
                    continue

                if 2 <= size <= 30 :
                    original_array = generate_random_array(size)
                    break
                else:
                    print("Размер массива некорректен. Выберите из доступных вариантов.")
        else :
            original_array = generate_random_array(random.randint(2, 30))
    return original_array

# Основная функция программы
def main():
    while True:
        # Генерация исходного массива
        original_array = get_user_array()

        # Вывод исходного массива
        print("Исходный массив: ", original_array)

        # Сортировка
        bubble_sort(original_array)

        # Вывод отсортированного массива
        print("Отсортированный массив: ", original_array)

        # Предложение повторить генерацию чисел
        repeat_generation = input("Хотите сгенерировать новый массив? (y/n): ")
        if repeat_generation.lower() != "y":
            break

# Вызов основной функции
if __name__ == "__main__":
    main()
