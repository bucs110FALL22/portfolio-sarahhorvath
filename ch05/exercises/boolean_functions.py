
def getGrade(percentage):
    letter = 'F'
    if percentage >= 90:
        letter = 'A'
    elif percentage >= 80:
        letter = 'B'
    elif percentage >= 70:
        letter = 'C'
    elif percentage >= 60:
        letter = 'D'
    return letter


def isPassing(letter):
    if letter == 'A': 
        return True
    elif letter == 'B':
        return True
    elif letter == 'C':
        return True
    return False

print(isPassing(getGrade(85)))
print(isPassing(getGrade(65)))
print(isPassing(getGrade(110)))
print(isPassing(getGrade(-1)))