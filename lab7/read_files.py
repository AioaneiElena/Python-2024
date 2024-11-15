import os
import sys

def read_files(dir_path, file_ext):
    try:
        if not os.path.isdir(dir_path):
            raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
        if not file_ext.startswith("."):
            raise ValueError("File extension should start with a '.' .")

        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                if file_name.endswith(file_ext):
                    file_path = os.path.join(root, file_name)
                    try:
                        with open(file_path, 'r') as file:
                            print(f"\nContents of {file_path}:")
                            print(file.read())
                    except Exception as e:
                        print(f"Error reading file '{file_path}': {e}")

    except Exception as e:
        print(f"Other file issues: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid arguments")
    else:
        dir_path = sys.argv[1]
        file_ext = sys.argv[2]
        read_files(dir_path, file_ext)

# python read_files.py ex1 .txt