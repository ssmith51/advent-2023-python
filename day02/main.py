max_cubes = {
  "red": 12,
  "green": 13, 
  "blue": 14
}

def validating_games(games): 
  print("Validating Games")

  valid_game_ids = []
  for game in games.items(): 
    is_valid = True
    for round in game[1].items(): 
      for color, count in round[1].items():
        if color != "total" and count > max_cubes[color]: 
          is_valid = False
    
    
    if is_valid: 
      valid_game_ids.append(game[0])

  return valid_game_ids


def load_games(file): 
  print("Parsing: " + file)

  games = {}
  total_cubes = 0

  f = open(file, "r")
  lines = f.readlines()

  for line in lines: 
    game_id, rounds = line.split(": ")

    game_id = int(game_id.split(" ")[1])
    rounds = rounds.split("; ")
    min_colors = {
      "red": 0,
      "green": 0, 
      "blue": 0,
      "total": 0
    }

    round_results = {}
    round_count = 0
    for round in rounds: 

      round_result = {}
      cubes = round.split(", ")
      

      for cube in cubes: 
        value, color = cube.split(" ")
        value = int(value)
        color = color.strip()
        round_result[color] = value

        if min_colors[color] <  value: 
          min_colors[color] = value
        

      round_results[round_count] = round_result
      round_count += 1

    min_colors["total"] = min_colors["red"] * min_colors["green"] * min_colors["blue"]
    games[game_id] = round_results
    games[game_id]["min_colors"] = min_colors
    total_cubes= total_cubes + min_colors["total"]

  f.close()
  return games, total_cubes

def main(): 
  print("Advent of Code 2023")
  games, total_cubes = load_games("/home/smis45/workspaces/personal/advent-2023-python/day02/input.txt")
  valid_game_ids = validating_games(games)
  sum_game_ids = sum(valid_game_ids)
  print(sum_game_ids)
  print(total_cubes)

if __name__ == "__main__":
  main()