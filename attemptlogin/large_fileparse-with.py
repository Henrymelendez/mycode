#!/usr/bin/env python3


loginfail = 0
successful = 0;


with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as file:

    for line in file:

        if "- - - - -] Authorization failed" in line:

            loginfail += 1;
        elif "-] Authorization failed" in line:  # can ONLY be true if the "if" was false
            successful += 1 # this is the total number of times we see this pattern


print("The number of failed log in attemps is", loginfail)
print("The number of sucessful log in attemps is", successful)



