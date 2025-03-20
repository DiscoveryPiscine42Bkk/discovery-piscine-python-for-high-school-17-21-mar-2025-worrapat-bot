#!/usr/bin/env python3

import sys

if len(sys.argv)>1:
    
    #correct all now
    num = len(sys.argv)-1
    print(f"parameters: {num}")
    
    
    Text = sys.argv[1:]
    
    for i in  Text:
        numText = (len(i))
        print(i, numText)

else:
    print("none")