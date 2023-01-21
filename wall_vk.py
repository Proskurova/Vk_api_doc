import requests


def make_request(method: str, params: dict) -> dict:
    response = requests.get('https://api.vk.com/method/' + method, params=params)
    data = response.json()
    return data


def get_1000_posts(token: str, version: float, domain: str, count: int, offset=0) -> list:
    '''
    1000 first posts from the community wall.
    :param token: user access key VK API
    :param version: API Versions VK
    :param domain: The short address of the user or community.
    :param count: The number of records to be retrieved. Maximum: 100
    :param offset: The offset required to select a specific subset of record.
    :return: The list of dictionaries with data for each posts
    '''

    all_posts = []

    while offset < 1000:
        method = "wall.get"
        params = {
            'access_token': token,
            'v': version,
            'domain': domain,
            'count': count,
            'offset': offset
        }
        data = make_request(method, params)['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def get_post_id(token: str, version: float, posts: str, extended=0) -> list:
    '''
    Returns a list of records from the walls of users or communities by their IDs.
    :param token: user access key VK API
    :param version: API Versions VK
    :param posts: The string is of this format: The owner_id and the post_id going through the underscore sign\
    and it is comma-separated ("93388_21539,-1_20904")
    :param extended: if the value is 1, additional profiles and groups fields will be returned in the response
    :return: Data from the wall is about the requested posts
    '''
    method = "wall.getById"
    params = {
        'access_token': token,
        'v': version,
        'posts': posts,
        'extended': extended
    }

    return make_request(method, params)['response']
