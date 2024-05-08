# Flask Blog Application

This is a simple Flask application for managing a blog. It allows users to create, read, update, and delete blog posts.

## Getting Started

To run this application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Set up a virtual environment (optional but recommended).
4. Run the `main.py` file using Python.
5. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Features

- **Homepage**: Displays all existing blog posts.
- **Individual Post Pages**: Shows the details of each blog post when clicked.
- **Create New Post**: Allows users to create new blog posts by filling out a form.
- **Edit Post**: Provides a form to edit existing blog posts.
- **Delete Post**: Allows users to delete blog posts.
- **About Page**: Provides information about the blog and its purpose.
- **Contact Page**: Allows users to get in touch with the blog owner.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- WTForms
- Flask-CKEditor
- Flask-Bootstrap

## File Structure

- `main.py`: Contains the main Flask application code, including routes and configurations.
- `classes/blog_post_class.py`: Defines the BlogPost class using SQLAlchemy for database interaction.
- `classes/post_form_class.py`: Defines the CreatePostForm class using WTForms for form validation.
- `templates/`: Contains HTML templates for rendering the web pages.
- `static/`: Stores static files such as CSS, JavaScript, and images.

## Credits

Developed By Abdullah Khurram <https://www.github.com/Abdullah9202>
