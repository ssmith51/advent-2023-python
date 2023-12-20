import re

def load_file(file): 
  f = open(file, "r")
  lines = f.readlines()
  grid =[]
  data = {
    "grid": grid,
    "max_x": 0,
    "max_y": 0  
  }

  for line in lines: 
    row = []
    for char in line.strip(): 
      row.append(char)

    grid.append(row)
    data["max_y"] += 1

  data["max_x"] = len(grid[0])
  f.close()
  return data

def parse_parts(data): 
  grid = data["grid"]
  max_x = data["max_x"]
  max_y = data["max_y"]

  parts = []
  part = {
    "gear": "", 
    "start_x": 0, 
    "start_y": 0,
    "catalog": "",
    "grid": []
  }

  #Parse all the parts
  for yi, y in enumerate(grid):
    for xi, x in enumerate(y): 
      if x.isdigit() and part["gear"] == "":
        part["gear"] = part["gear"]+ x
        part["start_x"] = xi
        part["start_y"] = yi

      elif x.isdigit(): 
        part["gear"] = part["gear"]+ x

      elif not x.isdigit() and len(part["gear"]) > 0: 
        parts.append(part)

        end_x = part["start_x"] + len(part["gear"]) +1
        end_y = part["start_y"]+ 1

        if end_x > max_x: end_x = max_x
        if end_y > max_y: end_y = max_y -1
        if part["start_y"] == 0: part["start_y"] = 1
        if part["start_x"] == 0: part["start_x"] = 1

        # Generate the parts 'catalog'
        y = part["start_y"]-1
        while  y <= end_y and y < max_y: 
          cat = []
          x = part["start_x"]-1
          while x < end_x: 
            part["catalog"] = part["catalog"] + grid[y][x]
            cat.append(grid[y][x])
            x = x + 1
            
          part["grid"].append(cat)
          y = y + 1

        part = {
          "gear": "", 
          "start_x": 0, 
          "start_y": 0,
          "catalog": "",
          "grid": []
        }

  return parts
       
def sum_parts(parts):
  sum = 0

  sum_parts = []
  not_parts = []

  p = re.compile("[^.0-9]")
  for part in parts:
    if p.search(part["catalog"]):
      sum_parts.append(part)
      sum = sum + int(part["gear"])
    else: 
      not_parts.append(part)

  return sum

def main(): 
  print("Advent of Code 2023")
  data = load_file("/home/smis45/workspaces/personal/advent-2023-python/day03/input.txt")
  parts = parse_parts(data)
  sum = sum_parts(parts)
  print(sum)


if __name__ == "__main__":
  main()