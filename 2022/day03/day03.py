def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def priority(item):
  charNum = ord(item)
  val = 0
  if charNum >= 97: val = charNum - 96
  if charNum >= 65 and charNum <= 96: val = charNum - 38
  return val

def partOne(rucksacks):
  prioritySum = 0

  for rucksack in rucksacks:
    compartments = [rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
    commonItems = list(set(compartments[0]).intersection(compartments[1]))
    prioritySum += priority(commonItems[0])

  return prioritySum

def partTwo(rucksacks):
  prioritySum = 0

  for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i + 3]
    commonItemsCount = {}

    for rucksack in group:
      commonItems = set(group[0]).intersection(rucksack)

      for item in commonItems:
        commonItemsCount[item] = commonItemsCount.get(item, 0) + 1

    badge = list(commonItemsCount.keys())[list(commonItemsCount.values()).index(3)]
    prioritySum += priority(badge)

  return prioritySum

def main():
  file = readFile("input.txt")
  rucksacks = file.split("\n");
  
  print(partOne(rucksacks))
  print(partTwo(rucksacks))

if __name__ == "__main__":
  main()