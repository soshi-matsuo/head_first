from collections import Counter

def is_straight_flush(hands):
    return is_flush(hands) and is_straight(hands) 

def is_flush(hands):
    i = 0
    while i < len(hands) - 1:
        if hands[i][1] != hands[i+1][1]:
            return False
        i += 1
    
    return True

def is_straight(hands):
    sorted_hand = sorted([int(hand[0]) for hand in hands])

    j = 0
    while j < len(sorted_hand) -1:
        if sorted_hand[j] != sorted_hand[j+1] - 1:
            return False
        j += 1
    return True

def is_four_card(hands):
    hands_num = [hand[0] for hand in hands]
    c = Counter(hands_num)
    return max(c.values()) == 4