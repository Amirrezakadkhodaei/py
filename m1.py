def greet(name):
    """Print a friendly greeting."""
    print(f"Hi, {name}!")


def main():
    name = input("Enter your name: ").strip()

    if not name:
        print("You didn't enter a name.")
        return

    greet(name)


if __name__ == "__main__":
    main()
