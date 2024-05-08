from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import datetime
import bleach
# My Files (Classes)
from classes.blog_post_class import db, BlogPost
from classes.post_form_class import CreatePostForm

##Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app = db.init_app(app)

# Homepage Route
@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

# Show Posts Route
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.session.query(BlogPost).get(post_id)
    # Validation for requested post
    if requested_post:
        return render_template("post.html", post=requested_post)
    else:
        return "<h3>Requested post not found</h3>", 404

# New Post Route
@app.route("/new-post/", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    # Getting the date for form
    today_Date = datetime.datetime.now()
    formatted_Date = today_Date.strftime("%B, %d %Y")
    # Validaing the form
    if form.validate_on_submit():
        # Feeding the new post in DB
        newPost = BlogPost(
            title=form.title.data,
            subtitle=form.title.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=formatted_Date
        )
        db.session.add(newPost)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

# Edit Post Route
@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # Getting the post from DB
    post_to_edit = db.session.query(BlogPost).get(post_id)
    
    # Creating an edit form that is showing the data from the DB
    edit_form = CreatePostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        author=post_to_edit.author,
        img_url=post_to_edit.img_url,
        body=post_to_edit.body,
    )
    
    # Validating the edit_form
    if edit_form.validate_on_submit():
        # Editing the post in DB
        post_to_edit.title = edit_form.title.data
        post_to_edit.sub_title = edit_form.subtitle.data
        post_to_edit.author = edit_form.author.data
        post_to_edit.img_url = edit_form.img_url.data
        post_to_edit.body = edit_form.body.data
        # Commiting changes to DB
        db.session.commit()
        # Redirecting to home page in case of success
        return redirect(url_for("show_post", post_id=post_id))
    return render_template("edit-post.html", form=edit_form)

# Delete Route
@app.route("/delete-post/int:<post_id>", methods=["GET", "DELETE"])
def delete_post(post_id):
    post_to_delete = db.session.query(BlogPost).get(post_id)
    # Validation for post to delete
    if post_to_delete:
        db.session.delete(post_to_delete)
        db.session.commit()
        # Returning to homepage in case of success
        return redirect(url_for("get_all_posts"))
    else:
        return "<h3>Post not found!</h3>", 404

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Executing as script
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)