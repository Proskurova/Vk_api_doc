import requests


def get_1000_posts(token=str, domain=str, count=int, offset=0, version=5.131):
    '''
    1000 first posts from the community wall.
    :param token: Access key
    :param domain: The short address of the user or community.
    :param count: The number of records to be retrieved. Maximum: 100
    :param offset: The offset required to select a specific subset of record.
    :param version: vK API version
    :return: The list of dictionaries with data for each post
    '''

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