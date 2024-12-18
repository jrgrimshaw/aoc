def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  games = input.split("\n")
  total = 0

  for game in games:
    if game:
      split = game.split(":")
      id = int(split[0].split(" ")[1])
      sets = split[1].split(";")

      totals = {
        "blue": 0,
        "red": 0,
        "green": 0
      }

      for set in sets:
        bags = set.split(",")
        
        for bag in bags:
          bag_split = bag.strip().split(" ")
          count = int(bag_split[0])
          color = bag_split[1]

          if count > totals[color]:
            totals[color] = count

      power = totals["red"] * totals["green"] * totals["blue"]
      total += power

      print(id, totals, power)

  print('total', total)
    
  
if __name__ == '__main__':
  main()