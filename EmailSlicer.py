# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:54:30 2022

@author: Pierre-Henri Rossouw

"60 Apps in 60 Days Challenge - App #3: Email Slicer"

"""


email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)