def xsandoslettercounter(message):
    xcount = 0  # line 2 - 5 counts the amount of Xs in the message
    for i in message:
        if i == 'x':
            xcount = xcount + 1
    ocount = 0  # Line 6 - 9 counts the amount of Os in the message
    for i in message:
        if i == 'o':
            ocount = ocount + 1
    xsandos = "Your message has", xcount, "Xs and", ocount, "Os"  # Prints no of Xs and Os there are in user's message
    xsandostrue = "Your message is true because", xsandos,
    xsandosfalse = "Your message is false because", xsandos
    if xcount == ocount:  # In line 13 - 14 if the number of Xs and Os are the same, the message is "true"
        return xsandostrue
    else:
        return xsandosfalse  # if the number of Xs and Os are different, the message is "false"


message = "xylophone"
print(xsandoslettercounter(message))

