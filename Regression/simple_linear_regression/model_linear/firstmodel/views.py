from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pandas as pd

def salary_ten(request):
    return render(request, 'salary.html')

def predict_chances(request):
    # Receive data from client
    experience = (request.GET['experience'])
    
    model = pd.read_pickle('regresor.pickle')
    chances = model.predict([[experience]])
    return HttpResponse({"Salary": chances[0]})