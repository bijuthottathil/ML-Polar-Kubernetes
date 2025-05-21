#  Drug Classification ML model, containerize it with Polar (a FastAPI-based Python framework), deploy it to Kubernetes

![image](https://github.com/user-attachments/assets/8248448a-c481-41e2-a508-5a6d3c04c21f)



Follow these steps to setup environment. I used virtual environment in windows to run end to end
1.  PS D:\ML-Drug\bvenv> python3 -m venv bvenv
2.  PS D:\ML-Drug\bvenv> .\bvenv\Scripts\Activate.ps1
3.  cd benv
4.  Make sure that Docker for windows/mac is running ![image](https://github.com/user-attachments/assets/383f64b4-5fa7-46a6-8716-52cd07d3056d)

5.  Then you can proceed with below steps


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

4. Please create K8s folder and put deployment.yaml. created deployment.yaml under k8s folder![image](https://github.com/user-attachments/assets/954ff8ab-523f-4dd7-83e0-ebbd3fd6a1ec)

5. Docker build  using  (bvenv) PS D:\ML-Drug\bvenv> docker build -t bijuthottathil/drug-api:latest .  ![image](https://github.com/user-attachments/assets/942e4592-5f83-4724-b666-708f28bb0640)
6. Push docker image to docker hub  using docker push bijuthottathil/drug-api:latest    ![image](https://github.com/user-attachments/assets/c418050a-7a63-41b9-9594-68e6095bde82)
7. Image is successfully pushed to docker hub ![image](https://github.com/user-attachments/assets/1e804bec-4c3a-4115-9874-d5ce40306647)
8. Next deploying services to Kubernetes
9. (bvenv) PS D:\ML-Drug\bvenv> kubectl apply -f k8s/deployment.yaml
deployment.apps/drug-model-api created
service/drug-api-service created
(bvenv) PS D:\ML-Drug\bvenv> ![image](https://github.com/user-attachments/assets/a9f2dca5-0915-44a0-b342-e5adc35312d4)
10. pod is running  ![image](https://github.com/user-attachments/assets/54d27aca-53b7-4d62-815d-ff8ee6ed3167)
11. ![image](https://github.com/user-attachments/assets/4df738b5-800c-4e46-bc3b-14eaf3e7e537)
12. Next step is to get kubernetes url for the service . For that execute  minikube service drug-api-service --url ![image](https://github.com/user-attachments/assets/87898eb3-7396-4b65-baea-e38874c646e9)
13. To test whether service is running or not, I am using postman to post data to service
14. Functionality is working fine. 
15. ![image](https://github.com/user-attachments/assets/0d37546c-6b8e-4a4f-9c9b-337081f5f18a)
16. Now I changed data and posted to service in Kubernetes ![image](https://github.com/user-attachments/assets/d632cc14-e693-4706-9fc6-2017c3555446)
17. I checked Pods log . looking good ![image](https://github.com/user-attachments/assets/3f65deb6-489b-4d9c-852e-d38da009bebc)
18. In Kubernetes dashboard you can see green for the service we deployed  ![image](https://github.com/user-attachments/assets/56476911-c5f8-4d12-9720-28f56fd05bcd)

    







