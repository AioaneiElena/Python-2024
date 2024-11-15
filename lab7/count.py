import os
import sys
from collections import defaultdict

def count_files(dir_path):
    try:
        if not os.path.isdir(dir_path):
            raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")

        extension_count = defaultdict(int)
        files_found = False

        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            if os.path.isfile(file_path):
                files_found = True
                _, ext = os.path.splitext(file_name)
                ext = ext if ext else "[no ext]"
                extension_count[ext] += 1

        if not files_found:
            print(f"No files found in directory.")
            return

        print(f"File counts by ext in '{dir_path}':")
        for ext, count in extension_count.items():
            print(f"Extension '{ext}': {count} file(s)")

    except PermissionError:
        print(f"Permission denied: Cannot access directory '{dir_path}'.")
    except Exception as e:
        print(f"Other file issues: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
    else:
        dir_path = sys.argv[1]
        count_files(dir_path)

# python count.py ex1
# python count.py