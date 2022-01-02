import re

def count_smileys(arr):
    
    return len(re.findall(r"[:;][-~]?[)D]", "".join(arr)))
