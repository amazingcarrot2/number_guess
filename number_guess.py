import requests


def number_guess(player):
    url = 'https://python666.cn/cls/number/guess/'
    num = int(requests.get(url).text)
    guess = input('guess a number between 0 and 100:')
    latest_pef = 0
    end_game = False
    while not end_game:
        latest_pef += 1
        try:
            int(guess)
        except:
            guess = input('Input numbers only:')
        else:
            if int(guess) > num:
                guess = input(
                    'Try smaller number:')
            elif int(guess) < num:
                guess = input(
                    'Try larger number:')
            elif int(guess) == num:
                print('you got it! congratulations!')
                end_game = True
    ave_perf = str(
        round(
            (int(player['times']) * float(player['ave_perf']) + latest_pef) / (
                    int(player['times']) + 1), 2))
    times = str(int(player['times']) + 1)
    return [str(latest_pef), times, ave_perf]


def game(name, records_dic):
    stop = False
    print(records_dic)
    if len(records_dic) > 0:
        for player in records_dic:
            if stop:
                break
            if player['name'] == str(name):
                print(player)
                finished_player = number_guess(player)
                player['latest_perf'] = finished_player[0]
                player['times'] = finished_player[1]
                player['ave_perf'] = finished_player[2]
                player['best_perf'] = str(
                    min(int(finished_player[0]), int(player['best_perf'])))
                stop = True
                print(player)
                print('游戏结束')
            else:
                player = {'name': name, 'latest_perf': '0', 'times': '0',
                          'ave_perf':
                              '0', 'best_perf': '0'}
                print(player)
                finished_player = number_guess(player)
                player['latest_perf'] = finished_player[0]
                player['times'] = finished_player[1]
                player['ave_perf'] = finished_player[2]
                player['best_perf'] = finished_player[0]
                records_dic.append(player)
                stop = True
                print(player)
                print('游戏结束')
    else:
        player = {'name': name, 'latest_perf': '0', 'times': '0',
                  'ave_perf':
                      '0', 'best_perf': '0'}
        print(player)
        finished_player = number_guess(player)
        player['latest_perf'] = finished_player[0]
        player['times'] = finished_player[1]
        player['ave_perf'] = finished_player[2]
        player['best_perf'] = finished_player[0]
        records_dic.append(player)
        print(player)
        print('游戏结束')
        print(records_dic)
    return records_dic


def file_read():
    records = []
    try:
        open('records.txt', 'r')  # 判断是否已有记录表
    except:
        with open('records.txt',
                  'x') as f:  # 没有记录表则新建一个，表头为用户名，最新成绩，游玩次数，平均成绩，最好成绩
            title = 'name latest_perf times ave_perf best_perf\n'
            f.writelines(title)
            print('创建新表单')
            f.close()
    finally:  # 打开记录表，读取表中已有的数据。
        with open('records.txt', 'r') as fin:
            lines = fin.readlines()
            for line in lines:
                line = line.strip('\n')
                ''.join(line)
                line = line.split(' ')
                records.append(line)
            print('表单读取ok')
            print(records)
    return records


if __name__ == '__main__':
    name = input('please input your name:')
    # 文件读取
    exit_game = False
    records = file_read()
    records_dic = []
    if len(records) == 1:
        print('无数据')
    else:
        dic_ele = records.pop(0)
        for player in records:  # 对读取的数据进行处理，先将表中的已有的player变为字典储存在list中
            player_dic = dict(zip(dic_ele, player))
            records_dic.append(player_dic)
    print('原始表单已转化为字典')
    new_record = game(name, records_dic)  # new_record 储存了所有玩家的信息
    while not exit_game:
        again = input('Play Again?(Type Y to Play one more time):')
        if again == 'Y':
            new_record = game(name, new_record)
        else:
            exit_game = True
    print(new_record)
    title = 'name latest_perf times ave_perf best_perf\n'
    result_lst = []
    for player in new_record:
        result = []
        for value in player.values():
            result.append(value)
        result_lst.append(result)
    print(result_lst)
    with open('records.txt', 'w') as fin:
        fin.writelines(title)
        for result in result_lst:
            result = " ".join(result)
            fin.write(result)
            fin.write('\n')
