import win32print
import win32api
from log import writeLog
from printConfig import config
status = False
state = 'Error occured!'


def printFile(filename, printer_name):
    try:
        # print(filename)
        win32api.ShellExecute(
            0,
            "print",
            filename,
            '/d:"%s"' % win32print.OpenPrinter(printer_name),
            ".",
            0
        )
        status = "Success"
        state = filename

    except:
        status = 'Error occured!'
        state = 'Job failed'

    finally:
        writeLog(status, state)