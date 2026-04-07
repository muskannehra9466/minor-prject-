import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Zaroori files download karna
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
        # 1. Lowercase aur Tokenize
        tokens = word_tokenize(text.lower())
        
        # 2. Stopwords hatana aur sirf kaam ke words rakhna
        # isalnum() se punctuation (!, @, #) hat jayenge
        cleaned = [w for w in tokens if w.isalnum() and w not in self.stop_words]
        
        # 3. Lemmatization (Words ko unki basic form mein lana)
        # Example: 'studies' becomes 'study'
        lemmatized = [self.lemmatizer.lemmatize(w) for w in cleaned]
        
        return lemmatized

    def get_main_topic(self, text):
        # Ye function main topic nikaalne ke liye hai
        words = self.clean_text(text)
        # Filhal hum pehla bada word ya sabhi words return kar rahe hain
        return " ".join(words)

# Test karne ke liye (check if it works)
if __name__ == "__main__":
    processor = TextProcessor()
    sample_query = "Explain the process of Photosynthesis in plants!"
    print(f"Original: {sample_query}")
    print(f"Processed Keywords: {processor.clean_text(sample_query)}")