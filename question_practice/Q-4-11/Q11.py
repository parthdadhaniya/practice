# Q11. Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)


num_of_game_played = int(input("Enter number of game played : "))
num_of_game_won = int(input("Enter number of game won : "))


total_number_of_win = num_of_game_won * 4
total_number_of_ties = (num_of_game_played - num_of_game_won) * 2
total_point = total_number_of_win + total_number_of_ties

print(
    f"Total number of win point {total_number_of_win}, Total number of ties point {total_number_of_ties}"
)

print("Total point", total_point)
