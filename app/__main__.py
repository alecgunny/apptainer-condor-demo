import argparse


def greet():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    print(f"Hello {args.name}")


if __name__ == "__main__":
    greet()
