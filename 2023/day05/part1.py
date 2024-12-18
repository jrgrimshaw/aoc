def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  sections = input.split("\n\n")

  seeds = [int(num) for num in sections[0].split(": ")[1].split(" ")]
  print('seeds', seeds)

  sources = seeds
  for i in range(len(sections) - 1):
    maps = create_maps(sections[i + 1])
    new_sources = []
    for source in sources:
      new_sources.append(destination_from_source(maps, source))
    sources = new_sources

  print('locations', sources)
  print('min location', min(sources))

# if source num falls in any source ranges, select its matching destination range
# else, source is the same as destination
def destination_from_source(maps, source):
  destination = False

  for map in maps:
    if source >= map[0][0] and source <= map[0][1]:
      diff = source - map[0][0]
      destination = map[1][0] + diff

  if not destination:
    destination = source

  return destination 

def create_maps(section):
  maps = []
  rows = section.split(":\n")[1].split("\n")

  for row in rows:
    nums = [int(num) for num in row.split(" ")]
    
    destination_range = [nums[0], nums[0] + nums[2] - 1]
    source_range = [nums[1], nums[1] + nums[2] - 1]

    maps.append([source_range, destination_range])

  return maps
  
if __name__ == '__main__':
  main()