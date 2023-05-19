import requests
from bs4 import BeautifulSoup


def scrape_elements_by_class(url, target_class):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie s'il y a une erreur HTTP

        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(class_=target_class)
        extracted_data = [element.text for element in elements]
        return extracted_data

    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête HTTP :", str(e))
    except Exception as e:
        print("Erreur lors du scraping :", str(e))

try:
    url = input("URL de la page à scraper : ")
    class_name = input("Nom de la classe à cibler : ")
    extracted_elements = scrape_elements_by_class(url, class_name)
    print("Données extraites :")
    for element in extracted_elements:
        print(element)
        print("############################ \n")

except ValueError:
    print("Erreur : Veuillez fournir des entrées valides.")
