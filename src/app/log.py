from datetime import datetime


def writeLog(status, content):
    f = open('C:/FinBank/prints/log.txt', 'a')
    f.write(datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S') + " |\t" + status + "\t |\t" + content + "\n")
    f.close()
