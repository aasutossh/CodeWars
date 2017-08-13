def validate_pin(pin):
    """[ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
        but exactly 4 digits or exactly 6 digits.

        If the function is passed a valid PIN string, return true, else return false.

        eg:

        validate_pin("1234") == True
        validate_pin("12345") == False
        validate_pin("a234") == False
    """ 
    if len(pin) == 4 or len(pin) == 6:
        try:
            int(pin)
            return True
        except ValueError:
            return False
        
    else:
        return False