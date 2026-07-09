from cs50 import get_int


def draw(symbol: str, count: int) -> None:
    """Print `symbol` repeated `count` times without a newline."""
    print(symbol * count, end="")


def main():
    # prompt for height between 1 and 8 inclusive
    while True:
        height = get_int("Height: ")
        if 1 <= height <= 8:
            break

    # left-aligned half-pyramid (no gap, no right side)
    for i in range(height):
        draw(" ", height - i - 1)  # leading spaces
        draw("#", i + 1)          # hashes
        print()                    # newline


if __name__ == "__main__":
    main()
