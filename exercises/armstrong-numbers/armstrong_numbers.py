def is_armstrong_number(number):
    totalNumber = 0
    number_string = str(number)

    for i in range(0, len(number_string)):
        totalNumber += int(number_string[i]) ** len(number_string)

    return number == totalNumber