import os

# Get the directory path from the user (or use the current directory)
directory = input("Enter the directory path (leave empty for current directory): ") or "/"

# List the contents of the directory
try:
    contents = os.listdir(directory)
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")
