import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
import pickle 
import streamlit as st

iris_df = pd.read_csv('Iris (1).csv') 
iris_df.dropna(inplace=True) 
output = iris_df['Species'] 
features = iris_df[['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

features = pd.get_dummies(features) 
output, uniques = pd.factorize(output) 

x_train, x_test, y_train, y_test = train_test_split(
	features, output, test_size=.2) 
print(len(x_train))
print(len(x_test))


#declaring randomforestclassifier
rfc = RandomForestClassifier(random_state=35) 
rfc.fit(x_train, y_train)

#prediction = y_pred
y_pred = rfc.predict(x_test)  #testset

#Evaluation - accuracy? precision etc
score = accuracy_score(y_pred, y_test)
 
print('Our accuracy score for rfc model is {}'.format(score)) 


dtc = DecisionTreeClassifier(random_state=35)
dtc.fit(x_train, y_train)
#prediction = y_pred
y_pred_dtc = dtc.predict(x_test)  #testset

#Evaluation - accuracy? precision etc
score_dtc = accuracy_score(y_pred_dtc, y_test)
 
print('Our accuracy score for dtc model is {}'.format(score_dtc)) 

 
with open('TT', 'wb') as rf_pickle:
	pickle.dump(rfc, rf_pickle) 
	rf_pickle.close() 
with open('TT', 'wb') as output_pickle:
	pickle.dump(uniques, output_pickle) 
	output_pickle.close() 

fig, ax = plt.subplots() 
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns) 
plt.title('Which features are the most important for species prediction?') 
plt.xlabel('Importance') 
plt.ylabel('Feature') 
plt.tight_layout() 
fig.savefig('feature_importance.png') 

print(features)
print(output)
print(y_pred)