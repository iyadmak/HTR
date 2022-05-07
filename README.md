# Handwritten Text Recognition system

* **Graduation project for my Master's degree (In progress)**


* **Based on LSTM architecture.**
* **Implemented with TensorFlow (TF).**
* **Trained on the IAM off-line HTR dataset.**
* **The model takes images of single words as input & outputs the recognized text.**
----

## **How to use it**
Clone it 

```
https://github.com/Moha-boukhatem/HTR.git
```

Create & activate the ENV

```
python3 -m venv venv
. venv/bin/activate
```

Install requirements

```
pip3 install -r requirements.txt
```

## **Preprocess Step**
Run 

```
cd Preprocess
python3 Main.py
```
the Main file will
* Clean & Split data
* Generate New Data Files in New Folder named "Data"
* All actions will be demonstrated by some animations in the Terminal

![Terminal](Doc/Terminal.png)
