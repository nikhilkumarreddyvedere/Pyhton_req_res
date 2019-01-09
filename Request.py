
# coding: utf-8

# In[31]:

import requests
import json
url = 'http://127.0.0.1:5001/predict'
header = {'Content-Type': 'application/json','Accept': 'application/json'}
d = {}
d["Pregnancies"] = 6
d["Glucose"] = 183
d["BloodPressure"] = 72
d["Insulin"] = 33
d["BMI"] = 0.62
d["DiabetesPedigreeFunction"] = 50

dr=json.dumps(d,ensure_ascii=False)

resp = requests.post(url,data = dr,headers= header)
print(resp)


# In[ ]:




# In[ ]:



