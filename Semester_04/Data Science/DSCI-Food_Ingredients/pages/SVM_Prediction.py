import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score
import streamlit as st
st.set_page_config(layout='wide')
df = pd.read_csv('cleaned_food.csv')
df.dropna(inplace=True)
df.drop(['Unnamed: 0'],axis=1,inplace=True)

output= df['size']
features = df.drop(['size'],axis=1)

print (output)
print(features.columns)

output,uniques = pd.factorize(output)
features =  pd.get_dummies(features)

x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.5, random_state=42)
SVM_model = svm.SVC()

SVM_model.fit(x_train, y_train)

y_train_pred = SVM_model.predict(x_train)
y_test_pred = SVM_model.predict(x_test)

train_accuracy = accuracy_score(y_train_pred, y_train)
test_accuracy = accuracy_score(y_test_pred, y_test)
train_f1score = f1_score(y_train_pred, y_train,average='weighted')
test_f1score = f1_score(y_test_pred, y_test,average='weighted')

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

print("Training Accuracy:", train_f1score)
print("Testing Accuracy:", test_f1score)


st.header('SVM Model Page')

with st.form('Input'):
    col1, col2,col3,col4 = st.columns((0.2,0.2,0.2,0.4))
    with col1:
        calories_kcal = st.number_input("Enter calories (kcal)", min_value=0.0, step=0.1)
        fats_g = st.number_input("Enter fats (g)", min_value=0.0, step=0.1)
        sod_mg = st.number_input("Enter sodium (mg)", min_value=0.0, step=0.1)
        carb_g = st.number_input("Enter carbohydrates (g)", min_value=0.0, step=0.1)
        fiber_g = st.number_input("Enter fiber (g)", min_value=0.0, step=0.1)
        sugar_g = st.number_input("Enter sugar (g)", min_value=0.0, step=0.1)
        protein_g = st.number_input("Enter protein (g)", min_value=0.0, step=0.1)
        vitA_g = st.number_input("Enter vitamin A (g)", min_value=0.0, step=0.1)
        calcium_mg = st.number_input("Enter calcium (mg)", min_value=0.0, step=0.1)

    with col2:
        thiamin_mg = st.number_input("Enter thiamin (mg)", min_value=0.0, step=0.1)
        zinc_mg = st.number_input("Enter zinc (mg)", min_value=0.0, step=0.1)
        potassium_mg = st.number_input("Enter potassium (mg)", min_value=0.0, step=0.1)
        magnesium_mg = st.number_input("Enter magnesium (mg)", min_value=0.0, step=0.1)
        vitE_mg = st.number_input("Enter vitamin E (mg)", min_value=0.0, step=0.1)
        vitK_mcg = st.number_input("Enter vitamin K (mcg)", min_value=0.0, step=0.1)
        vitC_mg = st.number_input("Enter vitamin C (mg)", min_value=0.0, step=0.1)
        vitB6_mg = st.number_input("Enter vitamin B6 (mg)", min_value=0.0, step=0.1)

    with col3:
        copper_mg = st.number_input("Enter copper (mg)", min_value=0.0, step=0.1)
        carotene_mg = st.number_input("Enter carotene (mg)", min_value=0.0, step=0.1)
        carotene_mcg = st.number_input("Enter carotene (mcg)", min_value=0.0, step=0.1)
        cryptoxanthin_mcg = st.number_input("Enter cryptoxanthin (mcg)", min_value=0.0, step=0.1)
        lycopene_mcg = st.number_input("Enter lycopene (mcg)", min_value=0.0, step=0.1)
        cholesterol_mg = st.number_input("Enter cholesterol (mg)", min_value=0.0, step=0.1)
        quality = st.number_input("Enter quality", min_value=0, step=1)
        button = st.form_submit_button()
        
    with col4:
        if button is True:
            new_prediction = SVM_model.predict([[calories_kcal,fats_g,sod_mg,carb_g,fiber_g,sugar_g,protein_g,vitA_g,calcium_mg,thiamin_mg,zinc_mg,potassium_mg,magnesium_mg,vitE_mg,vitK_mcg,vitC_mg,vitB6_mg,copper_mg,carotene_mg,carotene_mcg,cryptoxanthin_mcg,lycopene_mcg,cholesterol_mg,quality]])
            prediction = uniques[new_prediction][0]
            st.write(f'Accuracy: {round(test_accuracy,1)*100}%')
            st.write(f'F1 Score: {round(test_f1score,1)*100}%')
            st.write(f'Set of size predict :{prediction}')
    


