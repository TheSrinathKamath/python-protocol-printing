import requests
import base64

# url = 'http://localhost:5000/jobs/printPdf/1/transactions/10-11-2020/490'


def getPDF(b64url, docExt):

    # token to mapped either with printer name or saved on windows as txt
    token = 'secretToken'

    base64_bytes = b64url.encode('ascii')
    url_bytes = base64.b64decode(base64_bytes)
    URL = url_bytes.decode('ascii') + "/" + token
    print(URL+'/'+docExt)
    r = requests.get(URL+'/'+docExt, stream=True)
    print(r.content)
    with open('C:/FinBank/prints/temp/temp.' + docExt, 'wb') as f:
        f.write(r.content)
        print('in')
    f.close()
