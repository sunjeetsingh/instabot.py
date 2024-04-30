import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
access_token='xxxx'
base_url='https://api.instagram.com'
def self_info():
    request_url=(base_url+'users/self/?access_token=%s') %(access_token)
    print'request url is: %s' %(request_url)
    user_info= requests.get(request_url).json() #getting details using GET method
    #printing required fields using JSON response

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

#ID of user using username

def get_user_id(insta_username):
    request_url = (base_url + 'users/search?q=%s&access_token=%s') % (insta_username, access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

#info of user using username

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url + 'users/%s?access_token=%s') % (user_id, access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'

#getting our own post

def get_own_post():
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


#get the recent post of a user by username

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

#ID of recent post of user using username

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()

#ID of our own post
def get_self_post_id():
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            return own_media['data'][0]['id']
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


#like recent post of a user

def like_a_post(insta_username):
    get_post_id(insta_username)
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/likes') % (media_id)
    payload = {"access_token": access_token}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

#liking own post
def like_own_post():
    media_id = get_own_post()
    request_url = (base_url + 'media/%s/likes') % (media_id)
    payload = {"access_token": access_token}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'
#to comment on recent post of a user

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": access_token, "text": comment_text}
    request_url = (base_url + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

#comment on own post
def post_own_comment():
    media_id = get_own_post()
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": access_token, "text": comment_text}
    request_url = (base_url + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

#delete negative comments from recent post user of user

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, access_token)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (base_url + 'media/%s/comments/%s/?access_token=%s') % (
                        media_id, comment_id, access_token)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'

#get listof comments on your own recent post

def get_own_comment_list():
    media_id=get_own_post()
    request_url= (base_url+ 'media/%s/comments?access_token=%s') %(media_id,access_token)
    print'GET request url=%s' %(request_url)
    comment_list=requests.get(request_url).json()
    print comment_list
    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            print'list of comments'
            number=1
            for text in comment_list['data']:
                print'%s from %s\n comment=%s' %(number,text['from']['username'],text['text'])
                number=number+1
        else:
            print'no comments found'
            return None
    else:
        print'status code other than 200 recieved'
        exit()

#Get list of comment of a users recent post

def user_comment_list(insta_username):
    media_id=get_user_post(insta_username)
    request_url = (base_url + 'media/%s/comments?access_token=%s') % (media_id, access_token)
    print'GET request url=%s' % (request_url)
    comment_list = requests.get(request_url).json()
    print comment_list
    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            print'list of comments'
            number = 1
            for text in comment_list['data']:
                print'%s from %s\n comment=%s' % (number, text['from']['username'], text['text'])
                number = number + 1
        else:
            print'no comments found'
            return None
    else:
        print'status code other than 200 recieved'
        exit()








def start_bot():
    while True:
        try:
            username_selection = int(raw_input("do you want to continue with the username already provided=singh_sunjeet\n if yes type 1\n else press 2"))
            if username_selection == 1:  # starting with the already provided username
                while True:
                    try:
                        print 'welcome to instabot'
                        print'here are you menu options'
                        print'1.Get your own details\n'
                        print'2.Get your own recent post\n'
                        print'3.Get ID of your recent post\n'
                        print'4.like your recent post\n'
                        print'5.comment on your recent post\n'
                        print'6.Get comment list on your recent post\n'
                        print'0.To exit'
                        selection = int(raw_input('enter your choice'))
                        if selection == 1:
                            self_info()
                        elif selection == 2:
                            get_own_post()
                        elif selection == 4:
                            like_own_post()
                        elif selection == 5:
                            post_own_comment()
                        elif selection == 6:
                            get_own_comment_list()
                        elif selection == 0:
                            exit()
                        else:
                            print "INVALID ENTRY,ENTER AGAIN"
                    except ValueError:
                        print'ENTER CORRECT INPUT PLEASE'

            else:

                while True:
                    try:
                        print '\n'
                        print 'Hey! Welcome to instaBot!'
                        print 'Here are your menu options:'
                        print "1.Get details of a user by username\n"
                        print "2.Get the recent post and ID of post of a user by username\n"
                        print "3.Like the recent post of a user\n"
                        print "4.Get a list of comments on the recent post of a user\n"
                        print "5.Make a comment on the recent post of a user\n"
                        print "6.Delete negative comments from the recent post of a user\n"
                        print "0.For exit"

                        choice = int(raw_input("Enter you choice: "))
                        if choice == 1:
                            insta_username = raw_input("Enter the username of the user: ")
                            get_user_info(insta_username)
                        elif choice == 2:
                            insta_username = raw_input("Enter the username of the user: ")
                            get_user_post(insta_username)
                            get_post_id(insta_username)
                        elif choice == 3:
                            insta_username = raw_input("Enter the username of the user: ")
                            like_a_post(insta_username)
                        elif choice == 4:
                            insta_username = raw_input("Enter the username of the user: ")
                            user_comment_list(insta_username)
                        elif choice == 5:
                            insta_username = raw_input("Enter the username of the user: ")
                            post_a_comment(insta_username)
                        elif choice == 6:
                            insta_username = raw_input("Enter the username of the user: ")
                            delete_negative_comment(insta_username)
                        elif choice == 0:
                            exit()
                        else:
                            print "PLEASE ENTER A CORRECT INPUT"
                    except ValueError:
                        print'ENTER A VALID INPUT PLEASE'
        except ValueError:
            print'enter a valid input please'


start_bot()
