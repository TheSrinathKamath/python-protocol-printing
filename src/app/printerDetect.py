import win32api
import win32print
import json


def getNetworkPrinter(sysName, pPrinterName):
    print('net')
    status = False
    v_printer_name = ''

    prnList = win32print.EnumPrinters(100, None, 2)
    printer_name = '\\\\' + sysName + '\\' + pPrinterName

    for x in range(len(prnList)):
        if (prnList[x].get('pPrinterName').lower() == printer_name.lower()):
            v_printer_name = prnList[x].get('pPrinterName')
            status = True
            break
    print(v_printer_name)
    return {"status": status, "v_printer_name": v_printer_name}


def getUSBPrinter(sysName, printer_name):
    print('usb')
    status = False
    v_printer_name = ''

    if (win32api.GetComputerName().lower() != sysName.lower()):
        return {"status": False, "v_printer_name": v_printer_name}

    all_printers = [printer[2] for printer in win32print.EnumPrinters(
        win32print.PRINTER_ENUM_LOCAL)]

    for x in range(len(all_printers)):

        if (printer_name.lower() == all_printers[x].lower()):
            v_printer_name = all_printers[x]
            status = True
            break

    return {"status": status, "v_printer_name": v_printer_name}
