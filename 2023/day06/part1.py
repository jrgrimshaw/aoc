def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  rows = [row.split(":")[1] for row in input.split("\n")]
  times = [int(num) for num in list(filter(bool, rows[0].split(" ")))]
  distances = [int(num) for num in list(filter(bool, rows[1].split(" ")))]

  race_wins = 0

  # races
  for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    speed, wins = 0, 0
    while speed <= time:
      travel_dist = speed * (time - speed)

      if travel_dist > distance:
        wins += 1

      speed += 1

    if race_wins == 0:
      race_wins = wins
    else:
      race_wins *= wins

    print('race', i + 1, 'time', time, 'distance', distance, 'wins', wins)
    
  print(race_wins)

if __name__ == '__main__':
  main()