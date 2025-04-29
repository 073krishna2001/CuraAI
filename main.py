import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Session State for Welcome Screen
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0f7fa, #ffffff);
        padding: 10px;
    }
    .stButton>button {
        color: white;
        background-color: #00acc1;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }
    .stSuccess {
        background-color: #b2fab4;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to encode local image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Welcome Page
if st.session_state.page == 'welcome':
    image_path = 'front_bg.jpg'  # Your downloaded image path
    encoded_bg = get_base64_image(image_path)

    # Set the background image using base64 encoding
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_bg}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .welcome-container {{
            text-align: center;
            padding-top: 5px;
            color: black;
        }}
        .welcome-title {{
            font-size: 40px;
            padding-bottom: 100px;
            font-weight: bold;
        }}
        .welcome-subtitle {{
            font-size: 24px;
            margin-top: 150px;
        }}
        </style>
        <div class="welcome-container">
            <div class="welcome-title">👨‍⚕️ Welcome to Health Assistant</div>
            <div class="welcome-subtitle">Predict Your Health Status with AI Assistance</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("\n\n")
    if st.button('Enter Application'):
        st.session_state.page = 'main'
    st.stop()

# Actual Application starts
# getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
breast_cancer_model = pickle.load(open(f'D:/study/8th semester/major_project/final_project/try_11/saved_model/breast_cancer_model.sav', 'rb'))
diabetes_model = pickle.load(open(f'D:/study/8th semester/major_project/final_project/try_11/saved_model/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'D:/study/8th semester/major_project/final_project/try_11/saved_model/heart_disease_model.sav', 'rb'))

# Header Section
st.title("\U0001F468‍⚕️ Health Assistant")
st.subheader("Predict Your Health Condition with Confidence")
st.markdown("---")

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Breast Cancer Prediction',
                            'Diabetes Prediction',
                            'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'person', 'heart'],
                           default_index=0)

def show_doctors_and_precautions(disease, has_disease):
    st.markdown("---")
    if has_disease:
        st.subheader("🏥 Recommended Doctors")
        if disease == 'breast_cancer':
            st.markdown("- [Dr. Meenu Walia](https://www.maxhealthcare.in/doctor/dr-meenu-walia)")
            st.markdown("- [Dr. Harit Chaturvedi](https://www.maxhealthcare.in/doctor/dr-harit-chaturvedi)")
            st.markdown("- [Dr. Pramod Kumar Julka](https://www.maxhealthcare.in/doctor/dr-pramod-kumar-julka)")
        elif disease == 'diabetes':
            st.markdown("- [Dr. Anshu Alok](https://www.maxhealthcare.in/doctor/dr-anshu-alok)")
            st.markdown("- [Dr. Neeru Gera](https://www.maxhealthcare.in/doctor/dr-neeru-gera)")
            st.markdown("- [Dr. Ambrish Mithal](https://www.maxhealthcare.in/doctor/dr-ambrish-mithal)")
        elif disease == 'heart_disease':
            st.markdown("- [Dr. Nakul Sinha](https://www.maxhealthcare.in/doctor/dr-nakul-sinha)")
            st.markdown("- [Dr. Balbir Singh](https://www.maxhealthcare.in/doctor/dr-balbir-singh)")
            st.markdown("- [Dr. Sameer Shrivastava](https://www.maxhealthcare.in/doctor/dr-sameer-shrivastava)")
    else:
        st.subheader("📈 Precautionary Advice")
        if disease == 'breast_cancer':
            st.markdown("-> Maintain a healthy weight - Being overweight, especially after menopause, increases breast cancer risk.")
            st.markdown("-> Eat a healthy diet - Focus on fruits, vegetables, whole grains, and lean proteins. Limit red meat and processed foods.")
            st.markdown("-> Limit alcohol intake - Even small amounts of alcohol can increase breast cancer risk. Ideally, avoid it or limit to one drink a day.")
            st.markdown("-> Limit hormone therapy - Long-term use of combined hormone therapy (for menopause symptoms) can increase risk. Discuss safer options with your doctor.")
            st.markdown("-> Get regular screenings - Mammograms and clinical breast exams can help detect cancer early, when it's most treatable.")

        elif disease == 'diabetes':
            st.markdown("-> Maintain a healthy weight - Excess weight, especially around the abdomen, increases the risk of type 2 diabetes.")
            st.markdown("-> Exercise regularly - Aim for at least 30 minutes of moderate physical activity most days—like walking, cycling, or swimming.")
            st.markdown("-> Stay hydrated with water - Water helps control blood sugar levels and avoids sugary drink intake.")
            st.markdown("-> Monitor blood sugar levels (if at risk or diagnosed) - Regular checks help you catch any rise early and manage it properly.")
            st.markdown("-> Manage stress - Stress hormones can raise blood sugar levels. Practice meditation, breathing exercises, or hobbies you enjoy.")

        elif disease == 'heart_disease':
            st.markdown("-> Eat a heart-healthy diet - Focus on fruits, vegetables, whole grains, lean proteins (like fish and legumes), and healthy fats (like olive oil).")
            st.markdown("-> Exercise regularly - Aim for at least 30 minutes of moderate exercise (like brisk walking) most days of the week.")
            st.markdown("-> Manage cholesterol levels -  High LDL (bad cholesterol) can lead to blocked arteries. Eat healthy and take medicines if prescribed.")
            st.markdown("- Limit alcohol - Drink in moderation—up to one drink a day for women and two for men.")
            st.markdown("- Get regular health checkups -  Regular screening can catch early signs of trouble like hypertension, high cholesterol, or diabetes.")

# Pages
if selected == 'Breast Cancer Prediction':
    st.header('Breast Cancer Prediction')
    st.info('Please fill out the following details:')

    input_fields = ['Radius Mean', 'Texture Mean', 'Perimeter Mean', 'Area Mean', 'Smoothness Mean', 'Compactness Mean', 'Concavity Mean', 'Concave Points Mean', 'Symmetry Mean', 'Fractal Dimension Mean',
                    'Radius SE', 'Texture SE', 'Perimeter SE', 'Area SE', 'Smoothness SE', 'Compactness SE', 'Concavity SE', 'Concave Points SE', 'Symmetry SE', 'Fractal Dimension SE',
                    'Radius Worst', 'Texture Worst', 'Perimeter Worst', 'Area Worst', 'Smoothness Worst', 'Compactness Worst', 'Concavity Worst', 'Concave Points Worst', 'Symmetry Worst', 'Fractal Dimension Worst']

    user_input = []
    for i in range(0, len(input_fields), 3):
        col1, col2, col3 = st.columns(3)
        with col1:
            user_input.append(st.text_input(input_fields[i]))
        with col2:
            if i+1 < len(input_fields):
                user_input.append(st.text_input(input_fields[i+1]))
        with col3:
            if i+2 < len(input_fields):
                user_input.append(st.text_input(input_fields[i+2]))

    cancer_diagnosis = ''

    if st.button('Predict Breast Cancer'):
        try:
            processed_input = [float(x) for x in user_input]
            prediction = breast_cancer_model.predict([processed_input])
            if prediction[0] == 1:
                cancer_diagnosis = 'The person has breast cancer'
            else:
                cancer_diagnosis = 'The person does not have breast cancer'
        except:
            cancer_diagnosis = '⚠️ Invalid input values!'

    st.success(cancer_diagnosis)
    if cancer_diagnosis:
        show_doctors_and_precautions('breast_cancer', 'has breast cancer' in cancer_diagnosis)

if selected == 'Diabetes Prediction':
    st.header('Diabetes Prediction')
    st.info('Please fill out the following details:')

    fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    user_input = []
    col1, col2, col3 = st.columns(3)
    for idx, field in enumerate(fields):
        with [col1, col2, col3][idx % 3]:
            user_input.append(st.text_input(field))

    diab_diagnosis = ''

    if st.button('Predict Diabetes'):
        try:
            processed_input = [float(x) for x in user_input]
            prediction = diabetes_model.predict([processed_input])
            if prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except:
            diab_diagnosis = '⚠️ Invalid input values!'

    st.success(diab_diagnosis)
    if diab_diagnosis:
        show_doctors_and_precautions('diabetes', 'is diabetic' in diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.header('Heart Disease Prediction')
    st.info('Please fill out the following details:')

    fields = ['Age', 'Sex', 'Chest Pain types (cp)', 'Resting Blood Pressure (trestbps)', 'Serum Cholestoral in mg/dl(chol)', 'Fasting Blood Sugar > 120 mg/dl (fbs)',
              'Resting Electrocardiographic results (restecg)', 'Maximum Heart Rate achieved (thalach)', 'Exercise Induced Angina (exang)',
              'ST depression induced by exercise (oldpeak)', 'Slope of peak exercise ST segment (slope)', 'Major vessels colored by flourosopy (ca)', 'Thal']

    user_input = []
    col1, col2, col3 = st.columns(3)
    for idx, field in enumerate(fields):
        with [col1, col2, col3][idx % 3]:
            user_input.append(st.text_input(field))

    heart_diagnosis = ''

    if st.button('Predict Heart Disease'):
        try:
            processed_input = [float(x) for x in user_input]
            prediction = heart_disease_model.predict([processed_input])
            if prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
        except:
            heart_diagnosis = '⚠️ Invalid input values!'

    st.success(heart_diagnosis)
    if heart_diagnosis:
        show_doctors_and_precautions('heart_disease', 'has heart disease' in heart_diagnosis)
