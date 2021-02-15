from argSanitise import sanitise
from printerDetect import getUSBPrinter, getNetworkPrinter
from printConfig import config
from printJob import printFile
from URLPrint import getPDF
from errors import getError
import sys

if __name__ == "__main__":
    req = open('C:\\FinBank\\prints\\requests.txt', "a")
    try:
        args = sys.argv[1].split(":")
        argArray = args[1].split("@@")
        sysName = sanitise(argArray[0])
        printerName = sanitise(argArray[1])
        urlArr = argArray[2].split("~~~")
        url = urlArr[0]
        docArr = args[1].split("~~~")
        print(url)
        docType = docArr[1]
        docExt = 'pdf'

        if docType == 'html':
            docExt = 'html'

        getPDF(url, docExt)
        # print(getError(printerName))

        pdfPath = 'C:\\FinBank\\prints\\temp\\temp.' + docExt
        print(pdfPath)
        v_printer = getUSBPrinter(sysName, printerName)
        # print(v_printer)

        if(v_printer["status"]):
            printFile(pdfPath, v_printer["v_printer_name"])
        else:
            v_printer = getNetworkPrinter(sysName, printerName)

            if(v_printer["status"]):
                # print(v_printer)
                printFile(pdfPath, v_printer["v_printer_name"])
    except:
        req.write('error')
    finally:
        req.write('\n' + url + "\t" + v_printer["v_printer_name"])
        req.close()
