import instaloader
from datetime import datetime
loader = instaloader.Instaloader()
#loader = Instaloader()
USERNAME = "killergod007"
loader.load_session_from_file('killergod007')
profile = instaloader.Profile.from_username(loader.context,USERNAME)

#download only profile pic
loader.download_profile(USERNAME,profile_pic_only=True)

# post_url = "https://www.instagram.com/p/CgbAU5GD6MU/"
# post = instaloader.Post.from_shortcode(loader.context, post_url.split("/")[-2])
# caption = post.caption
# print("Caption: ", caption)
# comments = []
# for comment in post.get_comments():
    # comments.append(comment.text)
# print("Comments: ", comments)
# num_likes = post.likes
# print("Likes: ", num_likes)
# loader.download_post(post, target=profile.username)

# Extract the post's hashtags
#hashtags = re.findall(r"#(\w+)", caption)
#print("Hashtags: ", hashtags)

#loader.download_profiles(profiles:USERNAME,profile_pic: bool = True, posts: bool = False, tagged: bool = False, igtv: bool = False, highlights: bool = False, stories: bool = False, fast_update: bool = True)

#get all post
#for post in profile.get_posts():
    #loader.download_post(post, target=profile.username)

# returns an integer representing number of posts
#media = profile.mediacount 
#print(media)

# returns integer equal to the number of igtv posts [not working]
#igtv = profile.igtvcount 
#print(igtv)

# returns link to the profile picture [sd pic]
#profile_pic = profile.profile_pic_url
#print(profile_pic)