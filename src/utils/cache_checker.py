#!user/bin/env python3
import time

def check(response):
    '''
    cache terminal printer for dev
    Args:
        response(:obj:): takes response object as input
    Output:
        Prints to terminal
    Returns
        N/A success 
    '''
    now = time.ctime(int(time.time()))

    print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))

    return