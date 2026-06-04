from collections import Counter
ip_counts = Counter()
with open("data/sample_auth.log" , "r") as log_data :
    for line in log_data :
        if "Failed" in line :
            parts = line.split()
            ip_index = parts.index("from") + 1
            ip = parts[ip_index]
            ip_counts[ip] += 1
            
ranked_ips = ip_counts.most_common()
for ip, count in ranked_ips:
    print(f"{ip}  —  {count} failed attempts")        