def is_valid_roman_numeral(r_num: str) -> bool:
    """
    Check if input string is a correct r numeral
    """
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if any(numeral not in roman_to_int for numeral in r_num):
        return False

    if "VV" in r_num or "LL" in r_num or "DD" in r_num:
        return False

    invalid_subtractions = ["IL", "IC", "ID", "IM", "XD", "XM", "VX", "VL", "VC", "VD", "VM", "LC", "LD", "LM"]
    for seq in invalid_subtractions:
        if seq in r_num:
            return False

    # check for correct order
    prev_value = 0
    for numeral in reversed(r_num):
        value = roman_to_int[numeral]
        if value < prev_value:
            if prev_value > value * 10:
                return False
        prev_value = value

    return True


def roman2int(r_num: str) -> int:
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    prev_value = 0

    for numeral in reversed(r_num):
        current_value = roman_to_int[numeral]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total


def main():
    while True:
        roman_numeral = input("enter r numeral")
        if roman_numeral.lower() == 'exit':
            break
        if not is_valid_roman_numeral(roman_numeral):
            print("invalid r numeral. try again")
        else:
            result = roman2int(roman_numeral)
            print(f'int value of r numeral {roman_numeral} is {result}.')


if __name__ == "__main__":
    main()

