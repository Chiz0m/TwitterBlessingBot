import tweepy

def tweetBlessing():
    api_key = ""
    api_secret_key = ""
    access_token = ""
    access_token_secret = ""
    # Protocol for authorization
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    # Give access to api
    api = tweepy.API(auth)

    # Tweeting with my developer twitter account
    api.update_status(status = "Today is a blessing ❤️")


# calling my tweetBlessing function to tweet on Twitter
tweetBlessing()


# this try except allows me to test if the authentication works
# try:
#     api.verify_credentials()
#     print("Authentication OK")
    
# except:
#     print("Error during authentication")

