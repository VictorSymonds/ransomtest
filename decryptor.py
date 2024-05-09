import sys
import os
from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
	with open(file_path, 'rb') as f:
		encrypted_data = f.read()
	fernet = Fernet(key)
	decrypted_data = fernet.decrypt(encrypted_data)
	with open(file_path, 'wb') as f:
		f.write(decrypted_data)
	print(f"File decrypted: {file_path}")

def main():
	if len(sys.argv) != 3:
		print("Usage: python decryptor.py <folder_path> <decryption_key>")
		sys.exit(1)

	folder_path = sys.argv[1]
	key = sys.argv[2]

	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			decrypt_file(file_path, key)

	print("Your files have been decrypted")

if __name__ == "__main__":
	main()
