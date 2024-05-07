import os
import sys
import bleach

# Getting the path of current dir ==> others
current_dir = os.path.dirname(__file__)
# Add the root directory of the project to the Python path
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(root_dir)


# My Files
from main import app, db, BlogPost

# Creating an application context
app.app_context().push()

# Getting the data
data = db.session.query(BlogPost).all()

for post in data:
    print(post.body)