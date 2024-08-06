#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

def road_to_philosophy(page_title, pages_visited):
    """
    Recursive function that navigates through Wikipedia links starting from
    a given page title to find the path to the 'Philosophy' article.

    Args:
    - page_title (str): The initial page title to start the search from.
    - pages_visited (list): A list to keep track of visited page titles.

    Returns:
    - None: The function prints the path to 'Philosophy' in the terminal and stops.

    Raises:
    - sys.exit: If it encounters a dead end (no valid links), infinite loop (repeated page),
      or encounters a network error during requests.
    """
    URL = "https://en.wikipedia.org/wiki/" + page_title

    try:
        response = requests.get(URL, allow_redirects=True)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        page_title = soup.find(name="title").text.split(" - ")[0]
        all_links = soup.find(id="mw-content-text").select("p > a")

        if len(all_links) == 0:
            sys.exit("It leads to a dead end!")
        if page_title in pages_visited:
            sys.exit("It leads to an infinite loop!")
        if page_title == "Philosophy":
            print("Philosophy")
            return

        print(page_title)
        pages_visited.append(page_title)

        next_link = None
        for link in all_links:
            href_value = link.get('href', '')
            if href_value.startswith('/wiki/') and not (href_value.startswith('/wiki/Help:') or href_value.startswith('/wiki/Wikipedia:')):
                next_link = href_value
                break
        
        if not next_link:
            sys.exit("It leads to a dead end!")

        next_search_term = next_link.split('/')[-1]
        road_to_philosophy(next_search_term, pages_visited)

    except requests.exceptions.RequestException:
        sys.exit("It leads to a dead end!")

def main():
    """
    Main function that processes the command line argument and initiates the
    search for the path to 'Philosophy'.
    """
    if len(sys.argv) != 2:
        sys.exit("Pass in only one argument, use double quotes if necessary")
    
    initial_search_term = sys.argv[1].replace(' ', '_')
    pages_visited = []

    road_to_philosophy(initial_search_term, pages_visited)

    print(f"{len(pages_visited)} roads from {initial_search_term} to Philosophy")

if __name__ == "__main__":
    main()
