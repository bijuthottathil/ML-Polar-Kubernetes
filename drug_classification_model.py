# drug_classification_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Sample data
data = pd.DataFrame({
    'Age': [25, 35, 45, 20, 60],
    'Sex': [1, 0, 1, 0, 1],  # 1=Male, 0=Female
    'BP': [1, 2, 0, 1, 2],   # 0=Low, 1=Normal, 2=High
    'Cholesterol': [1, 0, 2, 1, 2],  # 0=Normal, 1=High, 2=Very High
    'Na_to_K': [15.0, 13.2, 14.5, 17.1, 12.3],
    'Drug': ['DrugY', 'DrugC', 'DrugX', 'DrugY', 'DrugC']
})

X = data.drop('Drug', axis=1)
y = data['Drug']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
