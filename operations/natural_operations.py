from classes import *

class NaturalOperations:

    #N-1 Разработчик:Басик.В
    @staticmethod
    def COM_NN_D(num1: Natural, num2: Natural) -> int: #works
        """
        Сравнение двух натуральных чисел.
        Возвращает:
        - 2, если num1 > num2
        - 1, если num1 < num2
        - 0, если num1 == num2
        """
        # Сравниваем длины чисел
        if len(num1.digits) > len(num2.digits):
            return 2
        elif len(num1.digits) < len(num2.digits):
            return 1
        else:
            # Если длины равны, сравниваем цифры по порядку
            for i in range(len(num1.digits)):
                if num1.digits[i] > num2.digits[i]:
                    return 2
                elif num1.digits[i] < num2.digits[i]:
                    return 1
            return 0

    #N-2 Разработчик:Басик.В
    @staticmethod
    def NZER_N_B(num: Natural) -> str: #works
        """
        Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
        """
        if len(num.digits) == 1 and num.digits[0] == 0:
            return "нет"
        return "да"

    # N-3 Разработчик:Глебова.В
    @staticmethod
    def ADD_1N_N(num: Natural) -> Natural: #works
        """
        Добавление 1 к натуральному числу.
        """
        carry = 1
        result_digits = num.digits[::-1]  # переворачиваем, чтобы сложение было проще

        # Пытаемся добавить 1, начиная с младших разрядов
        for i in range(len(result_digits)):
            result_digits[i] += carry
            if result_digits[i] == 10:
                result_digits[i] = 0
                carry = 1
            else:
                carry = 0
                break

        if carry == 1:
            result_digits.append(1)

        result_digits.reverse()  # возвращаем порядок цифр в нормальное состояние
        return Natural(''.join(map(str, result_digits)))

    # N-4 Разработчик:Потапов.Р
    @staticmethod
    def ADD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Сложение двух натуральных чисел.
        """
        carry = 0
        result_digits = []

        len1, len2 = len(num1.digits), len(num2.digits)
        max_len = max(len1, len2)

        # Сложение по разрядам с учетом переноса
        for i in range(max_len):
            digit1 = num1.digits[len1 - i - 1] if i < len1 else 0
            digit2 = num2.digits[len2 - i - 1] if i < len2 else 0

            total = digit1 + digit2 + carry
            result_digits.append(total % 10)
            carry = total // 10

        if carry:
            result_digits.append(carry)

        result_digits.reverse()
        return Natural(''.join(map(str, result_digits)))

    # N-5 Разработчик:Глебова.В
    @staticmethod
    @staticmethod
    def SUB_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычитание из первого большего натурального числа второго меньшего или равного.
        """
        # Проверяем, что num1 >= num2
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            raise ValueError("Первое число должно быть больше или равно второму.")

        # Если числа равны, возвращаем 0
        if NaturalOperations.COM_NN_D(num1, num2) == 0:
            return Natural("0")

        result_digits = []
        borrow = 0

        # Вычитаем поразрядно, начиная с младших разрядов
        for i in range(1, len(num1.digits) + 1):
            digit1 = num1.digits[-i]
            digit2 = num2.digits[-i] if i <= len(num2.digits) else 0

            diff = digit1 - digit2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result_digits.append(diff)

        # Разворачиваем результат, убираем ведущие нули
        result_digits.reverse()
        result_str = ''.join(map(str, result_digits)).lstrip("0")

        return Natural(result_str or "0")  # Если строка пустая (все нули), вернуть "0"

    # N-6 Разработчик:Джаватова.З
    @staticmethod
    def MUL_ND_N(num: Natural, digit: int) -> Natural:
        """
        Умножение натурального числа на цифру (от 0 до 9).
        """
        if not (0 <= digit <= 9):
            raise ValueError("Цифра должна быть в пределах от 0 до 9.")

        result_digits = []
        carry = 0

        # Перемножаем каждый разряд числа на цифру
        for i in range(len(num.digits) - 1, -1, -1):
            temp_product = num.digits[i] * digit + carry
            result_digits.append(temp_product % 10)
            carry = temp_product // 10

        # Если есть перенос, добавляем его
        if carry:
            result_digits.append(carry)

        # Переворачиваем результат, чтобы вернуть правильный порядок цифр
        result_digits.reverse()
        return Natural(''.join(map(str, result_digits)))

    # N-7 Разработчик:Тимошук.Е
    @staticmethod
    @staticmethod
    def MUL_Nk_N(num: Natural, k: int) -> Natural:
        """
        Умножение натурального числа на 10^k.
        """
        if k < 0:
            raise ValueError("k должно быть натуральным числом (неотрицательным).")

        if k == 0:
            return num

        # Добавление k нулей в конце числа
        result_digits = num.digits + [0] * k
        return Natural(''.join(map(str, result_digits)))

    # N-8 Разработчик:Тимошук.Е
    @staticmethod
    def MUL_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Умножение двух натуральных чисел.
        """
        result = Natural("0")  # Начальное значение результата - ноль.

        for i in range(len(num2.digits)):  # Перебираем цифры второго числа (num2).
            digit = num2.digits[len(num2.digits) - i - 1]  # Цифра из num2.
            temp = NaturalOperations.MUL_ND_N(num1, digit)  # Умножаем num1 на цифру.
            temp = NaturalOperations.MUL_Nk_N(temp, i)  # Умножаем на 10^i (сдвигаем на разряд).
            result = NaturalOperations.ADD_NN_N(result, temp)  # Прибавляем результат к общему.

        return result

    # N-9 Разработчик:Раутио.И
    @staticmethod
    def SUB_NDN_N(num1: Natural, num2: Natural, digit: int) -> Natural:
        """
        Вычитает из первого натурального числа результат умножения второго натурального числа на цифру.
        """
        if digit < 0 or digit > 9:
            raise ValueError("Цифра должна быть в пределах от 0 до 9.")

        # Умножаем второе число на цифру
        temp = NaturalOperations.MUL_ND_N(num2, digit)

        # Проверяем, что результат вычитания не будет отрицательным
        if NaturalOperations.COM_NN_D(num1, temp) < 0:
            raise ValueError("Результат вычитания будет отрицательным.")

        # Выполняем вычитание
        return NaturalOperations.SUB_NN_N(num1, temp)

    # N-10 Разработчик:Джаватова.З
    @staticmethod
    def DIV_NN_Dk(num1: Natural, num2: Natural, k: int) -> int:
        """
        Вычисление первой цифры деления двух чисел,
        домноженной на 10^k, где k — это номер позиции цифры.
        """

        # Преобразуем числа в строковое представление для удобства работы
        larger_digits = ''.join(map(str, num1.digits))
        smaller_digits = ''.join(map(str, num2.digits))

        # Домножаем num2 на 10^k
        num2_modified = NaturalOperations.MUL_Nk_N(num2, k)
        modified_smaller_digits = ''.join(map(str, num2_modified.digits))

        # Выполняем деление
        quotient = int(larger_digits) // int(modified_smaller_digits)

        # Извлекаем первую цифру от деления
        first_digit = int(str(quotient)[0])

        return first_digit

    # N-11 Разработчик:Раутио.И
    @staticmethod
    def DIV_NN_N(num1: Natural, num2: Natural) -> (Natural, Natural):
        """
        Деление первого натурального числа на второе с остатком.
        Возвращает частное и остаток.
        """
        if NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Делитель не может быть нулём.")

        # Если num1 меньше num2, частное = 0, остаток = num1
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            return Natural("0"), num1

        quotient = []  # Список для хранения цифр частного
        remainder = Natural("0")  # Текущий остаток

        # Перебираем цифры num1 по разрядам
        for digit in num1.digits:
            # Увеличиваем остаток, добавляя текущую цифру
            remainder = NaturalOperations.ADD_NN_N(
                NaturalOperations.MUL_Nk_N(remainder, 1),  # Умножение на 10
                Natural(str(digit))  # Добавляем цифру
            )

            # Считаем, сколько раз num2 помещается в текущем остатке
            current_digit = 0
            while NaturalOperations.COM_NN_D(remainder, num2) != 1:  # Пока остаток >= делителя
                remainder = NaturalOperations.SUB_NN_N(remainder, num2)
                current_digit += 1

            quotient.append(current_digit)

        # Формируем строку из цифр частного
        quotient_natural = Natural(''.join(map(str, quotient)))

        return quotient_natural, remainder

        # N-12 Разработчик:Березовсий.М
    @staticmethod
    def MOD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление остатка от деления первого натурального числа на второе.
        Предполагается, что делитель (num2) не равен нулю.
        """
        if NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Делитель не может быть нулём.")

        # Проверяем, если num1 меньше num2, то остаток — это num1
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            return num1

        # Используем цикл для вычитания num2 до тех пор, пока num1 >= num2
        remainder = num1
        while NaturalOperations.COM_NN_D(remainder, num2) != 1:
            # Находим первую цифру деления и вычитаем умноженное значение
            digit = NaturalOperations.DIV_NN_Dk(remainder, num2, 0)
            temp = NaturalOperations.MUL_ND_N(num2, digit)
            remainder = NaturalOperations.SUB_NN_N(remainder, temp)

        return remainder

    # N-13 Разработчик:Тимошук.Е
    @staticmethod
    def GCF_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление наибольшего общего делителя (НОД) двух натуральных чисел.
        Используется алгоритм Евклида.
        """
        # Проверяем, не равен ли одно из чисел нулю
        if NaturalOperations.NZER_N_B(num1) == "нет" or NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Число не может быть равно нулю.")

        while True:
            # Проверяем, не нужно ли менять местами числа перед расчетом остатка
            if NaturalOperations.COM_NN_D(num1, num2) < 0:
                num1, num2 = num2, num1

            # Получаем остаток от деления
            remainder = NaturalOperations.MOD_NN_N(num1, num2)

            # Если остаток равен нулю, то возвращаем второе число как НОД
            if NaturalOperations.COM_NN_D(remainder, Natural("0")) == 0:
                return num2

            # Если остаток не равен нулю, продолжаем с новым делителем
            num1, num2 = num2, remainder

    # N-14 Разработчик:Тимошук.Е
    @staticmethod
    def LCM_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление наименьшего общего кратного (НОК).
        """
        gcf = NaturalOperations.GCF_NN_N(num1, num2)
        product = NaturalOperations.MUL_NN_N(num1, num2)
        lcm, _ = NaturalOperations.DIV_NN_N(product, gcf)
        return lcm