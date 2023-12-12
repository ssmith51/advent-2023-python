import re

def parseVal(str): 
  val = ""
  if str == "one": 
    val = "1"
  elif str == "two": 
    val = "2"
  elif str == "three": 
     val = "3"
  elif str == "four": 
    val = "4"
  elif str == "five":
    val = "5"
  elif str == "six":
    val = "6"
  elif str == "seven":
    val = "7"
  elif str == "eight": 
    val = "8" 
  elif str == "nine": 
    val = "9"

  return val
      
def main(): 
  print("Advent of Code 2024")

  f = open("test.txt", "r")
  lines = f.readlines()


  p = re.compile("^.*?(one|two|three|four|five|six|seven|eight|nine|[0-9]).*(one|two|three|four|five|six|seven|eight|nine|[0-9]).*$")
  sum = 0

  for line in lines: 
    result = p.findall(line)

    if len(result) > 0 and len(result[0]) == 2: 

      first = result[0][0] 
      last = result[0][1]

      #Check for invalid values
      if len(first) == 0 and len(last) > 0: 
          first = last

      elif len(last) == 0 and len(first) >0: 
          last = first

      elif len(last) == 0 and len(first) == 0: 
          first = 0
          last = 0

      #Check for text values
      if len(first) > 1: 
        first = parseVal(first)
      
      if len(last) > 1: 
        last = parseVal(last)

      print(first+last)

      sum = sum + int(first + last)

  f.close()
  print(sum)
  
  


if __name__ == "__main__":
  main()