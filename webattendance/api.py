
import instaloader
loader = instaloader.Instaloader()
loader.login('your_username', 'your_password')
profile = instaloader.Profile.from_username(loader.context, 'target_username')
print("Username:", profile.username)
print("Full Name:", profile.full_name)
print("Followers:", profile.followers)
print("Following:", profile.followees)
print("Bio:", profile.biography)
posts = profile.get_posts()
for post in posts:
    # Access post data
    print("Post:", post.url)
    print("Caption:", post.caption)
    print("Likes:", post.likes)
    print("Comments:", post.comments)
    print("Timestamp:", post.date)
    print("---")
stories = profile.get_stories()
for story in stories:
    # Access story data
    print("Story:", story.url)
    print("Timestamp:", story.date)
    print("---")
