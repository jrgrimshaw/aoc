import re

def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def findPacketMarker(buff, uniqueChars):
  for i in range(len(buff)):
    if i >= 3:
      lastFour = buff[i-uniqueChars:i]
      if re.search(r'^(?!.*(.).*\1)[A-Za-z0-9]+$', lastFour):
        return i

def main():
  buff = readFile("input.txt")
  
  print(findPacketMarker(buff, 4)) #part1
  print(findPacketMarker(buff, 14)) #part2

if __name__ == "__main__":
  main()