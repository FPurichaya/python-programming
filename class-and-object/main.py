from user import User
from post import Post

app_user_1 = User("rr@rr.com", "Ronald Weasley", "ronald", "Wizard")
app_user_1.get_user_info()

app_user_2 = User("hh@hh.com", "Harry Potter", "harry", "Wizard")
app_user_2.get_user_info()

new_post_2 = Post("The one that loves us never really leave us.", app_user_2.name)
new_post_2.get_post_info()