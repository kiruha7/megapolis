with open('monster_game.csv', encoding='UTF-8') as f:
    f = f.read().split('\n')[1:]
    ans = []
    attack = input()
    while attack != 'хватит':
        ans = 0
        attack = int(attack)
        for i in range(len(f) - 1):
            data = f[i].split(',')
            if (attack > int(data[5])) and (int(data[5]) != 0):
                ans += 1
        if ans == 0:
            print('Вы очень слабы. Сходите и наберитесь опыта!')
        else:
            print(f'Вы сможете победить: {ans} монстров')
        attack = input()

