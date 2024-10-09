import os

def extract_css_from_file(file_path):
    # Read the content of the CSS file
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def scan_css_files(directories):
    css_contents = []
    
    # Iterate through the list of directories
    for directory_path in directories:
        # Walk through each directory to find CSS files
        for root, _, files in os.walk(directory_path):
            for index, file in enumerate(files, start=1):
                if file.endswith('.css'):
                    file_path = os.path.join(root, file)
                    css_content = extract_css_from_file(file_path)
                    
                    if css_content:
                        css_contents.append((index, file, css_content))
    
    return css_contents

def write_css_contents_to_file(css_contents, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for index, file_name, css_content in css_contents:
            file.write(f"File Number - {index} - {file_name}\n")
            file.write("-" * 27 + "\n\n")
            file.write(css_content + "\n\n")
            file.write("-" * 27 + "\n")
            file.write("\n" * 10)  # 10 white spaces between entries

if __name__ == "__main__":
    # List of directories containing CSS files
    directories = [
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\core\colors",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\core\menu\menu-types",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\core\mixins",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\pages",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\animate",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\calendars",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\extensions",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\file-uploaders",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\forms\extended",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\forms\validation",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\forms",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\loaders\animations",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\loaders",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\pickers",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\tour",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\plugins\ui",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css\themes",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\css",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\animate",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\calendars\extensions",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\calendars",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\charts",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\editors\quill",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\extensions",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\file-uploaders",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\forms\select",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\forms\spinner",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\forms\toggle",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\modal",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\perfect-scrollbar",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\pickers\pickadate",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\tables\ag-grid",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\tables\datatable\extensions",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\tables\datatable",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\ui",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css\weather-icons",
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\css",
    ]
    
    # Output file path
    output_file = "css_app_assets_vendor_contents.txt"
    
    # Extract CSS contents from all directories
    css_contents = scan_css_files(directories)
    
    # Write the CSS contents to the output file
    write_css_contents_to_file(css_contents, output_file)
    
    print(f"CSS contents have been extracted and written to {output_file}")
