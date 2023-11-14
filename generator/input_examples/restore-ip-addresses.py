def ip_addresses(s):
    results = []
    
    def backtrack(idx, curr_ip):
        if idx == len(s) and len(curr_ip) == 4:
            results.append('.'.join(curr_ip))
            return
        
        if len(curr_ip) == 4:
            return
        
        for i in range(1, 4):
            if idx + i > len(s):
                break
            
            part = s[idx:idx+i]
            if part[0] == '0' and len(part) > 1: 
                continue
            
            if 0 <= int(part) <= 255:
                backtrack(idx+i, curr_ip + [part])
        
    backtrack(0, [])
    return results

print(ip_addresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']

print(ip_addresses("0000"))  
# ['0.0.0.0']

print(ip_addresses("101023"))
# ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']
