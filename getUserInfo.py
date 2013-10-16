from twitter_request import make_twitter_request
'''Function to get User Information of user ids taking 100 user ids in a request at a time'''


def get_user_info(twitter_api, user_ids=None):
    items_to_info = {}
    items = user_ids
    while len(items) > 0:
        # Process 100 items at a time per the API specifications for /users/lookup. See
        # https://dev.twitter.com/docs/api/1.1/get/users/lookup for details
        items_str = ','.join([str(item) for item in items[:100]])
        response = make_twitter_request(twitter_api.users.lookup, user_id=items_str)
        for user_info in response:
            items_to_info[user_info['id']] = user_info['followers_count']
        return items_to_info


'''Lookup Function to get the screen name using any twitter user id'''


def get_screen_name(twitter_api, user_ids=None):
    response = make_twitter_request(twitter_api.users.lookup, user_id=user_ids)
    for user_info in response:
        t = user_info['screen_name']
    return t