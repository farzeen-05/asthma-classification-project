from flask import Flask,render_template,request,redirect,url_for,flash,session
import mysql.connector
from werkzeug.security import generate_password_hash,check_password_hash
import re
import joblib
import numpy as np
import pandas as pd

#save LR model
model=joblib.load('rf_os_model.pkl')

#save scaler
scaler=joblib.load('scaler_ml.pkl')

app = Flask(__name__)
app.secret_key = '9945'

#Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="astma_db",
        port=3306
    )

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/starter_page')
def starter_page():
    return render_template('starter_page.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user_id' not in session:
        flash("Please login to access the prediction system", "warning")
        return redirect(url_for('register'))

    prediction = None 

    if request.method == 'POST':
        try:
            name = request.form['name']
            age = float(request.form['age'])
            bmi = float(request.form['bmi'])
            smoking = int(request.form['smoking'])
            allergy = int(request.form['allergy'])
            breathing = int(request.form['breathing'])

            # ✅ Create full 28 feature input
            data = [0]*28

            data[0] = age
            data[2] = bmi
            data[9] = smoking
            data[15] = allergy
            data[18] = breathing

            df = pd.DataFrame([data], columns=[
                'Age','Gender','BMI','Medication_Adherence','Number_of_ER_Visits',
                'Peak_Expiratory_Flow','FeNO_Level','Occupation_Type_Indoor',
                'Occupation_Type_Outdoor','Smoking_Status_Current',
                'Smoking_Status_Former','Smoking_Status_Never',
                'Physical_Activity_Level_Active','Physical_Activity_Level_Moderate',
                'Physical_Activity_Level_Sedentary','Allergies_Dust',
                'Allergies_Multiple','Allergies_Pets','Allergies_Pollen',
                'Air_Pollution_Level_High','Air_Pollution_Level_Low',
                'Air_Pollution_Level_Moderate','Comorbidities_Both',
                'Comorbidities_Diabetes','Comorbidities_Hypertension',
                'Asthma_Control_Level_Not Controlled',
                'Asthma_Control_Level_Poorly Controlled',
                'Asthma_Control_Level_Well Controlled'
            ])

            # ✅ Scale input
            scaled = scaler.transform(df)

            # ✅ Predict
            prediction = model.predict(scaled)

            if prediction[0] == 1:
                result = "High Risk of Asthma"
            else:
                result = "Low Risk of Asthma"

            return render_template('predict.html', prediction=result, name=name)

        except Exception as e:
            return f"Error: {e}"

    return render_template('predict.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email format", "danger")
            return redirect(url_for('register'))

        if len(password) < 6:
            flash("Password must be at least 6 characters", "danger")
            return redirect(url_for('register'))    

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email =%s" ,(email,))
        user=cursor.fetchone()
        cursor.close()
        cursor.close()

        if user and check_password_hash (user['password'],password):
            session['user_id']=user['u_id']
            session['username']=user['u_name']
            return redirect(url_for('index'))    
        else:
            flash("Invalid email or password ","danger")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        u_name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # validation INSIDE POST
        if not u_name.strip():
            flash("Username is required", "danger")
            return redirect(url_for('register'))

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email format", "danger")
            return redirect(url_for('register'))

        if len(password) < 6:
            flash("Password must be at least 6 characters", "danger")
            return redirect(url_for('register'))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT u_id FROM users WHERE email=%s", (email,))
        if cursor.fetchone():
            flash("Email already registered", "danger")
            cursor.close()
            conn.close()
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        cursor.execute(
            "INSERT INTO users (u_name, email, password) VALUES (%s, %s, %s)",
            (u_name, email, hashed_password)
        )
        conn.commit()

        cursor.close()
        conn.close()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for('login'))

    #  GET request safe
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)

