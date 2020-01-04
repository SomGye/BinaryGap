"""
Maxwell Crawford 2020-01-03
1. Binary Gap
    a. need to return LONGEST binary gap only (can be first, mid, or last)
    b. return 0 if none (if all 0, or 1111..., or 1000..)
    c. input is a whole integer in 1 -> intmax range
"""


def main():
    n = input("Enter an integer N>0: ")
    try:
        if int(n):
            result = binary_gap(int(n))
            return result
        else:
            print("Error: Must be a valid integer!")
            return 0
    except ValueError:
        return 0


def binary_gap(n):
    """
    For a valid integer n, get the longest binary gap between 1's.
    If none, return 0.
    :param n: valid integer > 0.
    :return:
    """
    if n < 1:
        return 0
    else:
        binary_str = "{0:b}".format(n)
        current_gap = 0
        longest_gap = current_gap
        seen_gap = False
        last_bit = len(binary_str)
        for i in range(last_bit):
            prev_bit = int(binary_str[i - 1])
            current_bit = int(binary_str[i])
            # When 1 is hit, check that previous was 0, triggering a gap.
            # Ignore the first bit in the sequence.
            if current_bit == 1 \
                    and prev_bit == 0 \
                    and i > 0:
                seen_gap = True  # flag
                current_gap = 0  # reset
            # Don't trigger gap on last bit
            elif i < (last_bit - 1):
                # Iterate after first bit
                if i > 0:
                    current_gap += 1
                if current_gap > longest_gap:
                    longest_gap = current_gap  # set max
        if seen_gap:
            return longest_gap
        else:
            return 0


if __name__ == '__main__':
    main()
