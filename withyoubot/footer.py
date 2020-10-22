import datetime


def footer(message):
    utctime = datetime.datetime.utcnow()
    return message + str(utctime) + " | © Kolby Dunning"
