import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
import pickle 

penguin_df = pd.read_csv('Data Science\Machine Learning\penguins.csv')


#target variable 
penguin_df.dropna(inplace=True) 

#features variable
output = penguin_df['species'] 

features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']] 

print (features)
features = pd.get_dummies(features) 
print (features)

print (output)
output, uniques = pd.factorize(output) 
print (output)

x_train, x_test, y_train, y_test = train_test_split(
	features, output, test_size=.2) 
print(len(x_train))
print(len(x_test))

rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train, y_train) 
y_pred = rfc.predict(x_test) 
score = accuracy_score(y_pred, y_test)
 
print('Our accuracy score for this model is {}'.format(score)) 
 
# with open(r"C:\Users\yamin\Documents\GitHub\Nimayka_Coding\Semester_04\Data Science\Machine Learning", 'wb') as rf_pickle:
# 	pickle.dump(rfc, rf_pickle) 
# 	rf_pickle.close() 
 
# with open('C:\Users\yamin\Documents\GitHub\Nimayka_Coding\Semester_04\Data Science\Machine Learning', 'wb', encoding='utf-8') as output_pickle:
# 	pickle.dump(uniques, output_pickle) 
# 	output_pickle.close() 

fig, ax = plt.subplots() 
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns) 
plt.title('Which features are the most important for species prediction?') 
plt.xlabel('Importance') 
plt.ylabel('Feature') 
plt.tight_layout() 
fig.savefig('feature_importance.png') 