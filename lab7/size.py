import os
import sys

def calc_size(dir_path):
    total_size = 0
    try:
        if not os.path.isdir(dir_path):
            raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")

        for root, _, files in os.walk(dir_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    total_size += os.path.getsize(file_path)
                except (OSError, IOError) as e:
                    print(f"Error accessing file '{file_path}': {e}")

        print(f"Total size of all files in '{dir_path}': {total_size} bytes")

    except Exception as e:
        print(f"Other file issues: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments.")
    else:
        dir_path = sys.argv[1]
        calc_size(dir_path)

#python size.py ex2