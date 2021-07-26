class PhoneNumber:
    def __init__(self, number):

        # Remove non-digit characters from string
        number = ''.join(x for x in number if x.isdigit())

        # Raise an error if phone number is not of length 10 or 11
        if len(number) < 10 or len(number) > 11:
            raise ValueError("Invalid phone number")

        if len(number) == 11:
            # Removes first number if it is a 1
            if number[0] in "1":
                number = number[1:]
            # Raise an error otherwise
            else:
                raise ValueError("Invalid phone number")
        # Raise an error if the area code or exchange code start with 0 or 1
        if number[0] in ["0", "1"] or number[3] in ["0", "1"]:
            raise ValueError("Invalid phone number")

        self.number = number
        self.area_code = self.number[:3]

    # Return pretty number function
    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
