"""
main.py
--------
This file runs your target Python code (mainfile.py). 
If there is any error, it automatically restores mainfile.py 
from a safe backup copy (mainfile.txt).
"""

import time

try:
    # Try running the main code file
    import mainfile  

except Exception as e:
    print("----- Error in the code -----")
    print("Error details:", e)
    time.sleep(1.5)

    print("\n----- Recovering the code -----")
    
    # Read backup code from mainfile.txt
    with open("mainfile.txt", "r") as backup:
        code = backup.read()
    
    # Overwrite mainfile.py with the backup code
    with open("mainfile.py", "w") as target:
        target.write(code)
    
    time.sleep(1.5)
    print("File recovered successfully! Now running recovered file...\n")
    time.sleep(1.5)

    # Import the recovered file
    import mainfile
