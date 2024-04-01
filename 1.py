with open('monster_game.csv', encoding='UTF-8') as f:
    f = f.read().split('\n')[1:]
    ans = []
    mx_health = 0
    for i in range(len(f) - 1):
        cur_sp = []
        data = f[i].split(',')
        if data[1] == 'регенерация':
            cur_health = int(data[5]) * int(data[2]) / 100
            if cur_health > mx_health:
                mx_health = cur_health
            cur_sp.append('регенерация')
            cur_sp.append(cur_health)
        elif data[1] == 'усиление атаки':
            cur_sp.append('усиление атаки')
            cur_sp.append(int(data[3]) * int(data[2]) / 100)
        elif data[1] == 'дополнительный ход':
            cur_sp.append('дополнительный ход')
            cur_sp.append((int(data[3]) + int(data[4]) + int(data[5]) + int(data[6])) * int(data[2]) / 100)
        ans.append(cur_sp)


with open('monster_opportunity.csv', encoding='UTF-8', mode='w') as new_f:
    new_f.write('opportunity, power\n')
    for elem in ans:
        new_f.write(f'{elem[0]}, {elem[1]}\n')

print(mx_health)

