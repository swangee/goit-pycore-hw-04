import cats


def main():
    cats_info = cats.get_cats_info("cats.txt")
    print(cats_info)


if __name__ == "__main__":
    main()