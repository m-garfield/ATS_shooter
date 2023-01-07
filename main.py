from Option import input_option

class Shooter:
    def __init__(self):
        self.surname = input("Введите Фамилию стрелка -> ")
        self.name = input("Введите Имя стрелка -> ")
        print("class begin")



print("                      Вводим исходные данные для упражнения.  ")
dict_option = input_option()

shooter1 = Shooter()