# StreamlitChatAppDemo

Chat sample code between users using Streamlit.

This project will be the code to chat between users by Streamlit.
Since it is the minimum necessary content, please modify it as necessary and use it.

## Install

```bash
pip install streamlit==1.24.0
pip install streamlit-authenticator==0.2.2
pip install streamlit-autorefresh==1.0.1
pip install extra-streamlit-components==0.1.56
pip install watchdog==3.0.0
pip install numpy==1.25.0
pip install Pillow==9.5.0
```

## Setting

The setting value of this code can be changed from the following setting file.
* [src/const.py](src/const.py)

You can configure the following settings.
* Local DB file path where user information and chat logs are saved.
* The path where the user's icon image is saved.
* Contents related to the Admin user registered as the initial user.
* Contents of cookies.
* The upper limit of the number of chats displayed and the refresh interval of the chat screen.


## Run

```bash
streamlit run src/01_login.py
```

During execution, you can check the demo screen from the following page.  
http://localhost:8501/chat

## Demo Video

![Demo](result/result.gif)

## How to use

1. Register as a user from the "register user" page.  
    If the login is successful, the following message will be displayed.  
    ```User registered successfully. Please login to continue.```  
    User information is registered in the local DB.  
    Also, the user set in setting file is registered as an initial user.  
2. Log in as a registered user from the "login" page.  
    A message similar to the one below is displayed.  
    ```Welcome [USER1].```  
3. If necessary, register your own icon image from the "change icon" page.  
    Icon images are saved in the folder specified in setting file.  
4. Chat from the "chat" page.  