import pickle
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

STOP_WORDS = set(stopwords.words('english'))

with open('stopwords.pkl', 'wb') as f:
    pickle.dump(STOP_WORDS, f)
