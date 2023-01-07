
def input_option ():
    while True:
        dict_option = {}
        dict_option['count_shoot_in_target'] = input('Введите количество выстрелов в мишень -> ')
        dict_option['count_target'] = input('Введите количество мишеней -> ')
        dict_option['foul_procedure'] = input('Введите время процедурного штрафа -> ')
        print(f"количество выстрелов в мишень -> {dict_option['count_shoot_in_target']}")
        print("Верно? Да / Нет" )
        answer = input("->  ")
        if answer == "Да":
            break
    return dict_option
