#!/bin/bash

url="http://10.250.3.66/"
action="logout"

read -p "Please input your uis username: " username
password=""
read -p "Are you trying to login[y/n] (y as default): " option

if [ -z "$option" ] || [ "${option^}" = "Y" ]; then
  read -s -p "Please input your password: " password
  action="login"
fi

data="action=$action&username=$username&password=$password&ac_id=1&save_me=0&ajax=1"

response=$(curl -s -X POST -d "$data" "$url/include/auth_action.php")

if [[ $response == *"login_ok"* ]]; then
  echo -e "\n网络已连接"
else
  echo -e "\n$response"
fi
