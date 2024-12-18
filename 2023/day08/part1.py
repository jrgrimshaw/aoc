def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file().split("\n\n")
  instructions = input[0].strip()
  rows = [row.split(" = ") for row in input[1].split("\n")]
  paths = {}
  for row in rows:
    paths[row[0]] = row[1][1:-1].split(", ")
  
  #finding
  current_node = "AAA"
  count = 0
  i = 0
  
  while current_node != "ZZZ":
    if i >= len(instructions):
      i = 0
    dir = instructions[i]
    if dir == "L":
      current_node = paths[current_node][0]
    elif dir == "R":
      current_node = paths[current_node][1]

    i+=1
    count+=1

  print(count)
  
if __name__ == '__main__':
  main()