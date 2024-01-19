import requests
import getpass
import sys

if sys.version_info[0] < 3:
    print("Error: Python3 is needed!")
    sys.exit(1)

url = "http://10.250.3.66/"
action = "logout"
username = input("Please input your uis username: ")
password = ""
option = input("Are you tring to login[y/n] (y as default): ")

if len(option) == 0 or option.upper()[0] == "Y":
    password = getpass.getpass("Please input your password:")
    action = "login"
    
data = {
    "action": action,
    "username": username,
    "password": password,
    "ac_id": "1",
    "save_me": "0",
    "ajax": "1",
}

r = requests.post(url + "include/auth_action.php", data)

if "login_ok" in r.content.decode("utf-8"):
    print("网络已连接")
else:
    print(r.content.decode("utf-8"))
