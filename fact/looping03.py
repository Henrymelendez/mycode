#!/usr/bin/env python3

import uuid


howmany = int(input("How Many UUIDs should be Generated? "))


print("Generating UUIDs...")


for rando in range(howmany):

    print(uuid.uuid4())
