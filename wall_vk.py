from requests_vk import RequestsVK
import config as con


res = RequestsVK(con.TOKEN, con.VERSION)


def get_1000_posts(domain: str, count: int, offset=0) -> list:
    '''
    1000 first posts from the community wall.
        :param domain: The short address of the user or community.
        :param count: The number of records to be retrieved. Maximum: 100
        :param offset: The offset required to select a specific subset of record.
    :return: The list of dictionaries with data for each posts
    '''

    all_posts = []

    while offset < 1000:
        method = "wall.get"
        params = {
            'access_token': str,
            'v': float,
            'domain': domain,
            'count': count,
            'offset': offset
        }
        data = res.make_request(method, params)['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def get_post_id(posts: str, extended=0, fields=None) -> list:
    '''
    Returns a list of records from the walls of users or communities by their IDs.
        :param posts: The string is of this format: The owner_id and the post_id going through the underscore sign\
        and it is comma-separated ("93388_21539,-1_20904")
        :param extended: if the value is 1, additional profiles and groups fields will be returned in the response
        :param fields: List of additional fields for profiles and groups to be returned.Note that this parameter \
        is taken into account only when extended=1.
    :return: Data from the wall is about the requested posts
    '''
    method = "wall.getById"
    params = {
        'access_token': str,
        'v': float,
        'posts': posts,
        'extended': extended,
        'fields': fields
    }

    return res.make_request(method, params)['response']


# def create_record_wall(token_community: str, version: float, owner_id: int, friends_only=0, from_group=0,
#                        message='', attachments=None):
#     method = "wall.post"
#     params = {
#         'access_token': token_community,
#         'v': version,
#         'owner_id': owner_id,
#         'friends_only': friends_only,
#         'from_group': from_group,
#         'message': message,
#         'attachments': attachments
#
#     }
#     return make_request(method, params)




