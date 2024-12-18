def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def elvesCalories():
  rawData = readFile("input.txt")

  split = rawData.split("\n\n")
  elves = []
  
  for i, line in enumerate(split):
    elves.append(sum(int(x) for x in line.split("\n")))

  elves.sort(reverse=True)

  return elves

def main():
  elves = elvesCalories()
  
  print(elves[0]) # part one
  print(elves[0] + elves[1] + elves[2]) # part two

if __name__ == "__main__":
  main()