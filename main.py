import argparse
import datetime
import sys
import time

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout


def check_url(url):
    try:
        requests.get(
            url,
            allow_redirects=False,
            timeout=2.0,
        )
    except HTTPError:
        return 'up'
    except ConnectionError:
        return 'down'
    except Timeout:
        return 'timeout'
    except Exception as ex:
        return 'error'
    else:
        return 'up'


def keep_checking(urls):
    while True:
        for url in urls:
            result = check_url(url)
            print('{stamp} {url} {result}'.format(
                stamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                url=url,
                result=result,
            ))


def get_args():
    parser = argparse.ArgumentParser(description='Check internet')
    parser.add_argument('-r', '--router-url', dest='router_url')
    parser.add_argument('-u', '--url', dest='urls', action='append')
    return parser.parse_args()
    

if __name__ == '__main__':
    args = get_args()
    if args.urls:
        keep_checking(args.urls)
    else:
        print('Need URLs')
        sys.exit(1)
