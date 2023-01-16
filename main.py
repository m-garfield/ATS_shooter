import Function
from Option import input_option

print("                      Вводим исходные данные для упражнения.  ")
dict_option = input_option()
list_rez = []
while True:
    surname_name= Function.input_name()
    time_all_foul_procedur = Function.foul_procedur(dict_option['foul_procedure'])
    sum_foul_target_zone = Function.all_time_foul_targets_zone(dict_option['count_target'], dict_option['count_shoot_in_target'])
    list_rez.append(Function.calculation_of_result_shooter(surname_name[0], surname_name[1], surname_name[2], time_all_foul_procedur, sum_foul_target_zone))
    answer_continion = input("Продолжаем? Да/Нет -->  ")
    if answer_continion == "Нет":
        list_rez = Function.sort_of_lieder(list_rez)
        Function.load_excel(list_rez)
        break




