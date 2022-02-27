import random

desc1 = "1 - simple operations with numbers 2-9"
desc2 = "2 - integral squares 11-29"


while True:
    print("Which level do you want? Enter a number:")
    print(desc1, desc2, sep='\n')
    choice = input()

    if choice not in ('1', '2'):
        print("Incorrect format.")
        continue
    correct_resp = 0

    for _ in range(5):
        if choice == '1':
            desc = desc1
            op = random.choice(('+', '-', '*'))
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            print(a, op, b)
            while True:
                try:
                    expr = int(input())
                except ValueError:
                    print("Incorrect format.")
                else:
                    resp = eval(str(a) + op + str(b))
                    if expr == resp:
                        correct_resp += 1
                        print('Right!')
                    else:
                        print('Wrong!')
                    break
        elif choice == '2':
            desc = desc2
            result = random.randint(11, 29)
            print(result)
            while True:
                try:
                    user_resp = int(input())
                except ValueError:
                    print("Incorrect format.")
                else:
                    if user_resp == result ** 2:
                        correct_resp += 1
                        print('Right!')
                    else:
                        print('Wrong!')
                    break

    print(f'Your mark is {correct_resp}/5.')

    print("Would you like to save your result to the file? Enter yes or no.")
    write = input()
    if write.lower() in ('yes', 'y'):
        username = input('username: ')
        with open('results.txt', 'a') as f:
            f.write(f"{username}: {correct_resp}/5 in level {choice} ({desc[4:]}).")

        print('The results are saved in "results.txt".')
    break
