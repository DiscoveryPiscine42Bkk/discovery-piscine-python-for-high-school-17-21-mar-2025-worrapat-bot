#!/usr/bin/env python3
import sys
import re

if len(sys.argv)>3:
    
    if sys.argv[1]:
        
        matches = re.findall(sys.argv[1], sys.argv[2])
    
        num_parameters = len(matches)

        print(f"{num_parameters}")
    
    else:
        print("0")
else:
    print("none")
  

