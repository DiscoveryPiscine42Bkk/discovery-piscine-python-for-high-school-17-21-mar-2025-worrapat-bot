#!/usr/bin/env python3

import sys
if len(sys.argv)<3:
     print("none")
    
else:
     Text = sys.argv[1:]
     Text.reverse()

for str in Text:
        print(str)
 