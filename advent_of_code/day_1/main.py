def getNumberFromSubString(string):
    if string[0:1:1].isdigit():
        return string[0:1:1]
    else:
        for numberWord in numberWords:
            if string[0:len(numberWord):1] == numberWord:
                return str(numberWords.index(numberWord))
    return None

def get_calibration_value_from_string(string):
    first_digit = None
    last_digit = None
    counter = 0
    for char in string:
        number = getNumberFromSubString(string[counter:len(string):1])
        if number is not None:
            if first_digit is None:
                first_digit = number
            else:
                last_digit = number
        counter += 1
    if last_digit is None:
        last_digit = first_digit
    return int(first_digit + last_digit)

if __name__ == '__main__':
    numberWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    file = open("input.txt", "r")
    total = 0
    for string in file:
        total += get_calibration_value_from_string(string)
    print(total)
