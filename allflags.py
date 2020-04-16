#!/usr/bin/python3

try:
    from colors import color
except ImportError:
    color = None

COLORS = ["White", "Black", "Green", "Red", "Blue", "Orange"]


def test_q1():
    done = set()
    for flag in make_flags("q1"):
        assert flag not in done
        assert flag[0] != flag[1], flag
        assert flag[1] != flag[2], flag
        done.add(flag)


def test_q2():
    done = set()
    for flag in make_flags("q2"):
        assert flag not in done
        assert flag[0] != flag[1], flag
        assert flag[0] != flag[2], flag
        assert flag[1] != flag[2], flag


def make_flags(mode):
    for first_color in COLORS:
        second_colors = list(COLORS)
        second_colors.remove(first_color)
        for second_color in second_colors:
            third_colors = list(COLORS)
            third_colors.remove(second_color)
            if mode == "q2":
                third_colors.remove(first_color)
            for third_color in third_colors:
                if color is None:
                    yield (first_color, second_color, third_color)
                else:
                    yield f"{color(' ',bg=first_color)}{color(' ', bg=second_color)}{color(' ', bg=third_color)} "


def main():
    """  We need a Python program that generates all the possible flags with 3
    colored stripes, see attachment.  The colors can be: White, Black, Green,
    Red, Blue, Green and Orange.

    Question 1: Please generate alle the possible flags. One color van not be
    the same in two stripes next to each other. So green, white, green is
    possible.

    Question 2: Please generate alle the possible flags. One color can only be
    used onces in a flag. So green, white, green is not good, but So green,
    white, blue is possible.

    Make a Python-program (for mathematic education) that makes this visable.
    We leave it to your creativity if it is possible to show the flags very
    small on the screen.

    It would be very nice if you can help us!

    Thanks in advance, Durk Jan de Bruin

    PS: Not all the flags exist in real countries. That is no problem """
    print("Q1")
    for flag in make_flags("q1"):
        print(flag, end=" ")
    print("\n\nQ2")
    for flag in make_flags("q2"):
        print(flag, end=" ")
    print("")


if __name__ == "__main__":
    main()
