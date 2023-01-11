
def chek_input(count_shoot, str_input, foul_a=0, foul_b = 1, foul_w = 5, foul_0 = 10):
        sum_foul_target_zone = 0
        x = len(str_input)
        if len(str_input) != int(count_shoot):
            return False
        for i in str_input:
            if i == 'а':
                sum_foul_target_zone = sum_foul_target_zone + foul_a
            elif i == 'б':
                sum_foul_target_zone = sum_foul_target_zone + foul_b
            elif i == 'в':
                sum_foul_target_zone = sum_foul_target_zone + foul_w
            elif i == '0':
                sum_foul_target_zone = sum_foul_target_zone + foul_0
            else:
                return False
        return str(sum_foul_target_zone)

def calculation_of_result_shooter (surname, name, time_all_foul_procedur, sum_foul_target_zone):
    dect_of_rezult = {}
    dect_of_rezult['surname'] = surname
    dect_of_rezult['name'] = name
    dect_of_rezult['sum_foul_target_zone'] = sum_foul_target_zone
    dect_of_rezult['time_all_foul_procedur'] = time_all_foul_procedur
    dect_of_rezult['time_all_foul'] =  int(dect_of_rezult['sum_foul_target_zone']) + int(dect_of_rezult['time_all_foul_procedur'])
    return  dect_of_rezult

def input_name():
    while True:

        surname = input('Введите фамилию стрелка --> ')
        name = input('Введите имя стрелка --> ')
        answer= input(f"Фамилия Имя стрелка {surname} {name}? Верно Да/Нет --> ")
        if answer == "Да":
            break
    return [surname, name]
def foul_procedur (foul_procedure):
    count_foul_procedur = int(input('Введите количество процедурных штрафов у стрелка -->  '))
    x=0
    time_all_foul_procedur = count_foul_procedur * int(foul_procedure)
    return time_all_foul_procedur

def all_time_foul_targets_zone(count_target, count_shoot):
    all_time_foul_targets_zone = 0
    x = count_target
    while x > 0:
        while True:
            str_input = input(f'Введите попадания в мишень {count_target - x + 1} --> ')
            rez = chek_input(count_shoot, str_input)
            if rez != False:
                all_time_foul_targets_zone = all_time_foul_targets_zone + int(rez)
                break
        x = x-1

    return all_time_foul_targets_zone
##di = {
    #return"кг":[1,2,3],
   # "слова":["сала","мало","мама"]
    # }
##z = pd.DataFrame(di)
#z.to_excel("file_name.xlsx")