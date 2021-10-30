def get_player_names(players: int):
    players_list = []
    for i in range(1, players+1):
        players_list.append(input(f"Player {i}: Please state your name: "))
    print(players_list)

get_player_names(4)
