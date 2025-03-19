#!/usr/bin/env python3

import sys

if len(sys.argv)>0:
    num = len(sys.argv)-1
    print(f"parameters: {num}")
    
    Text = sys.argv[1:]
    print(Text)
    for i in  Text:
        print()

else:
    print("none")