import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import os

# ✅ Load working dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep="\t", header=None)
df.columns = ['label', 'message']

# ✅ Encode labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# ✅ Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('model', MultinomialNB())
])

pipeline.fit(X_train, y_train)

# ✅ Save model
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, 'model/spam_model.pkl')
print("Model saved to model/spam_model.pkl")
