def readFile(fileName):
  with open(fileName) as file:
    return file.read()

def partOne(matrix):
  count = 0

  for i, row in enumerate(matrix):
    for j, col in enumerate(row):
      if i == 0 or j == 0 or i == len(matrix)-1 or j == len(row)-1 :
        count += 1
      else:
        visible = True
        for r in range(i):
          if matrix[r][j] >= matrix[i][j]:
            visible = False
        if visible:
          count += 1
          continue;

        visible = True
        for r in range(len(matrix)-i-1):
          if matrix[r+i+1][j] >= matrix[i][j]:
            visible = False
        if visible:
          count += 1
          continue;

        visible = True
        for c in range(j):
          if matrix[i][c] >= matrix[i][j]:
            visible = False
        if visible:
          count += 1
          continue;

        visible = True
        for c in range(len(row)-j-1):
          if matrix[i][c+j+1] >= matrix[i][j]:
           visible = False
        if visible:
          count += 1
          continue;

  return count

def partTwo(matrix):
  scores = []

  for i, row in enumerate(matrix):
    for j, col in enumerate(row):

      north = 0
      south = 0

      if i > 0 and i < len(matrix)-1:
        for n in range(i-1, -1, -1):
          north += 1
          if matrix[n][j] >= matrix[i][j]:
            break;

        for s in range(i+1, len(matrix), 1):
          south += 1
          if matrix[s][j] >= matrix[i][j]:
            break;

      west = 0
      east = 0

      if j > 0 and j < len(row)-1:
        for w in range(j-1, -1, -1):
          west += 1
          if matrix[i][w] >= matrix[i][j]:
            break;

        for e in range(j+1, len(row), 1):
          east += 1
          if matrix[i][e] >= matrix[i][j]:
            break;

      scores.append(north * south * east * west)

  return max(scores)

def main():
  file = readFile("input.txt")

  # Build matrix
  matrix = []
  matrix = file.split("\n")
  for i,row in enumerate(matrix):
    matrix[i] = [int(x) for x in list(row)]

  print(partOne(matrix))
  print(partTwo(matrix))

if __name__ == "__main__":
  main()