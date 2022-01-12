# Natural Language Processing & Sentiment Analysis
# 1. pip install textblob

from textblob import TextBlob
text = 'Tomorroe will be great weekend for us'
blob = TextBlob('text')
blob.detect_language()
chinese = blob.translate(to='zh')
spanish = blob.translate(to='es')

# Polarity: -1.0 (Negative) to 1.0 (Positive)
# Subjectivity: 0.0 (Objective) to 1.0 (Subjective)
blob.sentiment

text1 = 'Yesterday was a beautiful day, but today looks like bad weather'
blob1 = TextBlob(text1)
blob1.sentiment

blob2 = TextBlob(Path('RomeoandJuliet.txt').read_text())
items = blob.word_counts.item()
