

def ones(ones_digit) -> str:
    ones_names = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }
    return ones_names[ones_digit]


def tens(tens_digit) -> str:
    tens_names = {
        "1": " x ",
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety",
    }
    return tens_names[tens_digit]


def hundreds(hundreds_digit) -> str:
    hundreds_name = ones(hundreds_digit) + "hundred and "
    return hundreds_name


def number_with_text():
    number_str = input("Enter a 3 digit number ")
    result_number_with_text = (
        hundreds(number_str[0])
        + tens(number_str[1])
        + ones(number_str[2])
    )
    print(result_number_with_text)


if  __name__ == "__main__":
    number_with_text()
