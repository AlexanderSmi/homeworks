# Задача 1.1.
# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
#разбиваем строку по символам ", "
splitted_line = my_favorite_songs.split(', ')
#выводим результат
print(splitted_line[0],'\n',splitted_line[len(splitted_line)-1],'\n',splitted_line[1],'\n',splitted_line[len(splitted_line)-2])
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
