import random

ask_list = []
while True:
    ask_input = input("문제를 낼 단어를 입력하세요: ")
    if ask_input == "done!":
        break
    else:
        ask_list.append(ask_input)
        print(ask_list)
        print("-"*50)
        print("입력이 끝났으면 'done!'를 입력해 주세요")
ask = random.choice(ask_list)
life = int(input("원하는 목숨 갯수를 입력하세요: "))

letters = ""
while life > 0 :
    succeed = True
    for i in ask:
        if i in letters:
            print(i, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    if succeed:
        print("성공!")
        break
    print(" \n")
    print("현재까지 나온 알파벳 ("+",".join(letters)+")")
    answer = input("\n알파벳을 입력하세요: ")
    print("-"*50)
    if answer in letters:
        print("입력했던 알파벳 입니다. 다시 입력하세요\n")
    else:
        if answer in ask:
            letters += answer
            print("맞았습니다.")
        else:
            letters += answer
            life -= 1
            print("틀렸습니다. 라이프가 1 감소합니다. life: {}".format(life))        
if life == 0:    
    print("실패...")