import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download NLTK data (only needed once)
nltk.download('stopwords', quiet=True)

# Initialize stemmer
ps = PorterStemmer()

@st.cache_resource
def load_data_and_train_model():
    # Load your dataset
    df = pd.read_csv(
        r"C:\Users\hp\OneDrive\Documents\SRK_CLASS\SRK_Class\Notes\22. Natural Language Processing\SMSSpamCollection",
        sep="\t",
        names=['Label', 'Message']
    )
    
    # Preprocess text
    corpus = []
    for message in df['Message']:
        # Remove special characters
        message = re.sub('[^a-zA-Z]', ' ', message)
        # Convert to lowercase and split
        words = message.lower().split()
        # Remove stopwords and stem
        words = [ps.stem(word) for word in words if word not in stopwords.words('english')]
        # Join back to string
        corpus.append(' '.join(words))
    
    # Vectorize text
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)
    
    # Prepare target (convert to 1D array to avoid warning)
    y = pd.get_dummies(df['Label'], drop_first=True).astype('int').squeeze()
    
    # Train model
    model = MultinomialNB()
    model.fit(X, y)
    
    return model, cv

# Load model and vectorizer
model, cv = load_data_and_train_model()

def predict_message(message):
    # Preprocess the input message
    message = re.sub('[^a-zA-Z]', ' ', message)
    words = message.lower().split()
    words = [ps.stem(word) for word in words if word not in stopwords.words('english')]
    processed_msg = ' '.join(words)
    
    # Vectorize
    vectorized_msg = cv.transform([processed_msg])
    
    # Predict
    prediction = model.predict(vectorized_msg)
    probability = model.predict_proba(vectorized_msg)

    
    return "Spam" if prediction[0] == 1 else "Ham", probability[0][1]

# Streamlit UI
st.set_page_config(page_title=" Spam Detector", page_icon="📱")

st.title("📱/✉️ SMS/EMAIL Spam Detection")
st.write("""
This app uses Natural Language Processing to classify  messages as **Spam** or **Ham** (not spam).
""")

# Input form
with st.form("message_form"):
    user_input = st.text_area(
        "Enter a message to analyze:",
        
        height=150
    )
    submitted = st.form_submit_button("Check Message")

if submitted:
    if not user_input.strip():
        st.warning("Please enter a message to analyze.")
    else:
        prediction, spam_prob = predict_message(user_input)
        
        if prediction == "Spam":
            st.error(f"**Prediction:** {prediction} (confidence: {spam_prob:.1%}) 🚨")
            st.warning("This message appears to be spam. Be cautious with any links or requests.")
        else:
            st.success(f"**Prediction:** {prediction} (confidence: {1-spam_prob:.1%}) ✅")
            st.info("This message appears to be legitimate.")

# Add some info in the sidebar
st.sidebar.header("About")
st.sidebar.info("""
This app uses:
- **Natural Language Processing** to analyze messages
- **CountVectorizer** for text feature extraction
- **Naive Bayes** classifier
- Trained on the SMS Spam Collection dataset
""")

st.sidebar.header("How to Use")
st.sidebar.info("""
1. Type or paste an SMS message in the text box
2. Click 'Check Message'
3. View the prediction and confidence level
""")