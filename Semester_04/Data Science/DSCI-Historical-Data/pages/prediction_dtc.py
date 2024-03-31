import streamlit as st
import pandas as pd 
import pickle 
import sys

# Add the path to the modelling module if it's in a different directory
sys.path.append('path/to/modelling/module')

# Function to load the model and output data from pickle files
def load_model_and_output(model_file, output_file):
    try:
        with open(model_file, 'rb') as model_pickle, open(output_file, 'rb') as output_pickle:
            model = pickle.load(model_pickle)
            output = pickle.load(output_pickle)
        return model, output
    except FileNotFoundError:
        st.error("Model or output files not found.")
        return None, None

# Streamlit app title
st.title('Death Prediction using Decision Tree')

# Load the trained Decision Tree model and output data
model_file_path = 'dtc.pickle'  # Path to the trained model file
output_file_path = 'dtc_output.pickle'  # Path to the output file
decision_tree_model, uniques = load_model_and_output(model_file_path, output_file_path)

# Load the dataset
data = pd.read_csv('cause_of_deaths.csv')

# Filter options
selected_year = st.selectbox('Select year:', data['Year'].unique())
selected_country = st.selectbox('Select country:', data['Country/Territory'].unique())
selected_disease = st.selectbox('Select disease:', data.columns[3:], index=0)  # Default to the first disease

# Add a submit button
submit_button = st.button('Submit')

# Process user input when the submit button is clicked
if submit_button:
    # Filter data based on user selections
    filtered_data = data[(data['Year'] == selected_year) &
                         (data['Country/Territory'] == selected_country) &
                         (data[selected_disease] == 1)]

    # Display predictions
    if not filtered_data.empty:
        if decision_tree_model is not None:
            # Make predictions using the loaded model
            predictions_proba = decision_tree_model.predict_proba(filtered_data)[:, 1]  # Probabilities for the positive class

            # Define a threshold to classify instances
            threshold = 0.5  # Adjust as needed

            # Classify instances based on probabilities
            predictions = ['High Possibility' if prob >= threshold else 'Low Possibility' for prob in predictions_proba]

            # Display the predictions
            st.write(predictions)
        else:
            st.error("Model could not be loaded.")
    else:
        st.write('No data available for the selected filters.')
