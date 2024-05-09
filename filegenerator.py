import os
import platform

def generate_system_info_files(folder_path):
	os.makedirs(folder_path, exist_ok=True)

	for i in range(10):
		file_name = f"system_info_{i+1}.txt"
		file_path = os.path.join(folder_path, file_name)
		with open(file_path, 'w') as f:
			f.write(f"System Information {i+1}\n")
			f.write(f"OS: {platform.system()}\n")
			f.write(f"OS Release: {platform.release()}\n")
			f.write(f"Machine: {platform.machine()}\n")
			f.write(f"Processor: {platform.processor()}\n")
			f.write(f"Python Version: {platform.python_version()}\n")

def main():
	folder_name = "system_info_folder"
	folder_path = os.path.join(os.getcwd(), folder_name)
	generate_system_info_files(folder_path)
	print(f"A folder containing very vital computering info has been generated in: {folder_path}")
	print(f"Surely nothing bad could happen to those files right?")

if __name__ == "__main__":
	main()
