MAX_X = 500
MAX_Y = 500


def circleOne(x, y, clearance):
    if ((x - 0) ** 2 + (y - 0) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def circleTwo(x, y, clearance):
    if ((x - (-200)) ** 2 + (y - (-300)) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def circleThree(x, y, clearance):
    if ((x - 200) ** 2 + (y - (-300)) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def circleFour(x, y, clearance):
    if ((x - 200) ** 2 + (y - 300) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def squareOne(x, y, clearance):
    if (y >= -75 - clearance) and (y <= 75 + clearance) and (x >= -475 - clearance) and (x <= -325 + clearance):
        return False
    else:
        return True


def squareTwo(x, y, clearance):
    if (y >= -75 - clearance) and (y <= 75 + clearance) and (x >= 325 - clearance) and (x <= 475 + clearance):
        return False
    else:
        return True


def squareThree(x, y, clearance):
    if (y >= 225 - clearance) and (y <= 375 + clearance) and (x >= -275 - clearance) and (x <= -125 + clearance):
        return False
    else:
        return True


def isValidStep(position, clearance):
    x = position[0]
    y = position[1]
    if circleOne(x, y, clearance) and circleTwo(x, y, clearance) and circleThree(x, y, clearance) and circleFour(x, y,
                                                                                                                 clearance) and squareOne(
        x, y, clearance) and squareTwo(x, y, clearance) and squareThree(x, y, clearance):
        return True
    else:
        return False
