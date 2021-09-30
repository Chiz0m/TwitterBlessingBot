import tweepy
from tweepy import api

def tweetBlessing():
    api_key = "BFYAhp3aLGIS9yGJaCKuQpeY2"
    api_secret_key = "nKJ1KjMkGQv6HCLBXw5YBgpsQ3bjozR3XI1HnzAGqoTmtIFrtt"
    access_token = "751009198087995392-03RQMUqPlu3GvM28FOQLbafMFDvJBA8"
    access_token_secret = "3s7NGzhVbs5xAAYzfkZDpVyqPfAMJ6krc1omc2lqHI2r7"
    # Protocol for authorization
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    # Give access to api
    api = tweepy.API(auth)

    # Take input to be tweeted
    # tweet = input("What do you want to tweet?: ")

    # Tweeting with my developer twitter account
    api.update_status(status = "Today is a blessing ❤️ - TwitterBlessingBot")


# calling my tweetBlessing function to tweet on Twitter
tweetBlessing()


# this try except allows me to test if the authentication works
# try:
#     api.verify_credentials()
#     print("Authentication OK")
    
# except:
#     print("Error during authentication")

