# Printer Executable

### Software Dependency
```Adobe reader```

### Env Requirements
```Python 3 or above```

### Project Setup
```pip install -r src/requirements.txt```

### Project build
```python setup.py build```

### Project Demo
1) Download ```FinBank.rar```
2) Unzip directly to the ```C:/``` drive
3) Navigate to ```C:\FinBank\prints\application``` to find ```printer.reg```
4) Install the registry file
5) Open run or ```win key + R```
6) Execute ```pp20:system_name@@printer_name@@base64encoded_api_call```

### Demo Dependencies
1) Open ```fin-backend server```
2) Execute ```npm run printerServer```

### Debugging
Most of the time the error would be due to imporoper installation of protocol handler in the registry. Follow the methods shown below.

1) Open run or ```win key + R```
2) Execute regedit
3) Search for
```
HKEY_CURRENT_USER\Software\Classes\pp20
      (Default) = "URL:pp20"
      URL Protocol = ""
      DefaultIcon
         (Default) = "main.exe,1"
      shell
         open
            command
               (Default) = "C:\\FinBank\\prints\\application\\exe\\main.exe" "%1"
```
4) Delete this scheme
5) Open the ```printer.reg``` file in vscode and verify the paths in ```(Default)```
6) Make the changes to ```printer.reg``` and install again.

### Error logging

1) Navigate to ```C:\FinBank\prints```
2) Open ```log.txt``` - shows print job error
3) Open ```requests.txt``` - shows request apis and related printer

### References
Visit: https://stackoverflow.com/questions/7087728/custom-protocol-handler-in-chrome
