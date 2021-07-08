import pandas as pd
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('20210103_hundenamen.csv')

# Set Lookup column
names = set(df['HUNDENAME'])
target = 'Luca'

def get_leven_distance(s, t):
    # Same words have distace 0.
    if s == t:
        return False
    
    # Lenght of the words
    m = len(s)
    n = len(t)
    
    # Words with higher lenght difference than 1 will have distance >1.
    if abs(m - n) > 1:
        return False
    
    # Boolean that will become True when one edition is already needed.
    edited = False
    
    i = 0
    j = 0
    while i < m and j < n:
        # If the characters are not the same one edition will be needed.
        if s[i] != t[j]:
            if edited:
                return False
            
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:
                i+=1
                j+=1
                
            edited = True
            
        else:
            i+=1
            j+=1
    
    # If one of the words still has one more character to check.
    if (i < m or j < n) and edited:
        return False
    
    return True

resulting_names = []
for n in names:
    if get_leven_distance(n,target):
        resulting_names.append(n)

print(resulting_names)