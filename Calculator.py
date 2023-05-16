# coding: utf-8
import re
#-32/11-32+11-544+32-12-2*4

print("Введите выражение для подсчёта (калькулятор не поддерживает расчёт в скобках):")
calc_st=input()
calc_st_list=re.findall('[\+|-]?\d+|\D', calc_st) #Разбитие строки на числа и знаки "/" "*"
for i in range(0, len(calc_st_list)):
    try:
        calc_st_list[i]=int(calc_st_list[i])
    except:
        pass

def calculation(calc_st_list): # Сначала выполняется "/" и "*" затем сложение
    while "*" in calc_st_list or "/" in calc_st_list:
        for element in calc_st_list:
            if element == "*":
                element_index=calc_st_list.index(element)
                calc_st_list[element_index-1]=round(calc_st_list[element_index-1]*calc_st_list[element_index+1],1)
                calc_st_list.pop(element_index+1)
                calc_st_list.pop(element_index)
                break
            if element == "/":
                element_index=calc_st_list.index(element)
                calc_st_list[element_index-1]=round(calc_st_list[element_index-1]/calc_st_list[element_index+1],1)
                calc_st_list.pop(element_index+1)
                calc_st_list.pop(element_index)
                break
    result = sum(calc_st_list)
    return (result)
calculation(calc_st_list)     
