import functools

def read_file():
  with open('input.txt', encoding="utf-8") as f:
    return f.read()
  
def main():
  input = read_file()
  hands = [[hand.split(" ")[0], int(hand.split(" ")[1])] for hand in input.split("\n")]
  ranked_hands = []

  for [hand, bid] in hands:
    ranked_hands.append({"type": get_type_rank(hand), "hand": hand, "bid": bid})

  ranked_hands = sorted(ranked_hands, key=lambda d: d["type"])
  ranked_hands = sort_same_types(ranked_hands)

  total_winnings = 0
  for i in range(len(ranked_hands)):
    bid = ranked_hands[i]["bid"]
    total_winnings += bid * (i + 1)
    print(i + 1, ranked_hands[i])

  print(total_winnings)

def get_type_rank(hand):
  # five of a kind
  if five_of_kind(hand):
    return 7
  elif four_of_kind(hand):
    return 6
  elif full_house(hand):
    return 5
  elif three_of_kind(hand):
    return 4
  elif two_pair(hand):
    return 3
  elif one_pair(hand):
    return 2
  else:
    return 1
  
def better_hand_of_same_type(hand1, hand2):
  cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

  if not hand1 or not hand2:
    return 0
  
  for i in range(5):
    if hand1[i] != hand2[i]:
      if cards.index(hand1[i]) < cards.index(hand2[i]):
        return 1
      elif cards.index(hand1[i]) > cards.index(hand2[i]):
        return -1

def sort_same_types(ranked_hands):
  for passnum in range(len(ranked_hands)-1,0,-1):
    for i in range(passnum):
      if ranked_hands[i]["type"] == ranked_hands[i+1]["type"]:
        if better_hand_of_same_type(ranked_hands[i]["hand"], ranked_hands[i+1]["hand"]) == 1:
          temp = ranked_hands[i]
          ranked_hands[i] = ranked_hands[i+1]
          ranked_hands[i+1] = temp

  return ranked_hands
  
def make_hand_dict(hand):
  hand_dict = {}

  for i in range(len(hand)):
    if not hand[i] in hand_dict:
      hand_dict[hand[i]] = 0
    hand_dict[hand[i]] += 1

  hand_dict = dict(sorted(hand_dict.items(), key=functools.cmp_to_key(better_hand_of_same_type), reverse=True))
  hand_dict = dict(sorted(hand_dict.items(), key=lambda x: x[1], reverse=True))

  if "J" in hand_dict:
    for key in hand_dict:
      if key != "J":
        hand_dict[key] += hand_dict["J"]
        break
    
    if list(hand_dict.keys()) != ["J"]:
      hand_dict.pop("J")
  
  return list(sorted(hand_dict.values(), reverse=True))
  
def five_of_kind(hand):
  hand_dict = make_hand_dict(hand)
  return hand_dict[0] == 5

def four_of_kind(hand):
  hand_dict = make_hand_dict(hand)
  return hand_dict[0] == 4

def full_house(hand):
  hand_dict = make_hand_dict(hand)
  return hand_dict[0] == 3 and hand_dict[1] == 2

def three_of_kind(hand):
  hand_dict = make_hand_dict(hand)
  return hand_dict[0] == 3

def two_pair(hand):
  hand_dict = make_hand_dict(hand)
  return hand_dict[0] == 2 and hand_dict[1] == 2

def one_pair(hand):
  hand_dict = make_hand_dict(hand)
  return hand_dict[0] == 2
  
if __name__ == '__main__':
  main()