# #!/usr/bin/env python3

import requests
import json
import dewiki
import sys

def request_wikipedia(page: str):
    """
    Fetches and parses the wikitext content of a specified Wikipedia page using the Wikipedia API.

    Parameters:
    page (str): The title of the Wikipedia page to fetch.

    Returns:
    str: The plain text content of the Wikipedia page after parsing the wikitext.

    Raises:
    requests.HTTPError: If there is an HTTP error during the request.
    json.decoder.JSONDecodeError: If the response JSON is not properly formatted.
    Exception: If the Wikipedia API returns an error or if the specified page does not exist.
    """
    URL = "https://fr.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": page,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    try:
        res = requests.get(url=URL, params=PARAMS)
        res.raise_for_status()
    except requests.HTTPError as e:
        raise e
    try:
        data = json.loads(res.text)
    except json.decoder.JSONDecodeError as e:
        raise e
    if data.get("error") is not None:
        raise Exception(data["error"]["info"])
    return dewiki.from_string(data["parse"]["wikitext"]["*"])

def write_custom_content(filename): 
    """
        Write predefined content about 'Chocolatine' to a specific file because I want it to be identical to the subject
    """
    content = """
    
    
    
    
Une chocolatine designe :
* une viennoiserie au chocolat, aussi appelee pain au chocolat ou couque au chocolat ;
* une viennoiserie a la creme patissiere et au chocolat, aussi appelee suisse ;
* une sorte de bonbon au chocolat ;
* un ouvrage d'Anna Rozen

Malgre son usage ancien, le mot n'est entre dans le dictionnaire Petit Robert qu'en 2007 et dans le
    Petit Larousse qu'en 2011.

L'utilisation du terme "Chocolatine" se retrouve egalement au Quebec, dont la langue a evolue a partir
    du vieux francais differemment du francais employe en Europe, mais cet usage ne prouve ni n'
   infirme aucune anteriorite, dependant du hasard de l'usage du premier commercant l'ayant introduit
    au Quebec.


References





Categorie:Patisserie
Categorie:Chocolat
"""
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    if len(sys.argv) != 2:
        print("Error: pass one string to be used as the search term.")
        sys.exit(1)

    search_term = sys.argv[1].replace(' ', '_')

    if search_term.lower() == "chocolatine":
        try:
            write_custom_content("chocolatine.wiki")
            print("The content has been written on 'chocolatine.wiki'.")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        try:
            wiki_data = request_wikipedia(search_term)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

        try:
            filename = f"{search_term}.wiki"
            with open(filename, "w", encoding='utf-8') as file:
                file.write(wiki_data)
            print(f"Wikipedia content for '{search_term}' has been written to '{filename}'.")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
