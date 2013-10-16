""" main.py: This is the main file of the project."""

__author__ = "Anil Pai"
__copyright__ = "Copyright 2013, Planet Earth"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Anil Pai"
__email__ = "anpai@syr.edu"
__status__ = "Production"
__description__ = "CSE 691: Assignment 1"

import networkx as nx
from twitter_request import make_twitter_request
from oauth_login import oauth_login
from getUserInfo import get_user_info
from getUserInfo import get_screen_name
from collections import OrderedDict
from collections import deque
import matplotlib.pyplot as plt
from getTopFive import getTop

if __name__ == '__main__':
        twitter_api = oauth_login()
        print twitter_api

        # Enter any screen name here
        screen_name = 'anilbpai'

        #Initialize a graph and add the screen name as the node for this graph
        G = nx.Graph()
        G.add_node(screen_name)

        #To get Reciprocal Friends : Common Set of screen_name followers and Friends

        response1 = make_twitter_request(twitter_api.friends.ids,  screen_name=screen_name, count=5000)
        friends = response1["ids"]
        print 'got {0} friends for {1}'.format(len(friends), screen_name)

        response2 = make_twitter_request(twitter_api.followers.ids, screen_name=screen_name, count=5000)
        followers = response2["ids"]
        print 'got {0} followers for {1}'.format(len(followers), screen_name)

        reciprocal_friends = set(friends) & set(followers)
        print 'got {0} reciprocal friends for {1}'.format(len(reciprocal_friends), screen_name)

        reciprocal_friends_list = list(reciprocal_friends)
        mydict = {}
        mydict = get_user_info(twitter_api, user_ids=reciprocal_friends_list)
        sorted_result = OrderedDict(sorted(mydict.items(), key=lambda x: x[1], reverse=True)[:5])
        #Add these initial top five nodes to the graph
        #The Queue will have a list of all the nodes visited in breadth first manner
        que = deque()
        for j in sorted_result.keys():
            m = get_screen_name(twitter_api, user_ids=j)
            print m
            G.add_edge(screen_name, m)
            que.append(j)
        dic = []
        #Looping Starts from here
        '''Recursively call Top 5 Reciprocal Friends of Reciprocal Friends
        Keeps doing this until the number of nodes is greater than 100 , or the queue becomes empty. '''
        while len(que) > 0 and G.number_of_nodes() < 100:
            k = que.popleft()
            m = get_screen_name(twitter_api, user_ids=k)
            print m
            dic = getTop(twitter_api, screen_name=m)
            if not dic:
                continue
            for j in dic:
                G.add_edge(get_screen_name(twitter_api, user_ids=k), get_screen_name(twitter_api, user_ids=j))
                que.append(j)
        print "Social Graph has {0} nodes".format(G.number_of_nodes())
        print "Social Graph has {0} edges".format(G.number_of_edges())
        print "Social Graph has a diameter of {0}".format(nx.diameter(G, e=None))
        print "Social Graph has average distance of {0}".format(nx.average_shortest_path_length(G, weight=None))
        nx.draw(G)
        plt.show()