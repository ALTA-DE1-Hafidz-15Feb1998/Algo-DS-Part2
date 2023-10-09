def playing_domino(cards, deck):
    valid_cards = []

    for card in cards:
        if deck[0] in card or deck[1] in card:
            valid_cards.append(card)

    if not valid_cards:
        return valid_cards
    else:
        max_card = max(valid_cards, key=lambda x: x[0] + x[1])
        return max_card

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []