from requests_vk import RequestsVK
import config as con

res = RequestsVK(con.TOKEN, con.VERSION)


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