import praw
import config

def login():
    login = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "u/mindfreakz's read newspaper bot")
    return login

