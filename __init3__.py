# Свинипух

# phraze = input("vvedite phrazu stiha: ").upper()
# dic_gl = {
#     'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я'
# }
# spis = phraze.split(' ')
# summ_w = None
# summ=0
# d =1
# for word in spis:          # Перебираем слова в списке

#     summ = 0
#     for letter in word:    # Перебираем буквы каждого слова        
#         if letter in dic_gl:
#             summ = summ+1
#     print (summ)
#     if summ_w is None:     # Если это первое слово, сохраняем количество слогов
#         summ_w = summ
#     elif summ_w != summ:   # Если количество слогов отличается, прерываем цикл
#         print("Пам парам")
#         break
# else:                      # Если цикл завершился без break, значит ритм есть
#     print("Парам пам-пам")

num_rows = int(input('vvedite rows'))
num_columns = int(input('vvedite kolonki'))


def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=' ')
        print()  # переход на новую строку после завершения столбца

# Пример использования:
print_operation_table(lambda x, y: x * y, num_rows, num_columns)