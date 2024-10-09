import os

def find_js_directories(parent_directory):
    js_directories = set()
    
    # Walk through the directory to find .js files
    for root, _, files in os.walk(parent_directory):
        for file in files:
            if file.endswith('.js'):
                js_directories.add(root)
    
    return sorted(js_directories)

if __name__ == "__main__":
    # Parent directory containing JS files
    parent_directory = r"D:\Portfolio\portfolio\UI\backend-ui"
    
    # Find all directories containing .js files
    js_directories = find_js_directories(parent_directory)
    
    # Print each directory path
    for directory in js_directories:
        print(directory)
