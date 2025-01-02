import requests

def view_website(url: str):
    response = requests.get(f"https://r.jina.ai/{url}")
    
    if response.status_code == 200:
        data = response.text
        return str(data)
        # print(data)
    
    return f"Failed to retrieve data: {response.status_code}"