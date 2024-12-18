def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  games = input.split("\n")
  ids_total = 0

  for game in games:
    if game:
      split = game.split(":")
      id = int(split[0].split(" ")[1])
      sets = split[1].split(";")

      possible = True

      for set in sets:
        totals = {
          "blue": 0,
          "red": 0,
          "green": 0
        }
        bags = set.split(",")
        
        for bag in bags:
          bag_split = bag.strip().split(" ")
          count = int(bag_split[0])
          color = bag_split[1]

          totals[color] += count

        if totals["red"] > 12 or totals["green"] > 13 or totals["blue"] > 14:
          possible = False
        
      if possible:
        ids_total += id

      print(id, possible)

  print('ids total', ids_total)
    
  
if __name__ == '__main__':
  main()