import cs50

# coin values in cents (greedy, largest to smallest)
COINS = (25, 10, 5, 1)


def get_cents() -> int:
    """Prompt until non-negative, then return whole cents."""
    while True:
        dollars = cs50.get_float("Change owed: ")
        if dollars is not None and dollars >= 0:
            # round to avoid 0.04 -> 3.999... issues
            return int(round(dollars * 100))


def main() -> None:
    cents = get_cents()

    coins = 0
    for coin in COINS:
        coins += cents // coin   # how many of this coin
        cents %= coin            # remainder after taking them

    print(coins)                 # print only the integer


if __name__ == "__main__":
    main()
