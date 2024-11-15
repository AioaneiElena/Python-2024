import os
import sys

def rename_files(dir_path):
    try:
        if not os.path.isdir(dir_path):
            raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")

        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

        if not files:
            print(f"No files found in directory '{dir_path}'.")
            return
        # Rename files
        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(dir_path, filename)
            new_filename = f"file{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(dir_path, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except (IOError, OSError) as e:
                print(f"Failed to rename '{filename}': {e}")

    except Exception as e:
        print(f"Other file issues: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
    else:
        dir_path = sys.argv[1]
        rename_files(dir_path)

#python rename.py ex2