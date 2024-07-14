Data come from https://www.kaggle.com/datasets/prosperchuks/health-dataset?select=diabetes_data.csv

We'll work with diabetes_data.csv, which has 17 feature variables and 1 target variable and its classes are balanced.

* **Age**: 13-level age category arranged in 5 years steps: 1 = 18-24; 2 = 25-29; ...; 9 = 60-64; ...; 13 = 80 or older.
* **Sex**: patient's gender 1 = male; 0 = female.
* **HighChol**: 0 = no high cholesterol; 1 = high cholesterol.
* **CholCheck**: 0 = no cholesterol check in 5 years; 1 = yes cholesterol check in 5 years.
* **BMI**: Body Mass Index.
* **Smoker**: Have you smoked at least 100 cigarettes in your entire life? (Note: 5 packs = 100 cigarettes) 0 = no; 1 = yes.
* **HeartDiseaseorAttack**: coronary heart disease (CHD) or myocardial infarction (MI) 0 = no; 1 = yes.
* **PhysActivity**: physical activity in past 30 days - not including job 0 = no; 1 = yes.
* **Fruits**: Consume Fruit 1 or more times per day 0 = no; 1 = yes.
* **Veggies**: Consume Vegetables 1 or more times per day 0 = no; 1 = yes.
* **HvyAlcoholConsump**: (adult men >=14 drinks per week and adult women>=7 drinks per week) 0 = no; 1 = yes.
* **GenHlth**: Would you say that in general your health is: scale 1-5 1 = excellent; 2 = very good; 3 = good; 4 = fair; 5 = poor.
* **MentHlth**: days of poor mental health scale 1-30 days.
* **PhysHlth**: physical illness or injury days in past 30 days scale 1-30.
* **DiffWalk**: Do you have serious difficulty walking or climbing stairs? 0 = no; 1 = yes.
* **Stroke**: you ever had a stroke 0 = no; 1 = yes.
* **HighBP**: 0 = no high; BP 1 = high BP.
* **Diabetes**: 0 = no diabetes; 1 = diabetes.