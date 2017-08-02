import praw
import config


from create import commentBuilder, submissionLinkParsing
import botLogin 

def run(r):
    sub = r.subreddit("hci_circlejerk")
    for submission in sub.hot(limit=10):
        zelda = submission.url
        submissionLinkParsing(zelda)
        commentBody = commentBuilder(zelda)

if __name__ == "__main__":
    r = botLogin.login()
    run(r)
