import praw
import config
from create import post

def redditLogin():
    login = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "u/mindfreakz's read newspaper bot")
    return login

def run(r):
    sub = r.subreddit("hci_circlejerk")
    for submission in sub.hot(limit=10):
        zelda = submission.url
 #       print(zelda)
        post(zelda)

r = redditLogin()
run(r)
