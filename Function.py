

def chek_input(count_shoot, str_input, foul_a=0, foul_b = 1, foul_w = 5, foul_0 = 10):
    sum_foul = 0
    x = len(str_input)
    if len(str_input) != int(count_shoot):
        return False
    for i in str_input:
        if i == 'а':
            sum_foul = sum_foul + foul_a
        elif i == 'б':
            sum_foul = sum_foul + foul_b
        elif i == 'в':
            sum_foul = sum_foul + foul_w
        elif i == '0':
            sum_foul = sum_foul + foul_0
        else:
            return False
        return sum_foul
