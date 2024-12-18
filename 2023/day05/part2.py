def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()

def main():
  input = read_file()
  sections = input.split("\n\n")
  seeds = [int(num) for num in sections[0].split(": ")[1].split(" ")]
  seed_ranges = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]

  for i in range(len(sections) - 1):
    maps = create_maps(sections[i + 1])
    new_seed_ranges = []

    for seed_range in seed_ranges:
      new_seed_ranges += destination_from_source(maps, seed_range)
    
    seed_ranges = new_seed_ranges

  print(min(min(seed_ranges)))

def destination_from_source(maps, seed_range):
  destinations = []

  def search(range):
    start, end = range
    destination = False
    
    for map in maps:
      if start >= map[0][0] and start <= map[0][1] and end >= map[0][0] and end <= map[0][1]:
        diff = [start - map[0][0], end - map[0][0]]
        destination = [map[1][0] + diff[0], map[1][0] + diff[1]]        
      elif start >= map[0][0] and start <= map[0][1]:
        diff = start - map[0][0]
        destination = [map[1][0] + diff, map[1][1]]
        search([map[0][1] + 1, end])
      elif end >= map[0][0] and end <= map[0][1]:
        diff = end - map[0][0]
        destination = [map[1][0], map[1][0] + diff]
        search([start, map[0][0] - 1])

    if not destination:
      destination = [start, end]

    destinations.append(destination)

  search(seed_range)

  return destinations

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