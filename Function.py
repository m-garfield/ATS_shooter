import openpyxl
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

def calculation_of_result_shooter (surname, name, time_distantion, time_all_foul_procedur, sum_foul_target_zone ):
    dect_of_rezult = {}
    dect_of_rezult['surname'] = surname #Фамилия
    dect_of_rezult['name'] = name #Имя
    dect_of_rezult['sum_foul_target_zone'] = sum_foul_target_zone #
    dect_of_rezult['time_all_foul_procedur'] = time_all_foul_procedur #

    time_all_foul=  int(dect_of_rezult['sum_foul_target_zone']) + int(dect_of_rezult['time_all_foul_procedur'])
    dect_of_rezult['time_all_foul'] = time_all_foul #общее время всех штрафов
    dect_of_rezult['time_distantion'] = time_distantion #Время прохождения без штрафов
    dect_of_rezult['time_of_rezult'] = int(time_all_foul) + int(time_distantion) #Результируещее время всей дистанции со штрафами
    return dect_of_rezult

def input_name():
    while True:

        surname = input('Введите фамилию стрелка --> ')
        name = input('Введите имя стрелка --> ')
        time_distantion = input('Введите время прохождения дистанции  --> ')
        answer= input(f"{surname} {name} прошел за {time_distantion} секунд. Верно? Да/Нет --> ")
        if answer == "Да":
            break
    return [surname, name, time_distantion]
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
def load_excel(list_rez):
    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = 'Фамилия'
    sheet['B1'] = "Имя"
    sheet['C1'] = "Штраф за попадания в мишени"
    sheet['D1'] = "Процедурные штрафы"
    sheet['E1'] = "Время прохождения дистанции"
    sheet['F1'] = "Результирующее время на дистанции"
    row = 2
    for rez_string in list_rez:
        sheet[row][0].value = rez_string['surname']
        sheet[row][1].value = rez_string['name']
        sheet[row][2].value = rez_string['sum_foul_target_zone']
        sheet[row][3].value = rez_string['time_all_foul_procedur']
        sheet[row][4].value = rez_string['time_distantion']
        sheet[row][5].value = rez_string['time_of_rezult']
        row += 1
    book.save("Результаты соревнования.xlsx ")

    book.close()


def sort_of_lieder(list_rez):
    list_rez = sorted(list_rez, key= lambda shooter: shooter["time_of_rezult"])
    return list_rez


