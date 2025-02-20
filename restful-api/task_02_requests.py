#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Erreur lors de la récupération des posts")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        with open('posts.csv', 'w', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            for post in posts:
                writer.writerow({'id': post['id'],
                                 'title': post['title'], 'body': post['body']})
    else:
        print("Erreur lors de la récupération des posts")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
