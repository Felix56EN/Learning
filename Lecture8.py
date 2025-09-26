input_file = 'C:\\Новая папка\\text_file.txt'
output_file = "C:\\Новая папка\\reversed_text_file.txt"

with open(input_file, 'r', encoding='utf-8') as file:
    original = file.read()

revers = original[::-1]

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(revers)

print('---Оригинальный файл---')
with open(input_file,'r', encoding='utf-8') as input_file:
    for line in input_file:
        print(line)

print('---Перевернутый файл---')
with open(output_file,'r', encoding='utf-8') as output_file:
    for line in output_file:
        print(line)