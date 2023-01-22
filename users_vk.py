from requests_vk import RequestsVK
import config as con

res = RequestsVK(con.TOKEN, con.VERSION)


def get_users(user_ids: str, fields: str = None, name_case: str = None) -> list:
    '''
    Returns extended user information.
        :param user_ids: A comma-separated string of id or screen_name
        :param fields: List of additional profile fields
        :param name_case: See the available values in the documentation VK API
    :return: The list of data with information about users.
    '''
    method = "users.get"
    params = {
        'access_token': str,
        'v': float,
        'user_ids': user_ids,
        'fields': fields,
        'name_case': name_case
    }
    return res.make_request(method, params)['response']

