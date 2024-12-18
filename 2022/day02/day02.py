def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def decryptAction(action):
  if action == "A" or action == "X": return "Rock"
  if action == "B" or action == "Y": return "Paper"
  if action == "C" or action == "Z": return "Scissors"

def getActionScore(action):
  if action == "Rock": return 1
  if action == "Paper": return 2
  if action == "Scissors": return 3

def getOutcomeScore(outcome):
  if outcome == "Z": return 6
  if outcome == "Y": return 3
  if outcome == "X": return 0

def getRoundOutcome(round):
  [opponent, player] = round

  if opponent == "Rock" and player == "Paper": return "Z"
  if opponent == "Paper" and player == "Scissors": return "Z"
  if opponent == "Scissors" and player == "Rock": return "Z"
  if opponent == player: return "Y"

  return "X"

def getAction(opponent, outcome):
  if outcome == "Z":
    if opponent == "Rock": return "Paper"
    if opponent == "Paper": return "Scissors"
    if opponent == "Scissors": return "Rock"
  elif outcome == "X":
    if opponent == "Rock": return "Scissors"
    if opponent == "Paper": return "Rock"
    if opponent == "Scissors": return "Paper"
  else:
    return opponent

def partOne(rounds):
  score = 0

  for round in rounds:
    opponent = decryptAction(round[0])
    player = decryptAction(round[1])

    score += getOutcomeScore(getRoundOutcome([opponent, player]))
    score += getActionScore(player)

  return score

def partTwo(rounds):
  score = 0

  for round in rounds:
    opponent = decryptAction(round[0])
    outcome = round[1]

    score += getActionScore(getAction(opponent, outcome))
    score += getOutcomeScore(outcome)

  return score

def main():
  input = readFile("input.txt")
  rounds = input.split("\n")
  for i, round in enumerate(rounds): rounds[i] = round.split(" ")

  print(partOne(rounds)) # part one
  print(partTwo(rounds)) # part two

if __name__ == "__main__":
  main()