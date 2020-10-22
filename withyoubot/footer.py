import datetime


def footer(message):
    utctime = datetime.datetime.utcnow()
    return message + str(utctime.strftime("%H%Mz")) + " | © Kolby Dunning"
