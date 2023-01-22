from requests_vk import RequestsVK
import config as con

res = RequestsVK(con.TOKEN, con.VERSION) #TOKEN- сервисный ключ доступа
res_two = RequestsVK(con.access_token, con.VERSION) #access_token-ключ доступа пользователя


def get_by_id_group(group_ids: str, group_id: str, fields: str = None) -> list:
    '''
    Returns information about a given community or about several communities.
        :param group_ids: Identifiers or short names of communities. The maximum number of IDs is 500.
        :param group_id: The ID or short name of the community.
        :param fields: A list of additional fields that need to be returned.
    :return: The list of data with information about groups
    '''
    method = "groups.getById"
    params = {
        'access_token': str,
        'v': float,
        'group_ids': group_ids,
        'group_id': group_id,
        'fields': fields
    }
    return res.make_request(method, params)['response']


def get_members(group_id: str, fields: str = None, filters: str = None, count=100, sort='id_asc', offset=0) -> dict:
    '''
    Returns a list of community members.
        :param group_id: The ID or short name of the community.
        :param fields: A list of additional fields that need to be returned.
        :param filters: Filter communities by data:friends,unsure,managers,donut.
        :param count: The number of community members that you need to get information about.
        :param sort: Sorting from which to return the list of participants. Can take values:id_asc(ascending ID),\
        id_desc(decreasing ID),
        :param offset: The offset required to sample a specific subset of participants.
    :return: The list of data with information about members.
    '''
    method = "groups.getMembers"
    params = {
        'access_token': str,
        'v': float,
        'group_id': group_id,
        'sort': sort,
        'offset': offset,
        'count': count,
        'fields': fields,
        'filter': filters
    }
    return res.make_request(method, params)


def get_groups(user_id: int, fields: str = None, filters: str = None, count=100, extended=0, offset=0) -> dict:
    '''
    Returns a list of the specified user's communities.
        :param user_id: ID of the user whose community information you want to get.
        :param fields: A list of additional fields that need to be returned.
        :param filters: A comma-separated list of community filters to be returned.
        :param count: The number of community members that you need to get information about.
        :param extended: If 1-full information about user groups returned
        :param offset: The offset required to sample a specific subset of participants.
    :return: The list of data with information about user.
    '''
    method = "groups.get"
    params = {
        'access_token': str,
        'v': float,
        'user_id': user_id,
        'extended': extended,
        'offset': offset,
        'count': count,
        'fields': fields,
        'filter': filters
    }
    return res_two.make_request(method, params)