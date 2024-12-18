def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def parsePairs(file):
  pairs = file.split("\n")
  for i, pair in enumerate(pairs):
    sections = pair.split(",")
    for j, section in enumerate(sections):
      sections[j] = [int(x) for x in section.split("-")]
    pairs[i] = sections

  return pairs

def partOne(pairs):
  count = 0

  for pair in pairs:
    if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]):
      count += 1

  return count

def partTwo(pairs):
  count = 0

  for pair in pairs:
    if pair[0][0] <= pair[1][1] and pair[1][0] <= pair[0][1]:
      count += 1

  return count

def main():
  file = readFile("input.txt")
  pairs = parsePairs(file)

  print(partOne(pairs))
  print(partTwo(pairs))

if __name__ == "__main__":
  main()