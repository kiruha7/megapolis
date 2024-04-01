with open('monster_game.csv', encoding='UTF-8') as f:
    f = f.read().split('\n')[1:]
    opportunity = input()
    count = 0
    for i in range(len(f) - 1):
        data = f[i].split(',')
        if data[1] == opportunity:
            print(data[0] + ' ' + data[1] + ' ' + data[2] + ' - ' + opportunity)
            count += 1
            if count == 10:
                break