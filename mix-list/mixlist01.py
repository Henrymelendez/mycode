#!/usr/bin/env python3
my_list = ["192.168.0.5",5060,"UP"];

print("The first item in the list (IP): " + my_list[0]);
print("The second item in the (port): " + str(my_list[1]));
print("The last item in the list (state): " + my_list[2] )

iplist = [5060,"80",55,"10.0.0.1","10.20.30.1","ssh"];

print("IP addresses: " + iplist[3] + ", and " + iplist[4]);

print("IP addresses: " + iplist[3] + ", and", iplist[4]);

print(f"IP addresses: {iplist[3]}, and {iplist[4]}");


wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4);

num = input("a number between 0 and 20 ");

num = int(num);

print(tlgstudents[num] + " always uses " + str(num) + wordbank[1] + " to indent.");
