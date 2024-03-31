import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pickle 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC  # Import SVC for Support Vector Machine
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder
import streamlit as st

current_directory = os.getcwd()
print(current_directory)
file_path = os.path.join(current_directory, 'svm.pickle')  # Change the file path for the SVM model
file_path2 = os.path.join(current_directory, 'svm_output.pickle')  # Change the file path for the output
df = pd.read_csv('cause_of_deaths.csv')

# Filter options
countries = df['Country/Territory'].unique()
years = df['Year'].unique()
diseases = df.columns[3:]  # Assuming the diseases start from the fourth column

# Streamlit filters
selected_country = st.selectbox("Select Country/Territory", countries)
year_range = st.slider("Select Year Range", min_value=min(years), max_value=max(years), value=(min(years), max(years)))
selected_disease = st.selectbox("Select Disease", diseases)
submit = st.button("Submit")

if submit:
    filtered_df = df[(df['Country/Territory'] == selected_country) & (df['Year'].between(year_range[0], year_range[1]))]
    selected_disease_col = filtered_df[selected_disease]
    select = selected_disease_col.name

    output, uniques = pd.factorize(selected_disease_col)
    cat_features = filtered_df[['Country/Territory', 'Code', 'Year']]
    num_features = filtered_df.drop(columns=['Country/Territory', 'Code', 'Year', select])

    encoders = {}
    for feature in cat_features:
        encoder = LabelEncoder()
        encoded_values = encoder.fit_transform(cat_features[feature])
        cat_features.loc[:, feature] = encoded_values
        encoders[feature] = encoder

    output, uniques = pd.factorize(output)
    num_features = pd.get_dummies(num_features)
    features = pd.concat([cat_features, num_features], axis=1)

    # Adjust train-test split
    num_train_samples = int(len(features) * 0.7)
    x_train, x_test, y_train, y_test = train_test_split(features, output, train_size=num_train_samples, random_state=42)

    # Change the classifier to SVC (Support Vector Machine)
    svm_model = SVC(kernel='linear')  # You can specify different kernels as needed

    svm_model.fit(x_train, y_train)

    y_train_pred = svm_model.predict(x_train)

    train_accuracy = accuracy_score(y_train_pred, y_train)
    train_f1 = f1_score(y_train_pred, y_train, average='weighted')

    st.write("Training Accuracy:", train_accuracy)
    st.write("Training F1 Score:", train_f1)

    with open(file_path, 'wb') as rf_pickle:
        pickle.dump(svm_model, rf_pickle)
        rf_pickle.close()

    with open(file_path2, 'wb') as output_pickle:
        pickle.dump(uniques, output_pickle)
        output_pickle.close()

    # Since SVM doesn't provide feature importances, we'll skip generating feature importance plot

    st.write("SVM model does not provide feature importances.")
