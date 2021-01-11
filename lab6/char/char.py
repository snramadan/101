# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 06

def is_lower_101(char):
    if ord('a') <= ord(char) <= ord('z'):
        return True
    else:
        return False

def char_rot_13(char):
    if str.islower(char):
        if ord(char) <= ord('n'):
            return chr(ord(char) +13)
        else:
            return chr((ord(char) +13)%26)
    if str.isupper(char):
        if ord(char) >= ord('N'):
            return chr(ord(char) -13)
        else:
            return chr((ord(char) -13)%26)
