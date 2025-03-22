# everything has it`s own comments

from calculator_new_ver_alpha.module_sum import action_1 # module 1 import
from calculator_new_ver_alpha.module_sum import action_2 # module 2 import
from calculator_new_ver_alpha.module_sum import action_3 # module 3 import
from calculator_new_ver_alpha.module_sum import action_4 # module 4 import
from calculator_new_ver_alpha.module_sum import action_5 # module 5 import

print("Действие\n1. Сложить\n2. Вычесть\n3. Умножить\n4. Разделить\n5. Выйти\n") # actions list

while True: # loop start
    action = input("Выберите действие: ") # action choice

    if action.lower() == "сложить": # summary action
        action_1() # action call
    if action.lower() == "вычесть": # subtraction action
        action_2() # action call
    if action.lower() == "умножить": # multiplying action
        action_3() # action call
    if action.lower() == "разделить": # dividing action
        action_4() # action call
    if action.lower() == "выйти": # exit action
        action_5() # action call