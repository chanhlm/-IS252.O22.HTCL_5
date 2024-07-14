import streamlit as st
import numpy as np
import pickle
import pandas as pd


# LOAD DTS cho MinMaxScaler
with open('../Scaler/minmax_scaler.pkl', 'rb') as model_scaler:
    model_scaler = pickle.load(model_scaler)


# Set the page title
st.set_page_config(layout="centered",page_title="PROJECT: Predicting Diabetes risk using a classification algorithm",
                   page_icon=":alembic:")

# Set sidebar
# st.title('PROJECT: CRYPTOCURRENCY PREDICTION USING MACHINE LEARNING')
# Replace with the actual path to your image
image_path = "./images/diabetes.png"
st.sidebar.image(image_path, use_column_width=True)
st.sidebar.title('`Predicting diabetes`')
st.sidebar.markdown('Lecturer: **Phd. Cao Thi Nhan**  \n Instructor: **MSc. Vu Minh Sang**')
st.sidebar.write(' The Team:\n'
                 ' - 21520596 – Tran Thi Kim Anh\n'
                 ' - 21521049 – Ho Quang Lam\n'
                 ' - 21521586 – Le Thi Le Truc\n'
                 ' - 21521882 – Le Minh Chanh\n')
    
# Load models =========================
with open('./Models/knn.pkl', 'rb') as knn_model_file:
    knn_model = pickle.load(knn_model_file)
with open('./Models/svm.pkl', 'rb') as svm_model_file:
    svm_model = pickle.load(svm_model_file)
with open('./Models/rf.pkl', 'rb') as rf_model_file:
    rf_model = pickle.load(rf_model_file)
with open('./Models/dt.pkl', 'rb') as dt_model_file:
    dt_model = pickle.load(dt_model_file)
with open('./Models/xgb.pkl', 'rb') as xgb_model_file:
    xgb_model = pickle.load(xgb_model_file)
# =========================================

# Hàm này dùng để dự đoán
def predict_high_risk_stroke(model, features):
    prediction = model.predict(features)
    return prediction


def page_nav():
    prediction = None

# * **Age**: 13-level age category arranged in 5 years steps: 1 = 18-24; 2 = 25-29; ...; 9 = 60-64; ...; 13 = 80 or older.
# * **HighChol**: 0 = no high cholesterol; 1 = high cholesterol.
# * **BMI**: Body Mass Index.
# * **HeartDiseaseorAttack**: coronary heart disease (CHD) or myocardial infarction (MI) 0 = no; 1 = yes.
# * **PhysActivity**: physical activity in past 30 days - not including job 0 = no; 1 = yes.
# * **GenHlth**: Would you say that in general your health is: scale 1-5 1 = excellent; 2 = very good; 3 = good; 4 = fair; 5 = poor.
# * **PhysHlth**: physical illness or injury days in past 30 days scale 1-30.
# * **DiffWalk**: Do you have serious difficulty walking or climbing stairs? 0 = no; 1 = yes.
# * **Stroke**: you ever had a stroke 0 = no; 1 = yes.
# * **HighBP**: 0 = no high; BP 1 = high BP.
# * **Diabetes**: 0 = no diabetes; 1 = diabetes.

    # Load giá trị vào các từ điển ánh xạ
    age_mapping = {'18 - 24': 1, '25 - 29': 2, '30 - 34': 3, '35 - 39': 4, '40 - 44': 5, '45 - 49': 6, '50 - 54': 7, '55 - 59': 8, '60 - 64': 9, '65 - 69': 10, '70 - 74': 11, '75 - 79': 12, '80 or older': 13}
    highChol_mapping = {'No': 0, 'Yes': 1}
    #BMI
    heartDiseaseorAttack_mapping = {'No': 0, 'Yes': 1}
    physActivity_mapping = {'No': 0, 'Yes': 1}
    genHlth_mapping = {'Excellent': 1, 'Very Good': 2, 'Good': 3, 'Fair': 4, 'Poor': 5}
    #PhysHlth
    diffWalk_mapping = {'No': 0, 'Yes': 1}
    stroke_mapping = {'No': 0, 'Yes': 1}
    highBP_mapping = {'No': 0, 'Yes': 1} 



    # Header
    st.header(':kiwifruit: PREDICTING HIGH RISK OF DIABETES')
    st.markdown("<hr>", unsafe_allow_html=True)

    age = st.selectbox('What is your age group?', age_mapping.keys())

    # Medical checkout
    st.markdown("<hr>", unsafe_allow_html=True)

    # Load giá trị vào các selectbox từ các từ điển ánh xạ
    # HighChol
    highChol = st.selectbox('Do you have high cholesterol?', highChol_mapping.keys())
    # BMI
    BMI = st.number_input('What is your BMI?', min_value=0, max_value=100, value=0)
    # HeartDiseaseorAttack
    heartDiseaseorAttack = st.selectbox('Do you have coronary heart disease or myocardial infarction?', heartDiseaseorAttack_mapping.keys())
    # PhysActivity
    physActivity = st.selectbox('Do you have physical activity in past 30 days?', physActivity_mapping.keys())
    # GenHlth
    genHlth = st.selectbox('Would you say that in general your health is:', genHlth_mapping.keys())
    # PhysHlth
    PhysHlth = st.number_input('How many physical illness or injury days in past 30 days?', min_value=0, max_value=30, value=0)
    # DiffWalk
    diffWalk = st.selectbox('Do you have serious difficulty walking or climbing stairs?', diffWalk_mapping.keys())
    # Stroke
    stroke = st.selectbox('Have you ever had a stroke?', stroke_mapping.keys())
    # HighBP
    highBP = st.selectbox('Do you have high BP?', highBP_mapping.keys())
    

    # Đọc giá trị số tương ứng từ các từ điển ánh xạ
    age_numeric = age_mapping[age]
    highChol_numeric = highChol_mapping[highChol]
    BMI_numeric = BMI
    heartDiseaseorAttack_numeric = heartDiseaseorAttack_mapping[heartDiseaseorAttack]
    physActivity_numeric = physActivity_mapping[physActivity]
    genHlth_numeric = genHlth_mapping[genHlth]
    PhysHlth_numeric = PhysHlth
    diffWalk_numeric = diffWalk_mapping[diffWalk]
    stroke_numeric = stroke_mapping[stroke]
    highBP_numeric = highBP_mapping[highBP]

    features = np.array([
        age_numeric, highChol_numeric, BMI_numeric, heartDiseaseorAttack_numeric, physActivity_numeric, genHlth_numeric, PhysHlth_numeric, diffWalk_numeric, stroke_numeric, highBP_numeric
    ])

    # st.write("Features trước khi được chuẩn hóa:", features)
    

    # Chuẩn hóa dữ liệu
    scaler_features = pd.DataFrame([[BMI_numeric, age_numeric, PhysHlth_numeric, genHlth_numeric]], 
                                   columns=['BMI', 'Age', 'PhysHlth', 'GenHlth'])
    scaled_features = model_scaler.transform(scaler_features)
    BMI_numeric = scaled_features[0][0]
    age_numeric = scaled_features[0][1]
    PhysHlth_numeric = scaled_features[0][2]
    genHlth_numeric = scaled_features[0][3]


    # Sắp xếp các giá trị theo thứ tự yêu cầu
    features = np.array([
        age_numeric, highChol_numeric, BMI_numeric, heartDiseaseorAttack_numeric, physActivity_numeric, genHlth_numeric, PhysHlth_numeric, diffWalk_numeric, stroke_numeric, highBP_numeric
    ])

    features = features.reshape(1, -1)


    # In ra dữ liệu sau khi chuẩn hóa
    # st.write("Features sau khi được chuẩn hóa:", features)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Model Selection
    model = st.selectbox('Pick a model?', 
                         ('Decision Tree', 'Random Forest', 'Support Vector Machine (rbf kernel)', 'K-Nearest Neighbor', 'XGBoost'))

    # Predict Button
    btn = st.button("Predict")

    if btn:
        if model == 'Decision Tree':
            prediction = predict_high_risk_stroke(dt_model, features)
        elif model == 'Random Forest':
            prediction = predict_high_risk_stroke(rf_model, features)
        elif model == 'Support Vector Machine (rbf kernel)':
            prediction = predict_high_risk_stroke(svm_model, features)
        elif model == 'K-Nearest Neighbor':
            prediction = predict_high_risk_stroke(knn_model, features)
        elif model == 'XGBoost':
            prediction = predict_high_risk_stroke(xgb_model, features)

    if prediction is not None:
        if prediction[0] == 1:
            st.markdown("# :red[High risk of diabetes!!]")
        else:
            st.markdown("# :green[Not at high risk of diabetes~]")

page_nav()