import os
from bs4 import BeautifulSoup

def extract_links_from_html(file_path):
    css_links = set()
    js_links = set()
    
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all <link> tags for CSS files
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                css_links.add(href)
        
        # Find all <script> tags for JavaScript files
        for script in soup.find_all('script', src=True):
            src = script.get('src')
            if src:
                js_links.add(src)
    
    return css_links, js_links

def scan_html_files(directory_path):
    all_css_links = set()
    all_js_links = set()
    
    # Walk through the directory to find HTML files
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                css_links, js_links = extract_links_from_html(file_path)
                
                # Update the sets with new links
                all_css_links.update(css_links)
                all_js_links.update(js_links)
    
    return all_css_links, all_js_links

def write_links_to_file(css_links, js_links, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("<head>\n")
        
        # Write CSS links
        file.write("    <!-- CSS Links -->\n")
        for link in sorted(css_links):
            file.write(f'    <link rel="stylesheet" href="{link}">\n')
        
        # Write JavaScript links
        file.write("\n    <!-- JavaScript Links -->\n")
        for link in sorted(js_links):
            file.write(f'    <script src="{link}"></script>\n')
        
        file.write("</head>\n")

if __name__ == "__main__":
    # Directory containing HTML files
    directory_path = "D:/Portfolio/portfolio/UI/backend-ui/vertical-menu-template"
    
    # Output file path
    output_file = "output_links.txt"
    
    # Extract all CSS and JS links
    css_links, js_links = scan_html_files(directory_path)
    
    # Write the links to the output file
    write_links_to_file(css_links, js_links, output_file)
    
    print(f"Links have been extracted and written to {output_file}")
