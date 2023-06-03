# DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023
DETECTION of DOS ATTACKS FOR IOT NETWORK BASED ON ANOMALY DETECTION IDS TECHNIQUE AND MACHINE LEARNING ALGORITHMS

1- For writing our software code, we used the Jupiter Netbook, which features a flexible user interface for configuring and arranging workflows in fields like data science, machine learning, and statistical computing. Hence, we used the Jupiter Netbook to develop ML code. The IDE you can use for this is PyCharm or Visual Code. If you choose to utilize the PyCharm IDE, you need to download the professional version since it has the Jupiter network. Also, we downloaded Python version 3.9.13 to write our software code.

2- In order to begin writing our software, we first installed all the necessary packages such as Pandas, NumPy, time, Seaborn, and so on. In order to do that, we used the command pip install [package name]

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/30297597-4014-4ffc-917a-88aa9e19eee8)

Next, we downloaded the IoTID20 dataset from its website and saved it on the desktop.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/3787fcc6-3791-4c4c-b13f-ca546057975d)

3- In our code, we loaded the dataset and began preprocessing it. Preprocessing of data includes encoding, cleaning, and removing features. You can find the source code of Encoding and  the clean dataset function in the folowing figures.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/f08201b9-88fa-4a6a-b504-aa284a863831)

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/c05ae2de-eda7-45bc-88e3-09d7adb30163)

4- Following that, for the selection algorithms to select important features from the dataset, we started with GA. We wrote the GA code by importing genetic selection package. A source code for the GA feature selection algorithm is shown in Figure. Nevertheless, we encountered a problem when we ran this algorithm, which is the change of features every time it runs. After searching for four days, we finally found ”np.random. seed(42)”. This function allows the algorithm to give us the same features each time we run it.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/d18c40ed-f25b-4f18-9f88-bee6066d57c5)
5-For the CFS algorithm, we imported the CFS method from the skfeature.function. statistical based library. The disadvantage of this algorithm is that it takes a long time to select the features, around 12 hours. Furthermore, this algorithm does not select a specific number of features; instead it arranges them from most important to least important. For that reason, we limit the number of features of the CFS algorithm to the 13 most important, since GA selected 13 from the dataset, making a fair comparison. Figure presents the source code for the CFS algorithm.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/70d3742f-006f-4524-aed2-83c89d8f93dd)

6- The next step was to split our dataset into training and testing sets using the train test split method. In our ML software, we set apart 33% for testing and 67% for training. You can choose your own ratio, however.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/5d64eea2-3dc0-46b4-8418-f26f242df416)

7- The classification algorithms used were DT, RF, SVM, and KNN to make comparisons between them. The first step was to train them using all dataset features, then we trained them using only GA-selected features, and finally we trained them using features selected by the CFS algorithm. In order to implement these algorithms, we installed and used the Skitlearn library. 

8- We then compared these classification algorithms using a confusion matrix to calculate the four evaluation metrics: accuracy, precision, recall, and F1-score. This can be accomplished by importing confusion matrix , confusion matrixdisplay, accuracy score, recision score, recall score , and f1 score from sklearn.metrics. Figure illustrates the source code of the performance evaluation.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/249734b5-6e69-428a-bc6c-05cd318a1cac)

9- Once we compared the 12 models and chose the one we wanted to use in the IDS, we saved it using the pickle library in Python. Therefore, we imported the pickle
library, then opened a file, created an object, and dumped it into it. For serializing operations, it is necessary to specify the text modes as write (w) and binary (b). Figure shows the source code for saving the machine learning code.
![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/dcfba03f-95c9-4633-946c-5df3e73a93d4)

10- We next loaded the saved model and wrote a script that took feature values as inputs, preprocessed them and converted them to float types. We then entered them into the model to detect and predict whether it contained a DoS attack. The source code for this part can be seen in following figure.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/b34f3d5b-7fec-4965-acc9-9f24f4d204e7)

# Raspberry Pi Setup
For that, we used the following tools:

1. Raspberry Pi 3 model B+.
2. MicroSD card with 64 GB to store all Raspberry Pi files and the operating
system.
3. MicroSD card adapter.
4. HDMI to connect the Raspberry Pi to the monitor.
5. Power supply.
6. Keyboard and a mouse to control the Raspberry Pi.
7. Monitor to view the Raspberry Pi OS desktop environment.
8. SD card reader to connect the microSD card to the PC.

Therefore, we connected the microSD card to the PC using the SD card reader after entering it into the adapter, and then we installed the Raspbian operating system. The Raspberry Pi Imager is the easiest way to install Raspberry Pi OS on an SD card.

1- So first, we downloaded and launched the Raspberry Pi Imager from the Raspberry Pi websiteand clicked on the link for the Raspberry Pi Imager that matches the PC operating system, as shown in figure.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/12f1f9b6-a26a-4e42-99e5-0ac8540987c9)

2- As soon as the download was complete, we clicked it to launch the installer.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/5cc2678e-9089-45d0-9395-a69db173db35)

3- With the Raspberry Pi Imager, we selected the Raspberry Pi operating system (32 bits) and our SD card as the storage area for the installation, then we click on write, as shown in figure.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/c30ea65e-8225-4c75-9fb4-67f697221fa0)

4- After the Raspberry Pi Imager finished writing and got the following message in Figure, we ejected the SD card.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/91e851d2-71d7-4e77-b464-f75cba8d5d5b)

5- Then, we inserted the SD card that we would to set up with Raspberry Pi OS into the microSD card slot on the underside of the Raspberry Pi as shown in Figure 


![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/927a5cae-1348-4b42-8328-a142c173e8b5)

6- Here, we connected the Raspberry Pi to power, a USB mouse, a USB keyboard, and HDMI, and connected that to a TV screen or monitor. Figure shows how the connection is done.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/a4dbcb31-a760-402e-8062-2be09e4309c9)

7- Finally, the Raspberry Pi OS desktop appeared on the screen, as shown in figure.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/a8c061a0-81ef-4e42-af6e-1291348868ac)

# Uploading the System on the Raspberry Pi

1- For uploading and transferring the software, we used a USB driver.
2- Then, we installed all the required packages to run the software using Raspberry Pi’s command terminal, including Django, NumPy, scipy, and Skit-learn. During this process, we encountered many problems due to the size of the packages and the time it took to download them. The NumPy package also needs to be compatible with scipy, so we tried installing several versions of them until they worked. As shown in Figure, we reinstalled compatible versions of Nampy, scipy, and skit-learn.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/6d4367eb-3278-4de7-a084-0318b58f4856)

3- We ran the software from the command terminal after uploading it to the Raspberry Pi desktop. After entering the software folder with the cd command, we run the local web server with the ”python manage.py runserver” command. The commands to run the software is shown in figure.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/e22a9c81-f38e-4dea-9d20-a094f1ee7920)

4- After that, to run the system, we copied the web server link and pasted it into the browser.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/86c3e9df-2ce3-4512-9e83-77d8b008ef13)

5- Now, we have the web page where we can start a new test, as shown in Figure.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/90255f5e-cf76-4a12-81db-c4867f54ce97)

6- Then, we entered the packet features values as input and pressed detect, which sent the values to the model for prediction.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/042c7eeb-559d-48ef-b328-4763f621eb3d)

7- The system will show the result of the prediction on the main page of the website "The traffic is DoS attack, take action!" or "The traffic is Normal," as shown in figures.

![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/54ea2f42-4438-4942-bc9c-fa20d49adb04)


![image](https://github.com/Esra12989/DETECTION_of_DOS-ATTACKS_FOR_IOT_NETWORK_2023/assets/47214851/a1ddf79a-1a88-49ff-8285-da002dacc8b4)




