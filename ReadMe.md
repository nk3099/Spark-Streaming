# Installation/Setup Process:
## 1.using Docker <br>
## 2.using Local <br>


## Using Docker
### 1. Clone Github: [Docker-image](https://github.com/subhamkharwal/docker-images?tab=readme-ov-file)  repo from terminal:
![image](https://github.com/user-attachments/assets/5327789f-f0bf-4193-a09b-985f8502f9cc)
![image](https://github.com/user-attachments/assets/70e3b59f-a72f-489a-8683-1a648a32f467)
![image](https://github.com/user-attachments/assets/70956a02-14a7-41cb-96c5-7c95d084ea59)


### 2.Go to [localhost:8888](http://localhost:8888/) on browser:

-> Copy token from "ed-pyspark-jupyter-lab" docker image to localhost:8888
![image](https://github.com/user-attachments/assets/69566675-24ce-40c8-8664-76344e3bbdb6)

<br>
-> Create Spark Session in a program:

![image](https://github.com/user-attachments/assets/4058eb47-0863-4860-9c8b-e6819afe91fc)

### 3. Go to [localhost:4040](http://localhost:4040/) for Spark UI:
![image](https://github.com/user-attachments/assets/6c2f6ba7-ef48-4233-a763-f926f439de5b)

### 4. To validate KAFKA:
   -> Got to "ed-kafka" on docker -> exec (for terminal) <br>
   -> Command for changing to BASH: /bin/bash <br>
   -> Create & View a topic in Kafka <br>
   $ kafka-topics --list --bootstrap-server ed-kafka:9092 <br>
   $ kafka-topics --create --topic test-topic --bootstrap-server ed-kafka:9092 <br>
   ![image](https://github.com/user-attachments/assets/51980797-149f-4133-9ca6-1247f76bf02c)

### 5. ncat utility 
-> To create an endpoint for Spark to read streaming data using ncat, you can use it to listen on a specific port and forward the incoming data to Spark's streaming application, effectively creating a socket-based streaming source. <br>
**Socket** (IP+Port): communication endpoint that allows applications to exchange data over a network<br>

  -> conect to container and update repositories for ubuntu using command on terminal: docker exec -it "ed-pyspark-jupyter-lab Container ID" /bin/bash <br>
  -> Install ncat: to open socket endpoint   <br>                                                                          
             root@c5f0427c16f2:/home/jupyter# sudo apt-get install ncat <br>
             root@c5f0427c16f2:/home/jupyter# ncat -v <br>
      OR <br>
             root@c5f0427c16f2:/home/jupyter# apt install netcat-traditional <br>
             root@c5f0427c16f2:/home/jupyter# netcat -h <br>
             ![image](https://github.com/user-attachments/assets/3afc61c0-8a29-4aec-b248-e083eee8d296)

 
 ### 6.Setting up Jupyter Notebook:
Saving content in 'example.txt' file for Batch Program
![image](https://github.com/user-attachments/assets/6f6a6bad-a369-4f27-8b59-580affdd0f25)


### 7. Running Streaming Program
![image](https://github.com/user-attachments/assets/2331cf0e-cdea-4d56-a570-7cc8d34e5906)


## Using Local




  
