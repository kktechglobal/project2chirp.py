# def get_profile (*username,following,followers,post_likes):
#     if post_likes is None:
#         return {'message': 'Post likes not found in the profile.'}
#     elif post_likes > 0:
#         return {'message': 'Post likes found in the profile.', 'post_likes': post_likes}
#     following = profile.get('following', [])
#     if not following:
#         return {'message': 'User is not following anyone.'}
#     followers = profile.get('followers', [])
    
    


#     print(post_likes())
#     print(following(username))
#     print(profile)
#     print(post_likes)


# def get_feed(username): 
#     username = username.lower().strip()
#     # user_feed = [comment for comment in post.values()]
#     # return user_feed
#     user_feed = []
#     if username not in users_db:
#         return {'message': 'User does not exist, register first.'}
#     if username in follow_data:
#         following = follow_data[username]
#         for user in following:
#             if user in users_db:
#                 user_feed.extend(users_db[user].get('posts', []))
#                 if not user_feed:
#                     return {'message': 'No posts found from followed users.'}
#                 return {'message': f'Feed for {username} found.', 'posts': user_feed}
#     return {'message': 'User is not following anyone or no posts found from followed users.'}
# user_feed = get_feed('alice')
# print(user_feed)




# def get_feed(username):
#     username = username.lower().strip()
    
#     if username not in follow_data:
#         return {'message': 'User does not exist.'}
    
#     following = follow_data[username]
#     posts = []
    
#     for user in following:
#         if user in users_db:
#             posts.extend(users_db[user].get('posts', []))
    
#     return {'message': f'Feed for {username} found.', 'posts': posts}


#     print(get_feed('alice'))







# profile = {'firstname':'bob, 'lastname':love, 'username':mike22,'date_of_birth':12/02/1999,'phone_no':09100000099,'post_likes':int(455)}:




#                                #ASSINGMENT 2  BUILD A SOCIAL MEDIA APP
                                
#                                #ASSINGMENT 2  BUILD A SOCIAL MEDIA APP
#                                #ASSINGMENT 2  BUILD A SOCIAL MEDIA APP
                                
#                                #ASSINGMENT 2  BUILD A SOCIAL MEDIA APP






username = {}
post = {}
post_likes = {1: 0, 2: 10} 
follow = {}
users_db = {'alice': {}, 'bob': {}, 'charlie': {}, 'ken': {}, 'jane': {}}  
follow_data = {'alice': set(),   'bob': set(),  'charlie': set(), 'ken': set(), 'jane': set()}
profile = {}
feed = {}
treands = {}



#                                     #username 


def create_user(person):
    person = person.strip().lower()
    if person =='':
        return "Username cannot be empty, input username."
    if person in username:
        return "Username already exists, please choose a new username."
    username[person] = {}
    return "User created successfully."


#                                       #post


def create_post(username,text):
    username = username.strip().lower()
    if username not in username:
        return{'message' : 'User does not exist, please create a user first.'}
    post_id = len(post) + 1
    post[post_id] = {"username": 'auther',text : 'text', 'likes': 0}
    x = {'message' : 'Post created successfully.', 'post_id': post_id, **post[post_id]}
    return x


#                          #like a post 


def like_post(post_id):
    
    post_id = int(post_id) 
    
    
    if post_id in post_likes:
        try:
            
            post_likes[post_id] += 1
            
            return {
                'message': 'Post liked successfully.', 
                'likes': post_likes[post_id]
            }
        except error:
            return {'message': 'An error occurred while trying to like the post.'}
            
    
    return {'message': 'Post does not exist.'}




#                                 #follow


def follow_user(follower, following):
    
    follower = follower.strip().lower()
    following = following.strip().lower()
    

    if follower == following:
        return {'message': 'You cannot follow yourself.'}
        
    if follower not in users_db or following not in users_db:
        return {'message': 'One or both users do not exist.'}
        
    if follower not in follow_data:
        follow_data[follower] = set()
        
    if following in follow_data[follower]:
        return {'message': f'You are already following {following}.'}
        
    follow_data[follower].add(following)
    return {'message': f'You are now following {following}.'}

def unfollow_user(follower, following):
    follower = follower.strip().lower()
    following = following.strip().lower()
    
    if follower not in follow_data or following not in follow_data[follower]:
        return {'message': f'You are not following {following}.'}
        
    follow_data[follower].remove(following)
    return {'message': f'You have successfully unfollowed {following}.'}


                                
#                                 #get profile



def get_profile(username):
    username = username.lower().strip()
    
    if username not in users_db:
        return {'message': 'User does not exist.'}
    
    user_data = users_db[username]
    return {
        'message': f'Profile for {username} found.',
        'following': user_data.get('following', []),
        'posts': user_data.get('posts', [])
    }



 #                               #GET FEED FUNCTION


users_db = {
    'alice': {'posts': ['Alice post 1']},
    'bob': {'posts': ['Bob post 1', 'Bob post 2']},
    'charlie': {'posts': ['Charlie post 1']}
}

follow_data = {
    'alice': {'bob', 'charlie'},  # alice follows bob and charlie
    'bob': {'alice'}
}



def get_feed(username):
    username = username.lower().strip()
    
    if username not in users_db:
        return {'message': 'User does not exist, register first.'}
        
    
    following = follow_data.get(username, set())
    if not following:
        return {'message': 'User is not following anyone.'}
        
    user_feed = []
    
    
    for followed_user in following:
        if followed_user in users_db:
            posts = users_db[followed_user].get('posts', [])
            user_feed.extend(posts)
            
    
    
    if not user_feed:
        return {'message': 'No posts found from followed users.'}
        
    return {
        'message': f"Feed for {username} found.",
        'posts': user_feed
    }



#                                              # trend


post_likes_db = {
    'Bob post 1': 15,
    'Bob post 2': 2,
    'Alice post 1': 25,
    'Charlie post 1': 8
}
                                

def trending(n=3):

    
    sorted_posts = sorted(post_likes_db.items(), key=lambda item: item[1], reverse=True)
    

    top_posts = [post[0] for post in sorted_posts[:n]]

    
    return {
        'message': f"Top {n} trending posts.",
        'trending': top_posts
    }





    

#                                  #  crete user test
print(create_user("Alice"))
print(create_user("ALICE"))
print(create_user(""))
print(create_user("Bob"))



print(create_post("Alice", "Hello, this is my first post on the chirpy app !"))
print(create_post("Bob", "Hello, this is my first post on the chirpy app !"))



#                                    #like post test
print(like_post(1))

result = like_post(1)

if 'likes' in result:
    print(f"Success: {result['message']} Total Likes: {result['likes']}")
else:
    print(f"Error: {result['message']}")


#                                            # follower
print("--- Mutual Follow Test ---")
print(follow_user("Alice", "Bob"))  
print(follow_user("Bob", "Alice"))  
# print(users_db(follow_data))

print("\nCurrent Follow Data:", follow_data)

print("\n--- Unfollow Test ---")
print(unfollow_user("Alice", "Bob"))  # Alice unfollows Bob

print("\nUpdated Follow Data:", follow_data)

    
#                         # get_profile

print(get_profile('alice'))


#                                  # feed print


print("Feed Test")
print(get_feed('alice'))


#                                   # trend print


print("\n--- Trending Test ---")
print(trending(2)) 














