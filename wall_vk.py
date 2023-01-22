import datetime
import time

from requests_vk import RequestsVK
import config as con


res = RequestsVK(con.TOKEN, con.VERSION) #TOKEN- сервисный ключ доступа
res_two = RequestsVK(con.access_token, con.VERSION) #access_token-ключ доступа пользователя


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


def create_record_wall(owner_id: int, friends_only=0, from_group=0, message='', attachments=None, services: str = None,
                       signed=0, publish_date: str = None, post_id: int = None, mark_as_ads=0, close_comments=0,
                       donut_paid_duration=0, mute_notifications=0, copyright: str = None):
    '''
    Позволяет создать запись на стене, предложить запись на стене публичной страницы,
    опубликовать существующую отложенную запись.
    :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
    :param friends_only: 1 — запись будет доступна только друзьям, 0 — всем пользователям.
        По умолчанию публикуемые записи доступны всем пользователям.
    :param from_group: Данный параметр учитывается, если owner_id < 0 (запись публикуется на стене группы).
         1 — запись будет опубликована от имени группы, 0 — запись будет опубликована от имени пользователя
    :param message: Текст сообщения (является обязательным, если не задан параметр attachments).
    :param attachments: Объект или несколько объектов, приложенных к записи.К записи можно приложить медиа или ссылку
        на внешнюю страницу. Если объектов несколько, их нужно указать через запятую «,».
    :param services:Список сервисов или сайтов, на которые необходимо экспортировать запись, в случае если пользователь
     настроил соответствующую опцию
    :param signed: 1 — у записи, размещенной от имени сообщества, будет добавлена подпись (имя пользователя,
    разместившего запись), 0 — подписи добавлено не будет. Параметр учитывается только при публикации на стене
    сообщества и указании параметра from_group.
    :param publish_date: Дата публикации записи.Если параметр указан, публикация записи будет отложена до указанного
    времени. Вводится строка формат 'ГОД,МЕСЯЦ,ЧИСЛО,ВРЕМЯ,МИНУТЫ' (пример:'2023,01,22,22,00')
    :param post_id: Идентификатор записи, которую необходимо опубликовать. Данный параметр используется для публикации
    отложенных записей и предложенных новостей.
    :param mark_as_ads: 1 — у записи, размещенной от имени сообщества, будет добавлена метка Это реклама,
     0 — метки добавлено не будет.
    :param close_comments: 1 — комментарии к записи отключены, 0 — комментарии к записи включены.
    :param donut_paid_duration: Период времени в течение которого запись будет доступна для донов
    — платных подписчиков VK Donut. Возможные значения: смотреть в документации VK API.
    :param mute_notifications: 1 — уведомления к записи  отключены; 0 — уведомления к записи включены.
    :param copyright: Источник материала. Поддерживаются внешние и внутренние ссылки.


    :return: После успешного выполнения возвращает идентификатор созданной записи (post_id).
    '''
    date_time = datetime.datetime(*[int(i) for i in publish_date.split(',')])
    publish_date_unit = time.mktime(date_time.timetuple())

    method = "wall.post"
    params = {
        'access_token': str,
        'v': float,
        'owner_id': owner_id,
        'friends_only': friends_only,
        'from_group': from_group,
        'message': message,
        'attachments': attachments,
        'services': services,
        'signed': signed,
        'publish_date': publish_date_unit,
        'post_id': post_id,
        'mark_as_ads': mark_as_ads,
        'close_comments': close_comments,
        'donut_paid_duration': donut_paid_duration,
        'mute_notifications': mute_notifications,
        'copyright': copyright

    }
    return res_two.make_request(method, params)







