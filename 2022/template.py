def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def main():
  file = readFile("input.txt")
  print(file)

if __name__ == "__main__":
  main()