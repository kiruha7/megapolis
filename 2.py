with open('monster_game.csv', encoding='UTF-8') as f:
    f = f.read().split('\n')[1:]
    ans = []
    for i in range(len(f) - 1):
        cur_sp = []
        data = f[i].split(',')
        cur_sp.append(data[0])
        if data[1] == 'регенерация':
            cur_sp.append('регенерация')
            cur_sp.append(int(data[6]) * int(data[2]) / 100)
        elif data[1] == 'усиление атаки':
            cur_sp.append('усиление атаки')
            cur_sp.append(int(data[3]) * int(data[2]) / 100)
        elif data[1] == 'дополнительный ход':
            cur_sp.append('дополнительный ход')
            cur_sp.append((int(data[3]) + int(data[4]) + int(data[5]) +int(data[6])) * int(data[2]) / 100)
        ans.append(cur_sp)
    i = 0
    while i != len(ans) - 1:
        if ans[i][1] > ans[i+1][1]:
            a = ans[i][1]
            ans[i][1] = ans[i+1][1]
            ans[i+1][1] = a
            i = 0
        else:
            i += 1
    for i in range(3):
        print(f'{ans[i][0]} имеет возможность: {ans[i][1]}, вероятность использования возможности равна {ans[i][2]}')