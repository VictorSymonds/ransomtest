This is a python code made in terminal where i generate batch scripting
automated actions.

# Preparations
You need to have Python installed

Install dependencies from requirements.txt:
'pip install -r requirements.txt'



In this project there are 3 files:

# ransomware.py:

|This file encrypts the files in the folder you choose

|You may execute it this way (Im using the included important files folder):

|'python ransomware.py "Important_Files/"'

|Following this, all the .txt files in your folder will have gibberish and random symbols in their contents, blocking whatever you had written before.

|It will also generate the encryption key so you can decrypt it later

# decryptor.py:

|This file decrypts the files in the folder you choose

|You may execute it this way (Im using the included important files folder):

|'python decryptor.py "Important_Files/" "<>"' (between the < and the opposite of it, add the encryption key)

|Following this, all the .txt files in your folder will return back to how there were before

# filegenerator.py

|This file generates a folder with 10 files containing info from your PC

|You may execute it this way:

|'python filegenerator.py'

