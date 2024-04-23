import os
import requests


# This function extracts the type of image from its url.
def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.svg', '.gif']
    for extension in extensions:
        if extension in image_url:
            return extension


def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be located.')

    # Check if name exists.
    if os.path.isfile(image_name):
        raise Exception('File name already exists.')

    '''
    Download image.
    
    Param image_content contains the bytes of the image that will be downloaded.
    '''
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')


'''
Param input_url contains the url that user gives.

Param url_lists is a list that contain all of the urls  that user have inputted so far.

Param counter is useful for naming the pictures. It is added to the end of the string 'image' to prevent the files having
the same name and therefore over-writing.
'''
if __name__ == '__main__':
    url_list: list[str] = []
    print('------------------------------------------')
    print('Input the url of the picture to download!')
    print('Input 0 when you are done inputting urls.')
    while True:
        input_url: str = input('Enter a url: ')
        if input_url == '0':
            break
        else:
            url_list.append(input_url)
    print(url_list)
    counter: int = 0
    for url in url_list:
        counter += 1
        print('Downloading...')
        file_name: str = f'image{counter}'
        download_image(url, file_name, 'Images')
