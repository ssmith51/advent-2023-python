def load(file): 
  f = open(file, "r")
  lines = f.readlines()
  cards = []

  for line in lines: 
    print(line.strip())
    card = {
      "win_nums": [], 
      "card_nums": [], 
      "count": 1,
      "wins": 0
    }

    win_nums = line.split("|")[0].split(":")[1].strip().split(" ")
    card_nums = line.split("|")[1].strip().split(" ")

    for num in win_nums: 
      if num != "":
        card["win_nums"].append(int(num))
    
    for num in card_nums: 
      if num != "":
        card["card_nums"].append(int(num))

    cards.append(card)
  f.close()

  return cards

def solve(cards):

  total = 0
  for i, card in enumerate(cards): 
    card_total = 0
    wins = 0 
    for w in card["win_nums"]: 
      if w in card["card_nums"]: 
        if card_total == 0: 
          card_total = 1 
          wins = wins + 1
        else:
          card_total = (card_total * 2)
          wins = wins +1
    
    total = total + card_total
    cards[i]["wins"] = wins

    for x in range(wins): 
      cards[i+x+1]["count"] = cards[i+x+1]["count"] + card["count"]


  count = 0
  for card in cards: 
    count = count + card["count"]

  print(count)

  return total
        

def main(): 
  print("Advent of Code 2023")
  cards = load("/home/smis45/workspaces/personal/advent-2023-python/day04/input.txt")
  total = solve(cards)
  print(total)


if __name__ == "__main__":
  main()