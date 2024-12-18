def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  original_rows = [list(reversed(list(map(int, row.split(" "))))) for row in input.split("\n")]
  next_nums = []

  for o in range(len(original_rows)):
    i = 1
    new_rows = [original_rows[o]]
    while not all(x == 0 for x in new_rows[i-1]):
      new_rows.append([])
      for j in range(len(new_rows[i-1])):
        if j+1 < len(new_rows[i-1]):
          new_rows[i].append(new_rows[i-1][j+1] - new_rows[i-1][j])
      i += 1
    next_nums.append(get_next_in_seq(new_rows))

  for i in range(len(next_nums)):
    print(original_rows[i])

  print('answer:', sum(next_nums))
  
def get_next_in_seq(rows):
  for x in reversed(range(len(rows))):
    if x-1 >= 0:
      rows[x-1].append(rows[x-1][-1] + rows[x][-1])
    else:
      return rows[x][-1] 

if __name__ == '__main__':
  main()