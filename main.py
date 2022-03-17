from google_images_download import google_images_download
import unidecode
import json

response = google_images_download.googleimagesdownload()
path = './data/ingredients.json'
search_queries = []


def read_file_json(path):
    ingredientsNames = []
    f = open(path)
    data = json.load(f)

    for i in data:
        if type(list(i.values())[0]) is str:
            ingredientsNames.append(unidecode.unidecode(list(i.values())[0]))
    return ingredientsNames


def download_images(query):
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 5,
                 "print_urls": False,
                 "size": "medium",
                 "aspect_ratio": "panoramic"}

    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 5,
                     "print_urls": False,
                     "size": "medium"}

        try:
            response.download(arguments)
        except:
            pass


def main():
    search_queries = read_file_json(path)
    for query in search_queries:
        download_images(query)
        print()


if __name__ == "__main__":
    main()
