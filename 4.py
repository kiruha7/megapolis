with open('monster_game.csv', encoding='UTF-8') as f:
    f = f.read().split('\n')[1:]
    ans = []
    dict_monstr_damage = {}
    dict_monstr_n = {}
    for i in range(len(f)-1):
        data = f[i].split(',')
        monstr = data[0].split(' ')[1]
        if monstr in dict_monstr_damage:
            dict_monstr_damage[monstr] += int(data[3])
            dict_monstr_n[monstr] += 1
        else:
            dict_monstr_damage[monstr] = int(data[3])
            dict_monstr_n[monstr] = 1
    for elem in dict_monstr_damage:
        print(f'{dict_monstr_n[elem]} монстров класса {elem.capitalize()}, средняя сила атаки {dict_monstr_damage[elem] / dict_monstr_n[elem]}')