#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

names = dir(hidden_4)
for k in names:
    if k[:2] != "__":
        print(k)
