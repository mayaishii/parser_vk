import csv
import time

import requests


def take_1000_posts():
    token = 'fb3fee24fb3fee24fb3fee24d1fb520797ffb3ffb3fee24a6f833e0882bc95e6988a1bd'
    version = 5.92
    domain = 'judonews'
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': count,
                                'offset': offset
                            }
                            )

        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    with open('judonews.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass

            a_pen.writerow((post['likes']['count'], post['text'], img_url))

all_posts = take_1000_posts()
file_writer(all_posts)


print(1)