# QR_code-generator
Generates QR code for any given input.

**** Design Considerations ****
Simple flask application which takes input from user and returns a QR code by making an async call to get the response. 


**** Steps to follow ****
Please follow the below steps to launch this flask application. 

1. Install python3 
2. Install pip
3. In case pip isn't installed , please install get-pip.py from https://bootstrap.pypa.io/get-pip.py. 
4. python get-pip.py
5. pip install virtualenv <name>
6. cd <name> 
7. source bin/activate
7. pip install -r requirements.txt
8. pip install "Flask[async]" (this step is really important to use flask in async manner) 
9. python3 QR_code_generator.py

Your application is will be up @ localhost:8888

