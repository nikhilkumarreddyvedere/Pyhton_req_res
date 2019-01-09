
# coding: utf-8

# In[1]:

import numpy as np
from flask import Flask, request, jsonify
import pickle


# In[2]:

app = Flask(__name__)
model = pickle.load(open('E:/DS_ML/ML/week6/rfmodel.pkl','rb'))


# In[8]:

# app.route('/api',methods=['POST'])
# def predict():
#     data = request.get_json(force=True)
#     prediction = model.predict([[np.array(data['exp'])]])
#     output = prediction[0]
#     return jsonify(output)

# if __name__ == '__main__':
#     app.run(port=5000, debug=False)


# In[ ]:

app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)["Pregnancies","Glucose","BloodPressure","Insulin","BMI","DiabetesPedigreeFunction"]
    prediction = model.predict([data]).tolist()
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5001, debug=False)


# In[ ]:



