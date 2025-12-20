# Social Media Web Application (Instagram-like)

A full-stack social media web application built using Django, inspired by Instagram.  
The project includes real-world social media features such as following users, liking posts, commenting, replying, chatting, and feed-based content discovery.

The application is production-ready and deployed using modern tools like PostgreSQL, Cloudinary, WhiteNoise, and Render.

---

## What this application does

This project allows users to:
- Create an account and log in
- Follow and unfollow other users
- View posts from followed users on the home feed
- Explore other users’ posts via a FYP / gallery-style feed
- Create, upload, edit, and delete posts
- Like and unlike posts
- Comment on posts
- Reply to comments
- Like and unlike comments
- Chat and send messages to other users
- Upload and manage media files
- View user profiles with post galleries

Overall functionality and behavior are inspired by Instagram.

---

## Main Features

### Authentication & Profiles
- User signup, login, logout
- Profile creation and editing
- Profile picture and bio
- Followers and following system
- Reset Password (currently only working on local using console as email backend)

### Posts & Media
- Create, edit, and delete posts
- Image uploads
- Gallery-style layout
- Profile-based post viewing

### Likes, Comments & Replies
- Like and unlike posts
- Comment on posts
- Reply to comments (threaded)
- Like and unlike comments

### Feed System
- Home feed showing posts from followed users
- FYP / Explore feed showing posts from other users
- Chronological and gallery-based feeds

### Chat & Messaging
- One-to-one messaging system
- Chat list with recent conversations
- Message history between users

---

## Project Structure

```
social_media/
├── autho/                 # Authentication (login, signup, logout)
├── posts/                 # Posts, likes, comments, replies
├── profiles/              # User profiles, followers, following, messaging, chats, post-gallery, fyp, feed
├── social_media/          # Core project settings
├── templates/             # Django HTML templates
├── static/                # Static assets
├── uploads/               # Local media (development)
├── manage.py              # Django management file
├── db.sqlite3             # SQLite (local development)
├── requirements.txt       # Python dependencies
└── project_flow.md        # Project notes
```

---

## Technologies Used

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite (development)
- PostgreSQL (production)

### Media & Static Files
- Cloudinary (media storage in production)
- WhiteNoise (static file serving)

### Deployment
- Render (production hosting)

### Tools
- Git & GitHub

---

## Deployment Details

- **Database:** PostgreSQL
- **Media Storage:** Cloudinary
- **Static Files:** Served using WhiteNoise
- **Hosting Platform:** Render

Environment variables are used for sensitive data such as database credentials, secret keys, and Cloudinary configuration.

---

## How to Run Locally

Clone the repository:
```bash
git clone https://github.com/Jayantpradhan62/social_media.git
cd social_media
```

Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate      # Linux / macOS
env\Scripts\activate         # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Run the development server:
```bash
python manage.py runserver
```

Open in browser:
```
http://127.0.0.1:8000/
```
## Cloudinary & Environment Configuration

This project uses **Cloudinary for media storage** in production.

Some models use `CloudinaryField`, and the project is configured with:

- `django-cloudinary-storage`
- `DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`

Because of this, **Cloudinary environment variables are required** even when running the project locally.

If these variables are not set, the project may raise errors during startup or when accessing models that use `CloudinaryField`.

### Required Environment Variables

Before running the project locally, set the following environment variables:

```bash
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```
or just

```bash
CLOUDINARY_URL=your_cloudinary_url
```

### Local Development Options

You have two options when running locally:

#### Option 1: Use Cloudinary locally (recommended)

- Create a free Cloudinary account
- Set the environment variables listed above
- The project will behave the same as production

#### Option 2: Modify settings for local development

For local-only development, you may switch to Django’s default file storage by:
- change DEBUG=Flase to DEBUG=True in settings.py
- Replace `CloudinaryField` with `models.ImageField` in profiles/models.py as models.ImageField(upload_to="profile_pics")
- Run python3 manage.py makemigrations && python3 manage.py migrate


### Deployment Notes

- In production, Cloudinary credentials are securely loaded from environment variables
- Render is used as the hosting platform
- No secrets are hard-coded in the repository



---

## Why this project exists

This project was built to demonstrate:
- Full-stack Django development
- Social media system design
- Feed and follower logic
- Likes, comments, replies, and chat systems
- Media handling using cloud storage
- Production deployment with PostgreSQL and Render

It is suitable for portfolios, resumes, and real-world project demonstrations.

---

## Future Improvements

- Real-time chat using WebSockets
- Notification system
- REST API using Django REST Framework
- Mobile-first responsive UI
- Performance optimization
- Advanced security features

---

## Author

Jayant Pradhan  
GitHub: https://github.com/Jayantpradhan62/social_media

---

If you find this project useful, consider starring the repository.
