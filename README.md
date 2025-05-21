# ML-Polar


(bvenv) PS D:\ML-Drug> pip install pandas

 PS D:\ML-Drug\bvenv> pip install scikit-learn  
 (bvenv) PS D:\ML-Drug\bvenv> python drug_classification_model.py created pickle file  ![image](https://github.com/user-attachments/assets/cc0f3487-3d25-4fb5-bbaf-9a68ba59d273)

 (bvenv) PS D:\ML-Drug\bvenv> pip install polar

 (bvenv) PS D:\ML-Drug\bvenv> pip install pydantic
 pip install polar pandas scikit-learn numpy
 (bvenv) PS D:\ML-Drug\bvenv> uvicorn main:app --reload --port 5000
 ![image](https://github.com/user-attachments/assets/650c1de6-de72-4c48-989f-c88daa6b730e)

 FAST API is running and url is  http://127.0.0.1:5000

 I am calling api in postman with data 

![image](https://github.com/user-attachments/assets/a46571df-f4c2-49c6-a669-2d60eebc8152)

![image](https://github.com/user-attachments/assets/5358aa93-caf2-48af-bde9-08a1a03c39c7)

Now I am going to deploy this ML model in Kubernetes (MiniKube)


1 C:\Users\bijus>minikube start
2 C:\Users\bijus>minikube dashboard
![image](https://github.com/user-attachments/assets/6d68458d-9152-4ae6-ad49-993b164a21d5)

3. Created Dockerfile and requirements.txt![image](https://github.com/user-attachments/assets/da90c318-8dcd-42f8-b3e8-908fdce2c11c) ![image](https://github.com/user-attachments/assets/5099cdfd-2fe3-40f1-8ee5-080af429d8cc)

