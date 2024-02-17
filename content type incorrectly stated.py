import requests
from mimetypes import guess_type

def check_content_type(url):
    
    response = requests.get(url)
    response.raise_for_status()  
        
    content_type_header = response.headers.get('Content-Type', '')
        
    actual_content_type, _ = guess_type(url)
    actual_content_type = actual_content_type or 'application/octet-stream' or 'text/html'
        
    if content_type_header.lower() == actual_content_type.lower():
        return content_type_header, "Matched"
    else:
        return content_type_header, "Not Matched"
    
url_to_check = input("Enter the URL to check: ")
content_type, match_status = check_content_type(url_to_check)
if content_type is not None:
    print(f"Content-Type of the URL: {content_type}")
    print(f"Content-Type header matches with the content of the URL: {match_status}")
else:
    print(f"Error occurred while checking the URL: {match_status}")
