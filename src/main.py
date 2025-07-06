from textnode import TextType, TextNode


def main():
    dummy = TextNode(
        "I am bold",
        TextType.BOLD,
        "https://www.charliej2005.github.io"
        )
    print("hello world")
    print(dummy)


if __name__ == "__main__":
    main()
