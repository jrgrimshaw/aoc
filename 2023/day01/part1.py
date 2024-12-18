def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()

def collab_values(line):
  start, end = "", ""
  numbers = "0123456789"

  for i in range(len(line)):
    if line[i] in numbers:
      if start == "":
        start = line[i]
      else:
        end = line[i]
                   
  return start, end or start

def main():
  input = read_file()
  lines = input.split("\n")

  total = 0
  for line in lines:
    if line:
      start, end = collab_values(line)
      print(start, end)
      total += int(start + end)

  print(total)
    
if __name__ == '__main__':
  main()