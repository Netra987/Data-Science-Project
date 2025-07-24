# Data-Science-Project

COMPANY : CODTECH IT SOLUTIONS

NAME : NETRA ALLE

INTERN ID : CT04DG3270

DOMAIN : DATA SCIENCE

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

Spam Detector – A Machine Learning Web App using Flask

This project is a complete end-to-end machine learning web application built with Python and Flask that detects whether a given message is spam or not. The core objective of this application is to demonstrate how machine learning models can be integrated into real-world software systems. By using the power of Natural Language Processing (NLP) and a Naive Bayes classifier, the system can analyze text inputs and predict whether the content is likely spam. This project combines data science, machine learning, and web development concepts into a single, functional application.

The workflow begins with data preprocessing and model training. The dataset used for training is the classic SMS Spam Collection dataset, which contains thousands of messages labeled as "spam" or "ham" (not spam). The train_model.py script loads the dataset, cleans and vectorizes the text using CountVectorizer, and trains a MultinomialNB classifier from Scikit-learn. Once trained, the model is serialized and saved as a .pkl file for later use in predictions. This makes the model portable and ready to be deployed in production.

The backend of the application is powered by Flask, a lightweight and easy-to-use web framework in Python. The main application logic is written in app.py, which loads the saved model and defines routes to render the homepage and process user input. The frontend is handled using an HTML template (index.html) located in the templates folder. It provides a simple form where users can enter a message and receive instant feedback on whether it is considered spam.

For structure and organization, the project includes a clear folder hierarchy. The model folder stores the trained model (spam_model.pkl). The templates folder holds the HTML interface. All necessary dependencies, such as Flask, Scikit-learn, Pandas, and others, are listed in requirements.txt for easy installation. Additionally, a Procfile is included for seamless deployment to platforms like Heroku.

To run this project locally, start by cloning the repository and navigating to the project directory. It's highly recommended to create a virtual environment using python -m venv venv, then activate it (venv\Scripts\activate for Windows or source venv/bin/activate for Unix/macOS). Install all dependencies by running pip install -r requirements.txt. Next, execute train_model.py to generate the trained model file. Once that’s done, launch the web application with python app.py. You can now open your browser and interact with the app at http://127.0.0.1:5000.

This project demonstrates practical skills in machine learning, model deployment, and web integration. It’s a great example of how data science solutions can be turned into usable software products that people can interact with easily. The use of Flask as a web framework makes it extremely lightweight and ideal for small-to-medium scale ML deployments.

#OUTPUT

<img width="1920" height="873" alt="Image" src="https://github.com/user-attachments/assets/7a7f21c7-ed92-4223-8147-b7913b151ae8" />
