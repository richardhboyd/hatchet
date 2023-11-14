import re

def compareVersion(version1, version2):
    v1_parts = [int(x) for x in re.split('\.', version1)]
    v2_parts = [int(x) for x in re.split('\.', version2)]
    
    for i in range(max(len(v1_parts), len(v2_parts))):
        v1_part = v1_parts[i] if i < len(v1_parts) else 0
        v2_part = v2_parts[i] if i < len(v2_parts) else 0
        
        if v1_part > v2_part:
            return 1
        elif v1_part < v2_part:
            return -1
        
    return 0
