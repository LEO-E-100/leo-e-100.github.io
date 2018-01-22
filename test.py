import os
import glob

posts = []
for root, dirs, files in os.walk('posts'):
    posts += glob.glob(os.path.join(root, '*.html'))
print posts

titles = []
for post in posts:
    tmp = post.split('/')[1]
    tmp2 = tmp.split('.')[0]
    titles.append(tmp2)
print titles
