from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User

from joblib import load

kidneymodel = load('./savedModels/kidneymodel1.joblib')
heartmodel = load('./savedModels/heartmodel.joblib')
diebetesmodel = load('./savedModels/diebetesmodel.joblib')

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def diet(request):
    return render(request, 'home/diet.html')

def heart(request):
    return render(request, 'home/heart.html')

def kidney(request):
    return render(request, 'home/kidney.html')

def diebetes(request):
    return render(request, 'home/diebetes.html')

def bmicalc(request):
    return render(request,'home/bmi.html')

def team(request):
    return render(request,'home/team.html')

def login(request):
    return render(request, 'home/login.html')

def main(request):
    return render(request, 'home/index.html')

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



    y_pred_rf = heartmodel.predict([[age,sex,chest_pain,resting_blood_pressure,serum_cholestrol,fasting_blood_sugar,
                                     resting_ecg,max_heart_rate,exercise_induced_angina,ST_Depression,
                                     slope_peak_exercise,major_vessels_count,Thalassemia]])
    if y_pred_rf[0] == 0:
        y_pred_rf = 'Congrats!!! 🥳 Your Heart is in Good Condition. Prediction with accuracy score 90.16 %'
    elif[1]:
        y_pred_rf = "Consult to doctor related to Heart. Prediction with accuracy score 90.16 %" 
    return render(request,'home/heartresult.html',{'heartresult':y_pred_rf})





def kidneyresult(request):
    age = request.POST.get('age')
    blood_pressure = request.POST.get('blood-pressure')
    specific_gravity = request.POST.get('specific-gravity')
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

    if y_pred[0] == 0:
        y_pred = "Congrats!!! 🥳 Your Kidneys are in Good Condition. Prediction with accuracy score 97.2 %"
    elif y_pred[0] == 1:
        y_pred = "Consult to doctor related to Kidneys. Prediction with accuracy score 97.2 %"
    return render(request, 'home/kidneyresult.html', {'kidneyresult':y_pred})


def diebetesresult(request):
    Gender = request.POST.get('Gender')
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
    
    y_pred_dieb = diebetesmodel.predict([[Gender,age,Urea_Level,Creatinine,Haemoglobin,Cholestrol,Triglycerides,High_Density_Lipoprotein,
                                          Low_Density_Lipoprotein,Very_Low_Density_Lipoprotein,Body_Mass_Index]])
    
    if y_pred_dieb[0] == 0:
        y_pred_dieb = "Congrats!!! 🥳 You Are not having Diebetes. Prediction with accuracy score 98.94 %"
    elif[1]:
        y_pred_dieb = "Consult to doctor related to Diebetes. Prediction with accuracy score 98.94 %"
    return render(request,'home/diebetesresult.html',{'diebetesresult':y_pred_dieb})










def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request,'home/contact.html')



