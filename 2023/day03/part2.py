def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  rows = input.split("\n")
  gears = []

  for x in range(len(rows)):
    for y in range(len(rows[x])):
      if rows[x][y] == "*":
        numbers = []

        for i in [-1, 0, 1]:
          for j in [-1, 0, 1]:
            if x + i >= 0 and x + i < len(rows) and y + j >= 0 and y + j < len(rows[x]):
              if rows[x + i][y + j].isdigit():
                number = ""
                search_index = 0

                for dir in [-1, 1]:
                  if dir == 1: search_index = 1 
                  while y + j + search_index >= 0 and y + j + search_index < len(rows[x]):
                    if not rows[x + i][y + j + search_index].isdigit(): break
                    else:
                      if dir == -1:
                        number = rows[x + i][y + j + search_index] + number
                      else:
                        number += rows[x + i][y + j + search_index]
                      search_index += dir

                if number and int(number) not in numbers:
                  numbers.append(int(number))
                  number = ""

        if len(numbers) == 2:
          gears.append(numbers[0] * numbers[1])
    
  print(sum(gears))
  
if __name__ == '__main__':
  main()