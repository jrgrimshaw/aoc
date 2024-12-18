def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  cards = input.split("\n")

  cards_counter = []
  for i in range(len(cards)):
    cards_counter.append(1)

  for i in range(len(cards)):
    count = cards_counter[i]
    card = cards[i]
    card_numbers = card.split(": ")[1].split(" | ")
    winning_numbers = list(filter(bool, card_numbers[0].split(" ")))
    chosen_numbers = list(filter(bool, card_numbers[1].split(" ")))

    match_count = 1
    for winning_number in winning_numbers:
      if winning_number in chosen_numbers:
        cards_counter[i + match_count] += count
        match_count += 1

  print(sum(cards_counter))
  
if __name__ == '__main__':
  main()