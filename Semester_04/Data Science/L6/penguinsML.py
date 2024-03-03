import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
import pickle 
import os


#get current directory
currrent_directory = os.getcwd()
#place folder path into variable, if folder isnt exist it will create a new one for you
file_path = os.path.join(currrent_directory,'rfc.pickle')
file2 = os.path.join(currrent_directory,'penguins.csv')


penguin_df = pd.read_csv(r'C:\Users\yamin\Documents\GitHub\Nimayka_Coding\Semester_04\Data Science\L4\penguins.csv') 

penguin_df.dropna(inplace=True) 
output = penguin_df['species'] 
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']] 

features = pd.get_dummies(features) 
output, uniques = pd.factorize(output) 

x_train, x_test, y_train, y_test = train_test_split(
	features, output, test_size=.2) 
print(len(x_train))
print(len(x_test))

rfc = RandomForestClassifier(random_state=15) 
rfc.fit(x_train, y_train) 
y_pred = rfc.predict(x_test) 
score = accuracy_score(y_pred, y_test)
 
print('Our accuracy score for this model is {}'.format(score)) 
 
#Store Model
with open(file_path, 'wb') as rf_pickle:
	pickle.dump(rfc, rf_pickle) 
	rf_pickle.close() 
 
file_path2 = os.path.join(currrent_directory,'output.pickle')
#Passing Mapping Value
with open(file_path2, 'wb') as output_pickle:
	pickle.dump(uniques, output_pickle) 
	output_pickle.close() 

fig, ax = plt.subplots() 
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns) 
plt.title('Which features are the most important for species prediction?') 
plt.xlabel('Importance') 
plt.ylabel('Feature') 
plt.tight_layout() 
fig.savefig('feature_importance.png') 