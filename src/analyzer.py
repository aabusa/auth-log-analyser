with open("data/sample_auth.log" , "r") as log_data :
    for line in log_data :
        if "Failed" in line :
            parts = line.split()
            ip_index = parts.index("from") + 1
            ip = parts[ip_index]
            print("Failed ip is ", ip)
            
            
            