def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def parseFile(file):
  split = file.split("\n\n")
  rawStacks = split[0].split("\n")[:-1]
  instructions = split[1].split("\n")

  for i, stack in enumerate(rawStacks):
    rawStacks[i] = list(filter(None, stack.replace("    ", " - ").split(" ")))

  stacks = []
  for i in range(len(rawStacks[0])):
    stacks.append([])
    for item in rawStacks:
      if item[i] != "-": stacks[i].append(item[i][1])

  return stacks, instructions

def createMsg(stacks):
  msg = ""
  for stack in stacks:
    msg += stack[0]

  return msg

def partOne(stacks, instructions):
  s = list(stacks)

  for instruction in instructions:
    i = instruction.split(" ")

    count = int(i[1])
    moveFrom = int(i[3]) - 1
    moveTo = int(i[5]) - 1
    
    toMove = s[moveFrom][(count-1)::-1]
    s[moveFrom] = s[moveFrom][count:]
    s[moveTo] = toMove + s[moveTo]

  return createMsg(s)

def partTwo(stacks, instructions):
  s = list(stacks)

  for instruction in instructions:
    i = instruction.split(" ")

    count = int(i[1])
    moveFrom = int(i[3]) - 1
    moveTo = int(i[5]) - 1
    
    toMove = s[moveFrom][:count]
    s[moveFrom] = s[moveFrom][count:]
    s[moveTo] = toMove + s[moveTo]

  return createMsg(s)

def main():
  file = readFile("input.txt")
  
  stacks, instructions = parseFile(file)

  print(partOne(stacks, instructions))
  print(partTwo(stacks, instructions))

if __name__ == "__main__":
  main()