#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
    subs = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subs(sys.argv[1])
