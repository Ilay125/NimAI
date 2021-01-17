import nim


def main():
    game = nim.Nim(13)
    isPlayer = True
    print(game.getMatches())
    while not game.isWinner():
        if isPlayer:
            game.updateMatches(int(input("Enter a number (1/2): ")))
        else:
            game.updateMatches(game.compMove())
        isPlayer = not isPlayer
        print(game.getMatches())

    if isPlayer:
        print("Player wins!")
    else:
        print("PC wins!")


main()