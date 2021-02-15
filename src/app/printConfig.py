import win32print
import win32con


def config(printer_name):
    
    PRINTER_DEFAULTS = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
    pHandle = win32print.OpenPrinter(printer_name, PRINTER_DEFAULTS)
    properties = win32print.GetPrinter(pHandle, 2)
    pDevModeObj = properties["pDevMode"]
    pDevModeObj.PaperWidth = 200
    pDevModeObj.PaperLength = 100
    win32print.SetPrinter(pHandle, 2, properties, 0)
    win32print.ClosePrinter(pHandle)