# GIT LOST
## WIE LUMINA 25 Hackathon
#### Members: 
   #### Pradyumna Verma(Team Leader, ML Enginner of the team)
   
   #### Animesh Kansal(Backend , Frontend head)
   
   #### Raunit Lakhmani(Frontend, Backend Developer)
   
   #### Bhavyaa Chauhan(Frontend Developer)

## IDEA:- Centralized Student-Alumni Engagement Platform
A web platform designed to connect students and alumni of a specific university. This project bridges the gap between current students seeking guidance and experienced alumni willing to provide mentorship, share opportunities, and foster a strong community.

The platform features a dynamic frontend and is powered by machine learning models to ensure a relevant and safe user experience.

### ✨ Core Features


Student & Alumni Dashboards: Separate, tailored views for students to find mentors and alumni to post opportunities.

Intelligent Mentor Discovery: A searchable directory of alumni mentors, filterable by industry, skills, and company.

ML-Powered Community Feed: A personalized feed that recommends relevant posts, opportunities, and discussions to users.

ML-Powered Spam Protection: Automatically filters spam from user-generated posts and comments to maintain platform quality.

Community Groups: Allows users to join communities based on interests (e.g., "Web Dev", "Data Science", "Hackathons").

Events & Achievements: A section to highlight university news, student achievements, and upcoming alumni events.

LINUX friendly: Deployed model on flask in a way that it works on LINUX !

### 🛠️ Tech Stack


Frontend: Static HTML, Tailwind CSS

Machine Learning: Python, Scikit-learn, Pandas, Jupyter Notebook

Backend: Deployed the ML models on streamlit so any user can just download the app1.py and app2.py from our repo and run them on their own local host server. Deployed the model on Flask for LINUX as well.

### 🤖 Machine Learning Models


This repository contains two core machine learning models, detailed in Jupyter Notebooks.

1. Feed Personalization (Recommendation System)

File: Feed_Personalization.ipynb

Purpose: To create a personalized and relevant community feed for students and alumni. When a user views a post, this model recommends other posts that are contextually similar.

Algorithm: This is a Content-Based Filtering system.

TF-IDF Vectorizer: Post content (titles, descriptions) is converted into a numerical matrix representing the importance of each word.

Cosine Similarity (linear_kernel): The model calculates the similarity score between all posts based on their TF-IDF vectors.

Recommendation: When given a specific post, it returns a list of the most similar posts, which can then be displayed to the user as "Recommended for you."

2. Spam Protection (Text Classification)

File: Spam_Protection.ipynb

Purpose: To automatically detect and flag spammy content submitted by users (e.g., in the community feed or in comments).

Algorithm: This is a Supervised Text Classification model.

TF-IDF Vectorizer: The text is converted into a numerical matrix.

Multinomial Naive Bayes (MultinomialNB): A probabilistic classifier is trained on a labeled dataset to learn the likelihood of words appearing in 'spam' vs. 'ham' (legitimate) content.

Prediction: The trained model can predict whether a new, unseen piece of text is spam or ham with a high degree of accuracy.

### 🖥️ Frontend Components


The frontend is a collection of static HTML files styled with Tailwind CSS, demonstrating the user interface and flow.

login.html: Login page with differentiation for "Student" and "Alumni".

details.html: A profile setup page for users to input their information.

studentdashboard.html: The main landing page for students, showing the community feed and recommended mentors.

alumnidashboard.html: The main landing page for alumni, showing student requests and options to post opportunities.

mentor2.html: The "Find Mentors" page with search and filter functionality.

communities.html: A page showcasing different interest-based communities.

events.html: A page displaying university news and student achievements.

### 🔮 Future Work


Database: Add a database (like PostgreSQL, MySQL, or Firebase/Firestore) to store user data, posts, and community information.

Deployment: Deploy the fully integrated application to a cloud platform (e.g., Heroku, Vercel, AWS).
