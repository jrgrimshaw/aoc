def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  rows = input.split("\n")
  numbers = []
  cur_num = ""
  has_adjacent_symbol = False

  for x in range(len(rows)):
    for y in range(len(rows[x])):
      if rows[x][y].isdigit():
        cur_num += rows[x][y]

        for i in [-1, 0, 1]:
          for j in [-1, 0, 1]:
            if x + i >= 0 and x + i < len(rows) and y + j >= 0 and y + j < len(rows[x]):
              if not rows[x + i][y + j].isdigit() and not rows[x + i][y + j] == ".":
                has_adjacent_symbol = True
      elif cur_num:
        if has_adjacent_symbol:
          numbers.append(int(cur_num))
          has_adjacent_symbol = False
        cur_num = ""

  print(numbers)
  print(sum(numbers))
  
if __name__ == '__main__':
  main()