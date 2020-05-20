import pandas as pd

# Unpickle model 
model = pd.read_pickle('regresor.pickle') 

# Take input from user
experience = int(input("How many year experience  : "))

# Predict chances 
result = model.predict([[experience]])  # input must be 2D array
print(f"Salary are : {float(result)}")