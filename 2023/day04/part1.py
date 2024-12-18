def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  cards = input.split("\n")
  total_points = 0

  for card in cards:
    if card:
      card_numbers = card.split(": ")[1].split(" | ")
      winning_numbers = list(filter(bool, card_numbers[0].split(" ")))
      chosen_numbers = list(filter(bool, card_numbers[1].split(" ")))

      points = 0
      for winning_number in winning_numbers:
        if winning_number in chosen_numbers:
          if points == 0: points = 1
          else: points = points * 2

          print('match!', winning_number, points)

      total_points += points

  print(total_points)

if __name__ == '__main__':
  main()