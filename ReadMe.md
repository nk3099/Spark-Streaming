# Installation/Setup Process:
## 1.using Docker <br>
## 2.using Local <br>


# Using Docker
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


************************************************************************************************************************************************************
# Using Local

### Step 1: Check Installed Java Versions 
Run this command:

```
/usr/libexec/java_home -V
```
This will list all installed JDK versions. <br>
✅ If JDK 11 appears in the list, note its exact path. <br>
❌ If JDK 11 is NOT listed, we need to install it (go to Step 2).

### Step 2: Install JDK 11 (If Missing) <br>
If JDK 11 is not installed, install it using Homebrew:

```
brew install openjdk@11
```
After installation, check the installed path:

```
ls -l /opt/homebrew/opt/openjdk@11
```
You should see something like:

```
/opt/homebrew/opt/openjdk@11 -> ../Cellar/openjdk@11/11.0.x
```

### Step 3: Set JDK 11 as Default <br>
Now, set JAVA_HOME to point to JDK 11:

```
export JAVA_HOME=/opt/homebrew/opt/openjdk@11
export PATH="$JAVA_HOME/bin:$PATH"
```
Check if it's working:
```
echo $JAVA_HOME
java -version
```
You should see Java 11.

### Step 4: Make the Change Permanent
To make sure JDK 11 is set every time you open the terminal, add these lines to your shell config file:

✅ For macOS Catalina & Later (Zsh)
```
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@11' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
✅ For Older macOS Versions (Bash)
```
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@11' >> ~/.bash_profile
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

### Step 5: Verify Again
Now, check if Java is set correctly:
```
echo $JAVA_HOME
java -version
```




  
