#!/usr/bin/env python3


def main():

    bottles = int(input("How Many bottle? "))
    
    if bottles > 100:
        bottles = 100;


    for x in range(bottles, 0, -1):

        print(f"{x} bottles of beer on the wall!"); 
        print(f"{x} bottles of beer on the wall! {x} bottles of beer! you  You take one down, pass it around!") 
        if x == 1:
            print("no more bottles!")



if __name__ == '__main__':
    main()


