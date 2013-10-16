from twitter_request import make_twitter_request
from getUserInfo import get_user_info
from collections import OrderedDict

'''Function to get the Top 5 Reciprocal Friends '''


def getTop(twitter_api, screen_name=None):
    response1 = make_twitter_request(twitter_api.friends.ids,  screen_name=screen_name, count=5000)
    friends = response1["ids"]
    print 'got {0} friends for {1}'.format(len(friends), screen_name)
    response2 = make_twitter_request(twitter_api.followers.ids, screen_name=screen_name, count=5000)
    followers = response2["ids"]
    print 'got {0} followers for {1}'.format(len(followers), screen_name)
    reciprocal_friends = set(friends) & set(followers)
    print 'got {0} reciprocal friends for {1}'.format(len(reciprocal_friends), screen_name)
    reciprocal_friends_list = list(reciprocal_friends)
    mydict = get_user_info(twitter_api, user_ids=reciprocal_friends_list)
    if mydict:
        sorted_result = OrderedDict(sorted(mydict.items(), key=lambda x: x[1], reverse=True)[:5])
        return sorted_result.keys()
    else:
        sorted_result = mydict
        return sorted_result