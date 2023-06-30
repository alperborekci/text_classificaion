# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 23:56:43 2023

@author: AlperB
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os, re, glob
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from googletrans import Translator
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os, re, glob
from sklearn.preprocessing import LabelEncoder
from collections import Counter
#from googletrans import Translator
import numpy as np
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn import metrics



dataset= pd.read_excel('results.xlsx')
#print(dataset.head())
#dataset = dataset.drop(['Unnamed: 1'], axis=1)
print(dataset.describe())

sum_ = Counter(dataset['thema']).values()
class_ = Counter(dataset['thema']).keys()
df_class = pd.DataFrame(zip(class_,sum_), columns = ['thema', 'Toplam'])
df_class=df_class.dropna()
plt.figure(figsize=(20,10),dpi=300)
sns.set(color_codes=True)
sns.distplot(df_class.Toplam,rug = True, kde_kws={"color": "k"}, hist_kws={"color" : "r"});
plt.savefig('themalar.png')
plt.figure(figsize=(30,10),dpi=300)
sns.set(color_codes=True)

#sns.lineplot(x = "thema", y = "Toplam", data = df_class, ax = ax[0,0]);
sns.barplot(y = df_class.thema, x= df_class.Toplam, palette='vlag', orient="h",order=df_class.sort_values('Toplam',ascending = False).thema)

#plt.xticks(rotation=45)
plt.savefig('sınıfdagılım.png')
#dataset.to_excel('./data.xlsx')

df=dataset
print(df.head())



#%% Ön işleme 

import nltk
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
import string
from nltk.corpus import stopwords


nltk.download('stopwords')
WPT = nltk.WordPunctTokenizer()
stop_word_list = nltk.corpus.stopwords.words('german')

def stopword_extraction(values):
    wordFilter = [word for word in values.split() if word not in stop_word_list]
    notStopword = " ".join(wordFilter)
    return notStopword
 

#%%
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5,
                        ngram_range=(1, 4), 
                        stop_words=stopwords.words('german'))
# We transform each complaint into a vector
features = tfidf.fit_transform(df.text).toarray()
labels = df.category_id
print("Each of the %d complaints is represented by %d features (TF-IDF score of unigrams and bigrams)" %(features.shape))

#%%

from sklearn.neighbors import KNeighborsClassifier
#from lightgbm import LGBMClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier

X = features # Collection of documents
y = labels # Target or the labels we want to predict (i.e., the 13 different complaints of products)

#%%
models = [
        #LGBMClassifier(),
        #AdaBoostClassifier(),
        LogisticRegression(C=0.1,penalty="l2",max_iter=250),
        #SVC(kernel='linear',C=3),
        GaussianNB(),
        DecisionTreeClassifier(),
       #GradientBoostingClassifier(),
        KNeighborsClassifier(n_neighbors=3),
    RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0),
    LinearSVC(),
    #MultinomialNB(),
    #LogisticRegression(random_state=0),
]
# 5 Cross-validation
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))

entries = []
for model in models:
  model_name = model.__class__.__name__
  accuracies = cross_val_score(model, X, y, scoring='accuracy', cv=CV)
  for fold_idx, accuracy in enumerate(accuracies):
    entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])


#%%
mean_accuracy = cv_df.groupby('model_name').accuracy.mean()
std_accuracy = cv_df.groupby('model_name').accuracy.std()

acc = pd.concat([mean_accuracy, std_accuracy], axis= 1, 
          ignore_index=True)
acc.columns = ['Mean Accuracy', 'Standard deviation']
print(acc)

#görselleştirme
plt.figure(figsize=(8,5))
ax=sns.boxplot(x='model_name', y='accuracy', 
            data=cv_df, 
            color='lightblue', 
            showmeans=True)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
plt.title("Mean Accuracy (cv = 10)n", size=14);
#%%

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.30, 
                                                               random_state=42)
#%%

model = LinearSVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Classification report
print('ttttCLASSIFICATIION METRICSn')
print(metrics.classification_report(y_test, y_pred))


#%%
import seaborn as sns
conf_matrix=confusion_matrix(y_test, y_pred)
lables=['Abschiedslieder','Allgemein','Arbeitslieder','Balladen','Deutschlandlieder und Vaterlandsgesänge',
        'Frauenlieder','Geistliche Lieder','Heimatlieder','Jägerlieder','Jahreskreislauf',
        'Kinderlieder','Liebeslieder','Politische Lieder','Scherzlieder','Soldatenlieder',
        'Sportlieder','Tanzlieder','Trinklieder','Wanderlieder','Weihnachtslieder','Witzesammlung']
# Change figure size and increase dpi for better resolution
plt.figure(figsize=(15,12), dpi=300)
# Scale up the size of all text
sns.set(font_scale = 1.0)
plt.title('Confusion Matrix of The Classifier')
# Plot Confusion Matrix using Seaborn heatmap()
# Parameters:
# first param - confusion matrix in array format   
# annot = True: show the numbers in each heatmap cell
# fmt = 'd': show numbers as integers. 
ax = sns.heatmap(conf_matrix, annot=True, fmt='d', )

# set x-axis label and ticks. 
ax.set_xlabel("Predicted Diagnosis", fontsize=14, labelpad=20)
ax.xaxis.set_ticklabels(['']+lables)

# set y-axis label and ticks
ax.set_ylabel("Actual Diagnosis", fontsize=14, labelpad=20)
ax.yaxis.set_ticklabels(['']+lables)

# set plot title
ax.set_title("Confusion Matrix for the Volkslieder Detection Model", fontsize=14, pad=20)

plt.show()





