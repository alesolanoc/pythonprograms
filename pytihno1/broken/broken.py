import requests

def check_broken_links(url):
    """
    Check for broken links in a webpage.

    Args:
        url (str): The URL of the webpage to check.

    Returns:
        list: A list of broken links found in the webpage.
    """
    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get all the links in the webpage
        links = extract_links(response.text)

        # Check each link for validity
        broken_links = []
        for link in links:
            if not is_valid_link(link):
                broken_links.append(link)

        return broken_links
    else:
        # Return an empty list if the request was not successful
        return []

def extract_links(html):
    """
    Extract all links from an HTML document.

    Args:
        html (str): The HTML document.

    Returns:
        list: A list of links found in the HTML document.
    """
    # Use a regular expression to find all links in the HTML document
    # This regex pattern matches the href attribute of an anchor tag
    pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
    links = re.findall(pattern, html)

    return links

def is_valid_link(link):
    """
    Check if a link is valid.

    Args:
        link (str): The link to check.

    Returns:
        bool: True if the link is valid, False otherwise.
    """
    # Send a HEAD request to the link to check if it is valid
    response = requests.head(link)

    # Check if the request was successful and the status code is not 404
    if response.status_code == 200:
        return True
    else:
        return False

# Example usage
webpage_url = "https://example.com"
broken_links = check_broken_links(webpage_url)
print("Broken links found:")
for link in broken_links:
    print(link)
