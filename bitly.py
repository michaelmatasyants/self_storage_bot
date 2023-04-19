from urllib.parse import urlsplit
import argparse
import os
import requests
from dotenv import load_dotenv


def shorten_link(bitly_token, link) -> str:
    headers = {
      "Authorization": f'Bearer {bitly_token}',
    }
    payload = {'long_url': link}
    response_short = requests.post(
        'https://api-ssl.bitly.com/v4/bitlinks',
        headers=headers, json=payload)
    response_short.raise_for_status()
    bitlink = response_short.json().get("link")
    return bitlink


def count_clicks(bitly_token, link):
    parsed_url = urlsplit(link)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    url = 'https://api-ssl.bitly.com/v4'
    headers = {'Authorization': f'Bearer {bitly_token}'}
    params = {'unit': 'day', 'units': '-1'}
    count_clicks_response = requests.get(
        f'{url}/bitlinks/{bitlink}/clicks/summary',
        params=params, headers=headers)
    count_clicks_response.raise_for_status()
    return count_clicks_response.json().get("total_clicks")


def is_bitlink(bitly_token, link):
    headers = {'Authorization': f'Bearer {bitly_token}'}
    parsed_url = urlsplit(link)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    bitlink_response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}',
        headers=headers)
    return bitlink_response.ok


def main():
    load_dotenv()
    bitly_token = os.environ["BITLY_TOKEN"]
    parser = argparse.ArgumentParser(
        description="Get count of clicks on the bitlink"
        )
    parser.add_argument("link", help="shotened bitlink or link to make short")
    args = parser.parse_args()
    link = args.link
    if is_bitlink(bitly_token, link):
        return print(f'Number of clicks on {link} is:',
                     count_clicks(bitly_token, link))
    return print("The shortened link is:", shorten_link(bitly_token, link))


if __name__ == '__main__':
    main()
