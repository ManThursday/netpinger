import datetime
import sys
import time

import requests
from requests.exceptions import HTTPError


def check_url(url):
    try:
        requests.get(url, {
            'allow_redirects': False,
            'timeout': 2.0,
        })
    except HTTPError:
        return True
    except Exception as ex:
        return False
    else:
        return True


def keep_checking(urls):
    while True:
        for url in urls:
            result = check_url(url)
            print('{stamp} {url} {result}'.format(
                stamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                url=url,
                result='up' if result else 'down',
            ))


def get_args():
    parser = argparse.ArgumentParser(description='Check internet')
    parser.add_argument('-r', '--router-url', dest='router_url')
    parser.add_argument('-u', '--url', dest='urls', action='append')
    args = parser.parse_args()
    

if __name__ == '__main__':
    args = get_args()
    if args.urls:
        keep_checking(urls)
    else:
        print('Need URLs')
        sys.exit(1)
