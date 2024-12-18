def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()

def collab_values(line):
  numbers_words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  
  data = {
    "start": "",
    "start_index": 99,
    "end": "",
    "end_index": -1
  }

  def search_char(char, data):
    index = line.find(char)
    if index > -1:
      if index <= data['start_index']:
        data['start'] = i
        data['start_index'] = index
    rindex = line.rfind(char)
    if rindex > -1:
      if rindex >= data['end_index']:
        data['end'] = i
        data['end_index'] = rindex
    return data

  for i in range(len(numbers_words)):
    data = search_char(numbers_words[i], data)

  for i in range(10):
    data = search_char(str(i), data)

  return str(data['start']), str(data['end'])

def main():
  input = read_file()
  lines = input.split("\n")

  total = 0
  for line in lines:
    if line:
      start, end = collab_values(line)
      print(line, start, end)
      total += int(start + end)

  print(total)
    
if __name__ == '__main__':
  main()