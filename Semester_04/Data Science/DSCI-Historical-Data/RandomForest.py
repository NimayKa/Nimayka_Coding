import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

data = pd.read_csv('cause_of_deaths.csv')
data = data.drop(['Country/Territory', 'Code', 'Year'], axis=1)
data['mortality'] = data.sum(axis=1)
output = data['mortality']
features = data.drop(['mortality'],axis=1)

output,uniques = pd.factorize(output)
features =  pd.get_dummies(features)
print (features)
print (output)

x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.5, random_state=42)
random_forest_model = RandomForestClassifier()

random_forest_model.fit(x_train, y_train)

y_test_pred = random_forest_model.predict(x_test)

test_accuracy = accuracy_score(y_test_pred, y_test)
# test_precision = precision_score(y_test_pred, y_test)

print("Testing Accuracy:", test_accuracy)
# print("Testing Accuracy:", test_precision)

# print("Classification Report:")
# print(classification_report(y_test, y_test_pred))

with st.form('user_inputs'):
    meningitis_deaths = st.number_input(label='Input deaths for Meningitis', value=0)
    alzheimers_deaths = st.number_input(label='Input deaths for Alzheimers Disease and Other Dementias', value=0)
    parkinsons_deaths = st.number_input(label='Input deaths for Parkinsons Disease', value=0)
    nutritional_deaths = st.number_input(label='Input deaths for Nutritional Deficiencies', value=0)
    malaria_deaths = st.number_input(label='Input deaths for Malaria', value=0)
    drowning_deaths = st.number_input(label='Input deaths for Drowning', value=0)
    interpersonal_deaths = st.number_input(label='Input deaths for Interpersonal Violence', value=0)
    maternal_deaths = st.number_input(label='Input deaths for Maternal Disorders', value=0)
    hiv_deaths = st.number_input(label='Input deaths for HIV/AIDS', value=0)
    drug_deaths = st.number_input(label='Input deaths for Drug Use Disorders', value=0)
    tuberculosis_deaths = st.number_input(label='Input deaths for Tuberculosis', value=0)
    cardiovascular_deaths = st.number_input(label='Input deaths for Cardiovascular Diseases', value=0)
    lower_respiratory_deaths = st.number_input(label='Input deaths for Lower Respiratory Infections', value=0)
    neonatal_deaths = st.number_input(label='Input deaths for Neonatal Disorders', value=0)
    alcohol_use_deaths = st.number_input(label='Input deaths for Alcohol Use Disorders', value=0)
    self_harm_deaths = st.number_input(label='Input deaths for Self-harm', value=0)
    forces_of_nature_deaths = st.number_input(label='Input deaths for Exposure to Forces of Nature', value=0)
    diarrheal_deaths = st.number_input(label='Input deaths for Diarrheal Diseases', value=0)
    environmental_deaths = st.number_input(label='Input deaths for Environmental Heat and Cold Exposure', value=0)
    neoplasms_deaths = st.number_input(label='Input deaths for Neoplasms', value=0)
    conflict_terrorism_deaths = st.number_input(label='Input deaths for Conflict and Terrorism', value=0)
    diabetes_deaths = st.number_input(label='Input deaths for Diabetes Mellitus', value=0)
    chronic_kidney_deaths = st.number_input(label='Input deaths for Chronic Kidney Disease', value=0)
    poisonings_deaths = st.number_input(label='Input deaths for Poisonings', value=0)
    malnutrition_deaths = st.number_input(label='Input deaths for Protein-Energy Malnutrition', value=0)
    road_injuries_deaths = st.number_input(label='Input deaths for Road Injuries', value=0)
    respiratory_deaths = st.number_input(label='Input deaths for Chronic Respiratory Diseases', value=0)
    cirrhosis_deaths = st.number_input(label='Input deaths for Cirrhosis and Other Chronic Liver Diseases', value=0)
    digestive_deaths = st.number_input(label='Input deaths for Digestive Diseases', value=0)
    fire_deaths = st.number_input(label='Input deaths for Fire, Heat, and Hot Substances', value=0)
    hepatitis_deaths = st.number_input(label='Input deaths for Acute Hepatitis', value=0)
    button = st.form_submit_button()
    
if button is True:
    new_prediction = random_forest_model.predict([[meningitis_deaths , alzheimers_deaths , parkinsons_deaths , nutritional_deaths ,
    malaria_deaths , drowning_deaths , interpersonal_deaths , maternal_deaths ,
    hiv_deaths , drug_deaths , tuberculosis_deaths , cardiovascular_deaths ,
    lower_respiratory_deaths , neonatal_deaths , alcohol_use_deaths , self_harm_deaths ,
    forces_of_nature_deaths , diarrheal_deaths , environmental_deaths , neoplasms_deaths ,
    conflict_terrorism_deaths , diabetes_deaths , chronic_kidney_deaths , poisonings_deaths ,
    malnutrition_deaths , road_injuries_deaths , respiratory_deaths , cirrhosis_deaths ,
    digestive_deaths , fire_deaths , hepatitis_deaths]]) 
    prediction = uniques[new_prediction][0]
    
    st.write(f'F1 Score: {round(test_accuracy,1)*100}%')
    st.write(f'Mortality rate: {prediction}')