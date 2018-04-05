# EDA packages
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def genderguesser(name):
    print(name)
    # Load our data
    df = pd.read_csv('names_dataset.csv')
    df_names = df
    df_names.sex.replace({'F':0,'M':1},inplace=True)
    Xfeatures =df_names['name']
    # Feature Extraction
    cv = CountVectorizer()
    X = cv.fit_transform(Xfeatures)
    cv.get_feature_names()
    y = df_names.sex
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf = MultinomialNB()
    clf.fit(X_train,y_train)
    clf.score(X_test,y_test)
    sample_name = [name]
    vect = cv.transform(sample_name).toarray()
    x=""
    if clf.predict(vect) == 0:
        x="Female"
    else:
        x="Male"
    return x

