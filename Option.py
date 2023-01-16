import pandas

def input_option ():
    while True:
        dict_option = {}
        dict_option['count_target'] = int(input('Введите количество мишеней в поле -> '))
        dict_option['count_shoot_in_target'] = int(input('Введите количество выстрелов в мишень -> '))
        dict_option['foul_procedure'] = int(input('Введите штрафное время процедурного штрафа -> '))
        dict_option['count_granade'] = int(input('Введите количество бросков гранат -> '))

        print(f"\n                                    Исходные данные упражнения: ")
        print(f"В поле {dict_option['count_target']} мишеней по {dict_option['count_shoot_in_target']} выстрела в каждую.")
        print(f"Бросков гранат: {dict_option['count_granade']}")
        print(f"Время процедурного штрафа: {dict_option['foul_procedure']} секунд.")
        answer = input("Верно? Да / Нет? ->  ")
        if answer == "Да":
            break
    return dict_option
