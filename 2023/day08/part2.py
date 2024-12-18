import math

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
  current_nodes = []
  for path in list(paths.keys()):
    if path[2] == "A":
      current_nodes.append(path)

  counts = []
  for j in range(len(current_nodes)):
    current_node = current_nodes[j]
    count = 0
    i = 0
    
    while current_node[2] != "Z":
      if i >= len(instructions):
        i = 0
      dir = instructions[i]
  
      if dir == "L":
        current_node = paths[current_node][0]
      elif dir == "R":
        current_node = paths[current_node][1]

      i+=1
      count+=1

    counts.append(count)

  print(math.lcm(*counts))
  
if __name__ == '__main__':
  main()