from typing import Final
import requests

API_KEY: Final[str] = 'f6cd15dfe77c5c589aa34880b265850465431'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten_link(full_link: str):

    # We will send the payload to the server
    payload: dict = {'key': API_KEY, 'short': full_link}

    # We will get the response of server and assign it to request variable
    request = requests.get(BASE_URL, params=payload)

    # The response is json, so we turn it into dictionary and out it into data.
    data: dict = request.json()

    # Walrus operator: Assigns data.get('url') to url_data and then if the value is not empty or false it continues.
    if url_data := data.get('url'):

        # You can learn more about these codes at: https://cutt.ly/api-documentation/regular-api
        if url_data['status'] == 1:
            print('The link has already been shortened.')
        elif url_data['status'] == 2:
            print('The entered link is not a link.')
        elif url_data['status'] == 7:
            website_title: str = url_data['title']
            short_link: str = url_data['shortLink']
            print('Link: ', short_link)
            print('Website: ', website_title)
        else:
            print('Error!', url_data['status'])


def main():
    input_link: str = input('Enter a link: ')
    shorten_link(input_link)


if __name__ == '__main__':
    main()
