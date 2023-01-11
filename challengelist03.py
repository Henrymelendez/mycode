#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


a = challenge[2][0];
b = challenge[2][1];
c = challenge[3];

print(f"my {b}! The {a} do {c}");

a1 = trial[2]["eyes"];
b1 = trial[2]["goggles"];
c1 = trial[3];

print(f"My {b1}! The {a1} do {c1}");

a2 = nightmare[0]["user"]["name"]["first"];
b2 = nightmare[0]["kumquat"];
c2 = nightmare[0]["d"];


print(f"My {a2}! The {b2} do {c2}");

