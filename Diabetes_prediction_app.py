
import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/Desktop/ML/Diabetes Prediction/trained_model.sav', 'rb'))

def diabetes_predcition(input_data):

# changing the input_data to numpy array
    input_data_as_numpy_array = np.array(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
#std_data = scaler.transform(input_data_reshaped)
#print(std_data)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
  

def main():
      #giving title
      st.title('Diabetic Prediction Web based Application')
      
      #getting input data from the user
      
      Pregnancies = st.text_input('Number of Pregnancies')
      Glucose = st.text_input('Glucose level')
      BloodPressure = st.text_input('Blood Pressure Value')
      SkinThickness = st.text_input('Skin thinkness value')
      Insulin = st.text_input('Insulin Level') 
      BMI = st.text_input('BMI value')
      DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function value ')
      Age = st.text_input('Age of the person')
      
      #code for prediction
      diagnosis =''
      #creating a button for prediction
      if st.button('Dibetes Test Result'):
          diagnosis = diabetes_predcition([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
          
      st.success(diagnosis)
      
      
      
if __name__ =='__main__':
    main()