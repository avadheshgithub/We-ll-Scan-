from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from joblib import load
import numpy as np
from django.views.decorators.csrf import csrf_exempt
import requests
import os


heartmodel = load('./savedModels/heartmodelmain.joblib')
kidneymodel = load('./savedModels/kidneymodel1.joblib')
diebetesmodel = load('./savedModels/diebetesmodel.joblib')



# Create your views here.
def index(request):
    return render(request, 'index.html')

def consultation(request):
    return render(request, 'consultation.html')

def about(request):
    return render(request, 'about.html')

def diet(request):
    return render(request, 'diet_chart.html')

def team(request):
    return render(request,'team.html')

# def heart(request):
#     return render(request, 'heart.html')

def heart(request):
    return render(request, 'heart2.html')

# def kidney(request):
#     return render(request, 'kidney.html')

def kidney(request):
    return render(request, 'kidney2.html')

# def diebetes(request):
#     return render(request, 'diebetes.html')

def diebetes(request):
    return render(request, 'diebetes2.html')

def arthritis(request):
    return render(request, 'arthritis.html')

def consultation(request):
    return render(request, 'consultation.html')



def heartresult(request):
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    chest_pain = request.POST.get('cp')
    resting_blood_pressure = request.POST.get('trestbps')
    serum_cholestrol = request.POST.get('chol')
    fasting_blood_sugar = request.POST.get('fbs')
    resting_ecg = request.POST.get('restecg')
    max_heart_rate = request.POST.get('thalach')
    exercise_induced_angina = request.POST.get('exang')
    ST_Depression = request.POST.get('oldpeak')
    slope_peak_exercise = request.POST.get('slope')
    major_vessels_count = request.POST.get('ca')
    Thalassemia = request.POST.get('thal')

    # Making prediction using the model
    y_pred_rf = heartmodel.predict([[age, sex, chest_pain, resting_blood_pressure, serum_cholestrol, fasting_blood_sugar,
                                     resting_ecg, max_heart_rate, exercise_induced_angina, ST_Depression,
                                     slope_peak_exercise, major_vessels_count, Thalassemia]])

    # Prediction output
    if y_pred_rf[0] == 0:
        prediction_result = 'negative'
    else:
        prediction_result = 'positive'

    # Pass result to the template
    return render(request, 'heartresult.html', {'prediction_result': prediction_result})





def kidneyresult(request):
    age = request.POST.get('age')
    blood_pressure = request.POST.get('blood-pressure')
    specific_gravity = float(request.POST.get('specific-gravity'))
    albumin = request.POST.get('albumin')
    sugar = request.POST.get('sugar')
    blood_glucose = request.POST.get('blood-glucose')
    blood_urea = request.POST.get('blood-urea')
    serum_creatinine = request.POST.get('serum-creatinine')
    sodium = request.POST.get('sodium')
    potassium = request.POST.get('potassium')
    hemoglobin = request.POST.get('hemoglobin')
    packed_cell_volume = request.POST.get('packed-cell-volume')
    white_blood_cells =request.POST.get('white-blood-cells')
    red_blood_cells = request.POST.get('red-blood-cells')
    red_blood_cells_type = request.POST.get('red-blood-cells-type')
    pus_cells = request.POST.get('pus-cells')
    pus_cell_clumps = request.POST.get('pus-cell-clumps')
    bacteria = request.POST.get('bacteria')
    hypertension = request.POST.get('hypertension')
    diabetes = request.POST.get('diabetes')
    coronary_artery_disease = request.POST.get('coronary-artery-disease')
    appetite = request.POST.get('appetite')
    pedal_edema = request.POST.get('pedal-edema')
    anemia = request.POST.get('anemia')

    y_pred = kidneymodel.predict([[age, blood_pressure, specific_gravity, albumin, sugar, blood_glucose, blood_urea,
                serum_creatinine, sodium, potassium, hemoglobin, packed_cell_volume, white_blood_cells, red_blood_cells,
                red_blood_cells_type, pus_cells, pus_cell_clumps, bacteria, hypertension, diabetes, coronary_artery_disease, appetite, pedal_edema,
                anemia]])

    # Prediction output
    if y_pred[0] == 0:
        prediction_result = 'negative'
    else:
        prediction_result = 'positive'

    # Pass result to the template
    return render(request, 'heartresult.html', {'prediction_result': prediction_result})


# def diebetesresult(request):
#     Gender = request.POST.get('Gender')
#     age = request.POST.get('Age')
#     Urea_Level = request.POST.get('Urea_Level')
#     Creatinine = request.POST.get('Cr')
#     Haemoglobin = request.POST.get('HbA1c')
#     Cholestrol = request.POST.get('Chol')
#     Triglycerides = request.POST.get('TG')
#     High_Density_Lipoprotein = request.POST.get('HDL')
#     Low_Density_Lipoprotein = request.POST.get('LDL')
#     Very_Low_Density_Lipoprotein = request.POST.get('VLDL')
#     Body_Mass_Index = request.POST.get('BMI')
    
#     y_pred_dieb = diebetesmodel.predict([[Gender,age,Urea_Level,Creatinine,Haemoglobin,Cholestrol,Triglycerides,High_Density_Lipoprotein,
#                                           Low_Density_Lipoprotein,Very_Low_Density_Lipoprotein,Body_Mass_Index]])
    
#     if y_pred_dieb[0] == 0:
#         y_pred_dieb = "No Need to worry you are living a healthy life. Prediction with accuracy score 98.94 %"
#     elif[1]:
#         y_pred_dieb = "Alert you are on risk of diabetes. Consult to Doctor."
#     return render(request,'diebetesresult.html',{'diebetesresult':y_pred_dieb})

	# Gender	Age	Urea_Level	Cr	HbA1c	Chol	TG	HDL	LDL	VLDL	BMI

@csrf_exempt
def diebetesresult(request):
    if request.method == 'POST':
        try:
            # Retrieve and validate input data
            Gender = request.POST.get('Gender').strip().lower()
            age = request.POST.get('Age')
            Urea_Level = request.POST.get('Urea_Level')
            Creatinine = request.POST.get('Cr')
            Haemoglobin = request.POST.get('HbA1c')
            Cholestrol = request.POST.get('Chol')
            Triglycerides = request.POST.get('TG')
            High_Density_Lipoprotein = request.POST.get('HDL')
            Low_Density_Lipoprotein = request.POST.get('LDL')
            Very_Low_Density_Lipoprotein = request.POST.get('VLDL')
            Body_Mass_Index = request.POST.get('BMI')

            # Convert Gender to numerical (0 for Male, 1 for Female, adjust if needed)
            gender_numeric = 0 if Gender in ['male', 'm'] else 1

            # Convert inputs to appropriate data types
            input_data = np.array([[
                gender_numeric, int(age), float(Urea_Level), float(Creatinine),
                float(Haemoglobin), float(Cholestrol), float(Triglycerides),
                float(High_Density_Lipoprotein), float(Low_Density_Lipoprotein),
                float(Very_Low_Density_Lipoprotein), float(Body_Mass_Index)
            ]])

            # Ensure model is loaded
            if diebetesmodel:
                y_pred_dieb = diebetesmodel.predict(input_data)
            else:
                raise ValueError("Model not loaded properly.")

            # Interpret prediction result
                # Prediction output
            if y_pred_dieb[0] == 0:
               prediction_result = 'negative'
            else:
             prediction_result = 'positive'

            # Pass result to the template
            return render(request, 'heartresult.html', {'prediction_result': prediction_result})

           

        except (ValueError, TypeError) as e:
            return render(request, 'diebetesresult.html', {'error': f"Invalid input data: {str(e)}"})

    else:
        return render(request, 'diebetes.html')







def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request,'contact.html')









    # - Register a user
def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return JsonResponse({"error": "Your password and confirm password are not the same!"}, status=400)
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return JsonResponse({"success": "User created successfully!"}, status=201)
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            auth_login(request, user)
            return JsonResponse({"success": "Login successful!"}, status=200)
        else:
            return JsonResponse({"error": "Username or Password is incorrect!"}, status=400)

    return render(request, 'login.html')

@csrf_exempt  # Allows logging out via POST request (optional but useful)
def LogoutPage(request):
    if request.method == "POST":  # Ensures logout happens only via POST
        logout(request)
    return redirect('/')




@csrf_exempt
def arthritisresult(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        file_path = os.path.join('uploads', file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Send the image to the Flask service for prediction
        try:
            with open(file_path, 'rb') as f:
                response = requests.post('http://127.0.0.1:5000', files={'file': f})
            result = response.json()
        except Exception as e:
            result = {'error': str(e)}
        finally:
            os.remove(file_path)  # Cleanup uploaded file

        return JsonResponse(result)
    return render(request, 'arthritis.html')


