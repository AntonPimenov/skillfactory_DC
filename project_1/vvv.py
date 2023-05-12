# Приводим строку к нижнему регистру и заменяем пробелы на пустые строки
target_string = 'Шалаш'


target_string = target_string.lower().replace(' ', '')
# Сравниваем преобразованную строку с ней же в развернутом варианте
result = target_string == target_string[::-1]
print(result)