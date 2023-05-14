details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
num_older60 = 0
temp = []
for x in details:
    
    y = x[-4:-2]
    temp.append(y)
    
age_eval = [eval(i) for i in temp]

for z in age_eval:
    if z > 60:
        num_older60 = num_older60 + 1
        
print("There are " + str(num_older60) + " people who are over 60 years old.")

