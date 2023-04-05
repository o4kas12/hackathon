def determinant(matrix):
    """
    Функция для вычисления определителя матрицы.
    :param matrix: матрица (список списков)
    :return: определитель матрицы (число)
    """
    # проверяем, что матрица является квадратной
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Матрица должна быть квадратной.")

    # базовый случай: матрица 1x1
    if n == 1:
        return matrix[0][0]

    # базовый случай: матрица 2x2
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # рекурсивный случай: матрица n x n
    det = 0
    for j in range(n):
        sign = (-1) ** j
        minor = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += sign * matrix[0][j] * determinant(minor)

    return det

def input_matrix():
    """
    Функция для ввода матрицы.
    :return: матрица (список списков)
    """
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Введите элемент [{i+1}, {j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix



# основная часть программы
while True:
    print("Выберите операцию:")
    print("1. Умножение матриц")
    print("2. Деление матриц")
    print("3. Сложение матриц")
    print("4. Вычитание матриц")
    print("5. Транспонирование матрицы")
    print("6. Вычисление определителя")
    print("0. Выйти")

    choice = int(input("Ваш выбор: "))

    if choice == 0:
        break

    if choice == 1:
        # запрашиваем две матрицы у пользователя
        print("Введите первую матрицу:")
        matrix1 = input_matrix()

        print("Введите вторую матрицу:")
        matrix2 = input_matrix()

        # проверяем, можно ли умножить эти матрицы
        if len(matrix1[0]) != len(matrix2):
            print("Невозможно умножить эти матрицы.")
        else:
            # умножаем матрицы и выводим результат
            result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += matrix1[i][k] * matrix2[k][j]

            print("Результат умножения матриц:")
            for row in result:
                print(row)

    elif choice == 2:
        # запрашиваем две матрицы у пользователя
        print("Введите первую матрицу:")
        matrix1 = input_matrix()

        print("Введите вторую матрицу:")
        matrix2 = input_matrix()

        # проверяем, можно ли разделить эти матрицы
        if len(matrix2) != len(matrix2[0]) or len(matrix1) != len(matrix2[0]):
            print("Невозможно разделить эти матрицы.")
        else:
            # находим обратную матрицу второй матрицы
            det = determinant(matrix2)
            if det == 0:
                print("Вторая матрица вырожденная, невозможно разделить.")
            else:
                inverse_matrix = matrix2

                # умножаем первую матрицу на обратную матрицу второй
                result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i][j] += matrix1[i][k] * inverse_matrix[k][j]

                print("Результат деления матриц:")
                for row in result:
                    print(row)


    elif choice == 3:
        # запрашиваем две матрицы у пользователя
        print("Введите первую матрицу:")
        matrix1 = input_matrix()

        print("Введите вторую матрицу:")
        matrix2 = input_matrix()

        # проверяем, можно ли сложить эти матрицы
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            print("Невозможно сложить эти матрицы.")
        else:
            # складываем матрицы поэлементно
            result = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    result[i][j] = matrix1[i][j] + matrix2[i][j]

            print("Результат сложения матриц:")
            for row in result:
                print(row)

    elif choice == 4:
        # запрашиваем две матрицы у пользователя
        print("Введите первую матрицу:")
        matrix1 = input_matrix()

        print("Введите вторую матрицу:")
        matrix2 = input_matrix()

        # проверяем, можно ли вычесть эти матрицы
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            print("Невозможно вычесть эти матрицы.")
        else:
            # вычитаем матрицы поэлементно
            result = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    result[i][j] = matrix1[i][j] - matrix2[i][j]

            print("Результат вычитания матриц:")
            for row in result:
                print(row)

    elif choice == 5:
        # запрашиваем матрицу у пользователя
        print("Введите матрицу:")
        matrix = input_matrix()

        # транспонируем матрицу
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        print("Результат транспонирования матрицы:")
        for row in result:
            print(row)

    elif choice == 6:
        # запрашиваем матрицу у пользователя
        print("Введите матрицу:")
        matrix = input_matrix()

        # проверяем, что матрица является квадратной
        if len(matrix) != len(matrix[0]):
            print("Определитель может быть вычислен только для квадратной матрицы.")
        else:
            # вычисляем определитель матрицы
            det = determinant(matrix)
            print(f"Определитель матрицы: {det}")
