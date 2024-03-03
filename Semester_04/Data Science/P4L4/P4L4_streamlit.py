import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
import pickle 
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
 
st.title('Iris Classifier') 

st.write("This app uses 4 inputs to predict the Species of Iris Species") 

iris_file = st.file_uploader('Upload your own iris data') 

if iris_file is None: 

    rf_pickle = open('rfc.pickle', 'rb') 

    map_pickle = open('output.pickle', 'rb') 
    
    iris_df=  None

    rfc = pickle.load(rf_pickle) 

    unique_iris_mapping = pickle.load(map_pickle) 

    rf_pickle.close() 

    map_pickle.close() 

else: 

    iris_df = pd.read_csv(iris_file) 

    iris_df = iris_df.dropna() 

    output = iris_df['Species'] 

    features = iris_df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

    features = pd.get_dummies(features) 

    output, unique_iris_mapping = pd.factorize(output) 

    x_train, x_test, y_train, y_test = train_test_split( 

        features, output, test_size=.8) 

    rfc = RandomForestClassifier(random_state=15) 

    rfc.fit(x_train, y_train) 

    y_pred = rfc.predict(x_test) 

    score = round(accuracy_score(y_pred, y_test), 2) 

    st.write('We trained a Random Forest model on these data,' 
             ' it has a score of {}!' 
             .format(score))
    
    dtc = DecisionTreeClassifier(random_state=15)
    dtc.fit(x_train, y_train)
    y_pred_dtc = dtc.predict(x_test)
    score_dtc = round(accuracy_score(y_pred_dtc, y_test), 2)

    st.write('We trained a Decision Tree model on these data,' 
         ' it has a score of {}!'.format(score_dtc))

with st.form('user_inputs'): 
  Sepal_length = st.number_input(
    'Sepal Length (Cm)', min_value=0) 
  Sepal_width = st.number_input(
    'Sepal Width (Cm)', min_value=0) 
  Petal_length = st.number_input(
    'Petal Length (Cm)', min_value=0) 
  Petal_width = st.number_input(
    'Petal Width (Cm)', min_value=0) 
  submit= st.form_submit_button('submit') 
  # Assuming you're still using Streamlit's input form
  
if submit== True:
    new_prediction = rfc.predict(pd.DataFrame({
        'SepalLengthCm': [Sepal_length],
        'SepalWidthCm': [Sepal_width],
        'PetalLengthCm': [Petal_length],
        'PetalWidthCm': [Petal_width]
    
    }))
    new_prediction1 = dtc.predict(pd.DataFrame({
        'SepalLengthCm': [Sepal_length],
        'SepalWidthCm': [Sepal_width],
        'PetalLengthCm': [Petal_length],
        'PetalWidthCm': [Petal_width]
    
    }))

prediction_species = unique_iris_mapping[new_prediction][0]
prediction_species1 = unique_iris_mapping[new_prediction1][0]
st.write('We predict your iris is of the {} Species'.format(prediction_species)) 
st.write('We predict your iris is of the {} Species'.format(prediction_species1)) 

st.subheader("Predicting Your iris's Species:")
st.write('We predict your iris is of the {} Species'
.format(prediction_species))
st.write('We used a machine learning (Random Forest) model and (Decision Tree) Model to '
'predict the Species, the features used in this prediction '
' are ranked by relative importance below.')
st.image('feature_importance.png')

if iris_df is None:
    st.write('Please Upload Your Dataset')
else:
    
    st.write('Below are the histograms for each continuous variable '
    'separated by iris Species. The vertical line '
    'represents your the inputted value.')
    fig, ax = plt.subplots()
    ax = sns.displot(x=iris_df['SepalLengthCm'],
    hue=iris_df['Species'])
    plt.axvline(Sepal_length)
    plt.title('Speal Length by Species')
    st.pyplot(ax)

    fig, ax = plt.subplots()
    ax = sns.displot(x=iris_df['SepalWidthCm'],
    hue=iris_df['Species'])
    plt.axvline(Sepal_width)
    plt.title('Sepal Width by Species')
    st.pyplot(ax)

    fig, ax = plt.subplots()
    ax = sns.displot(x=iris_df['PetalLengthCm'],
    hue=iris_df['Species'])
    plt.axvline(Petal_length)
    plt.title('Flipper Length by Species')
    st.pyplot(ax)

    fig, ax = plt.subplots()
    ax = sns.displot(x=iris_df['PetalWidthCm'],
    hue=iris_df['Species'])
    plt.axvline(Petal_width)
    plt.title('Flipper Length by Species')
    st.pyplot(ax)
