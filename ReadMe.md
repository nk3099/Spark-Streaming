# Installation/Setup Process:

## 1. Clone github repo from terminal:
![image](https://github.com/user-attachments/assets/5327789f-f0bf-4193-a09b-985f8502f9cc)
![image](https://github.com/user-attachments/assets/70e3b59f-a72f-489a-8683-1a648a32f467)
![image](https://github.com/user-attachments/assets/70956a02-14a7-41cb-96c5-7c95d084ea59)


## 2.Go to [localhost:8888](http://localhost:8888/) on browser:

-> Copy token from "ed-pyspark-jupyter-lab" docker image to localhost:8888
![image](https://github.com/user-attachments/assets/69566675-24ce-40c8-8664-76344e3bbdb6)

<br>
-> Create Spark Session in a progream:
![image](https://github.com/user-attachments/assets/f291aa5d-776e-4849-adcd-a8ab5371edcd)

## 3. Go to [localhost:4040](http://localhost:4040/) for Spark UI:
![image](https://github.com/user-attachments/assets/6c2f6ba7-ef48-4233-a763-f926f439de5b)

## 4. To validate KAFKA:
   -> Got to "ed-kafka" on docker -> exec (for terminal) <br>
   -> Command for changing to BASH: /bin/bash <br>
   -> Create & View a topic in Kafka <br>
   $ kafka-topics --list --bootstrap-server ed-kafka:9092 <br>
   $ kafka-topics --create --topic test-topic --bootstrap-server ed-kafka:9092 <br>
   ![image](https://github.com/user-attachments/assets/51980797-149f-4133-9ca6-1247f76bf02c)
