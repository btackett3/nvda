def str_bin(s_str):
    st = s_str
    print(' '.join(format(ord(x), "b") for x in st))


def main():
    str_bin("lol")


if __name__ == "__main__":
    main()
    print("done")