from paulie.common.pauli_string_factory import get_pauli_string as p


def main():
    g = p(["XX", "YY", "ZZ", "ZY"])
    print(f"{g.get_algebra()} is {g.is_algebra('u(1)+2*su(2)')}")


if __name__ == "__main__":
    main()
