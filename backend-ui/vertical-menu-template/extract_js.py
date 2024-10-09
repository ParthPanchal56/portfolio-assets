import os

def extract_js_from_file(file_path):
    """Reads the content of a JS file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def scan_js_files(directories):
    """Scans for .js files in the specified directories."""
    js_contents = []
    
    # Iterate through the list of directories
    for directory_path in directories:
        # Walk through each directory to find JS files
        for root, _, files in os.walk(directory_path):
            for index, file in enumerate(files, start=1):
                if file.endswith('.js'):
                    file_path = os.path.join(root, file)
                    js_content = extract_js_from_file(file_path)
                    
                    if js_content:
                        js_contents.append((index, file, js_content))
    
    return js_contents

def write_js_contents_to_file(js_contents, output_file):
    """Writes the JS file contents to a specified output file."""
    with open(output_file, 'w', encoding='utf-8') as file:
        for index, file_name, js_content in js_contents:
            file.write(f"File Number - {index} - {file_name}\n")
            file.write("-" * 27 + "\n\n")
            file.write(js_content + "\n\n")
            file.write("-" * 27 + "\n")
            file.write("\n" * 10)  # 10 white spaces between entries

if __name__ == "__main__":
    # List of directories containing JS files
    directories = [
        r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\calendar",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\calendar\extensions",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\charts",

        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\charts\echarts",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\coming-soon",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\editors\quill",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\editors\quill\themes",

        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\editors\quill\ui",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\extensions",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\extended\maxlength",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\extended\typeahead",

        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\repeater",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\select",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\spinner",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\toggle",

        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\validation",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\media",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\miscellaneous",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\pagination",

        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\pickers\pickadate",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\tables\ag-grid",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\tables\datatable",
        # r"D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\ui",
        # r"D:\Portfolio\portfolio\UI\backend-ui\assets\js",
    ]
    
    # Output file path
    output_file = "js_app_assets_contents_3.txt"
    
    # Extract JS contents from all directories
    js_contents = scan_js_files(directories)
    
    # Write the JS contents to the output file
    write_js_contents_to_file(js_contents, output_file)
    
    print(f"JS contents have been extracted and written to {output_file}")







#     D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\core
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\core\libraries
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\ag-grid
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\cards
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\charts
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\charts\gmaps
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\datatables
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\editors
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\extensions
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\forms
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\forms\select
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\forms\validation
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\modal
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\navs
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\pages
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\pagination
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\pickers\dateTime
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\popover
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\tooltip
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\js\scripts\ui
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\calendar
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\calendar\extensions
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\charts
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\charts\echarts
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\coming-soon
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\editors\quill
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\editors\quill\themes
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\editors\quill\ui
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\extensions
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\extended\maxlength
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\extended\typeahead
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\repeater
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\select
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\spinner
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\toggle
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\forms\validation
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\media
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\miscellaneous
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\pagination
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\pickers\pickadate
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\tables\ag-grid
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\tables\datatable
# D:\Portfolio\portfolio\UI\backend-ui\app-assets\vendors\js\ui
# D:\Portfolio\portfolio\UI\backend-ui\assets\js
