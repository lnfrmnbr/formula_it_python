list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

def dividing_players(ls):
    num_players = len(ls)
    print(ls[0:(num_players // 2)])
    print(ls[(num_players // 2):len(ls)])

dividing_players(list_players)
