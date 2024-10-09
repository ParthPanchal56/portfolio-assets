import os
from bs4 import BeautifulSoup

def extract_body_from_html(file_path):
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract the body content without <script> tags
        body = soup.body
        if body:
            # Remove all <script> tags from the body
            for script in body.find_all('script'):
                script.decompose()
            return body.prettify()
    return None

def scan_html_files(directory_path):
    body_contents = []
    
    # Walk through the directory to find HTML files
    for root, _, files in os.walk(directory_path):
        for index, file in enumerate(files, start=1):
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                body_content = extract_body_from_html(file_path)
                
                if body_content:
                    body_contents.append((index, file, body_content))
    
    return body_contents

def write_body_contents_to_file(body_contents, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for index, file_name, body_content in body_contents:
            file.write(f"File Number - {index} - {file_name}\n")
            file.write("-" * 27 + "\n\n")
            file.write(body_content + "\n\n")
            file.write("-" * 27 + "\n")
            file.write("\n" * 10)  # 10 white spaces between entries

if __name__ == "__main__":
    # Directory containing HTML files
    directory_path = "D:/Portfolio/portfolio/UI/backend-ui/vertical-menu-template"
    
    # Output file path
    output_file = "body_contents.txt"
    
    # Extract body contents from all HTML files
    body_contents = scan_html_files(directory_path)
    
    # Write the body contents to the output file
    write_body_contents_to_file(body_contents, output_file)
    
    print(f"Body contents have been extracted and written to {output_file}")
