import os

def extract_json_from_file(file_path):
    # Read the content of the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def scan_json_files(directories):
    json_contents = []
    
    # Iterate through the list of directories
    for directory_path in directories:
        # Walk through each directory to find JSON files
        for root, _, files in os.walk(directory_path):
            for index, file in enumerate(files, start=1):
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    json_content = extract_json_from_file(file_path)
                    
                    if json_content:
                        json_contents.append((index, file, json_content))
    
    return json_contents

def write_json_contents_to_file(json_contents, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for index, file_name, json_content in json_contents:
            file.write(f"File Number - {index} - {file_name}\n")
            file.write("-" * 27 + "\n\n")
            file.write(json_content + "\n\n")
            file.write("-" * 27 + "\n")
            file.write("\n" * 10)  # 10 white spaces between entries

if __name__ == "__main__":
    # List of directories containing JSON files
    directories = [
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\data",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\json",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\config",
        # Add more directories as needed...
    ]
    
    # Output file path
    output_file = "json_contents.txt"
    
    # Extract JSON contents from all directories
    json_contents = scan_json_files(directories)
    
    # Write the JSON contents to the output file
    write_json_contents_to_file(json_contents, output_file)
    
    print(f"JSON contents have been extracted and written to {output_file}")
