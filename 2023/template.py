def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  print("input is", input)
  
if __name__ == '__main__':
  main()