'''
Ваша программа должна:
Выведите строку Enter your name: . Обратите внимание, что пользователь должен ввести свое имя в той же строке (а не в строке после вывода!)
Прочитать ввод с указанием имени пользователя и вывести новую строку Привет, <имя>
Прочтите файл с именем rating.txt и проверьте, есть ли запись для пользователя с таким же именем; если да, используйте счет, указанный в rating.txtдля этого пользователя, в качестве отправной точки для расчета счета в текущей игре. Если нет, начните подсчет очков пользователя с 0.
Прочтите ввод с указанием списка параметров, которые будут использоваться для игры (параметры разделены запятыми). Если ввод - пустая строка, поиграйте с параметрами по умолчанию.
Вывести строку Okay, let's start
Играйте по правилам, определенным на предыдущих этапах:
Прочитать ввод пользователя
Если вход есть !exit, выведите Bye!и остановите игру
Если вход - это имя опции, то:
Выберите случайный вариант
Выведите строку с результатом игры в следующем формате ( <option>это название опции, выбранной программой):
Проиграть -> Sorry, but the computer chose <option>
Рисовать -> There is a draw (<option>)
Победа -> Well done. The computer chose <option> and failed
За каждый розыгрыш прибавляйте к счету 50 очков. За победу каждого пользователя прибавляйте 100 к его / ее счету. Если пользователь проиграет, не меняйте счет.
Если вход соответствует чему-либо еще, выведите Invalid input
Сыграйте в игру снова (с теми же параметрами, которые были определены перед началом игры)
'''
import random
import sys

file = open('rating.txt', 'r+')
name = input("Enter your name: ")
print("Hello,", name)
count = 0
# file.readlines()
for line in file:
    a = line.split()
    if name in a[0]:
        count += int(a[1])
file.close()

print(count)

sp = input().split()
if sp == []:
    print("Okay, let's start")
    while True:
        word = input()
        opt_list = ['rock', 'scissors', 'paper']
        w = random.choice(opt_list)

        if word == '!rating':
            print('Your rating:', count)

        elif word == '!exit':
            print('Bye!')
            sys.exit()

        elif word == 'scissors':
            if w == 'scissors':
                count += 50
                print("There is a draw (scissors)")
            elif w == 'rock':
                print("Sorry, but the computer chose rock")
            else:
                count += 100
                print("Well done. The computer chose paper and failed")

        elif word == 'rock':
            if w == 'rock':
                count += 50
                print("There is a draw (rock)")
            elif w == 'paper':
                print("Sorry, but the computer chose paper")
            else:
                count += 100
                print("Well done. The computer chose scissors and failed")

        elif word == 'paper':
            if w == 'paper':
                count += 50
                print("There is a draw (paper)")
            elif w == 'scissors':
                print("Sorry, but the computer chose scissors")
            else:
                count += 100
                print("Well done. The computer chose rock and failed")

        else:
            print("Invalid input")
else:
    print("Okay, let's start")
    while True:
        word = input()
        winning_cases = {
            'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
            'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
            'devil': ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning'],
            'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
            'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
            'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
            'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
            'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
            'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
            'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
            'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
            'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
            'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
            'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
        }
        w = random.choice(list(sp))
        if word == '!rating':
            print('Your rating:', count)

        elif word == '!exit':
            print('Bye!')
            sys.exit()

        elif word in winning_cases:
            lst = winning_cases[word]
            if w in lst:
                count += 100
                print("Well done. The computer chose", w, "and failed")
            elif w == word:
                count += 50
                print("There is a draw ", "(", w, ")", sep="")
            else:
                print("Sorry, but the computer chose ",  w)


        else:
            print("Invalid input")
