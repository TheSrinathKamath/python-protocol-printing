from base64 import b64decode
from log import writeLog


def createPdf(b64):
    tempFile = 'C:\\FinBank\\prints\\temp\\temp.pdf'
    try:
        bytes = b64decode(b64, validate=True)

        if bytes[0:4] != b'%PDF':
            writeLog('Forbidden', 'Missing the PDF file signature')
            raise ValueError('Missing the PDF file signature')

        f = open(tempFile, 'wb')
        f.write(bytes)
        f.close()
    except:
        writeLog('Failed', 'Error creating PDF')
