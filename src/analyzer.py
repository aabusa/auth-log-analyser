import sys
from collections import Counter
import argparse

parser = argparse.ArgumentParser(

    description="Log analysing Tool For Brute Force Attempts "
)
parser.add_argument(
    "--logfile",
    required = True,
    help="Path to the authentication log file to analyse"
)

parser.add_argument(
    "--threshold",
    type = int,
    default = 10,
    help = "Number of failed attempts before an IP is flagged as suspicious (default: 10)"
)

args = parser.parse_args()

print(f"Using log file: {args.logfile}")
print(f"Maximum allowed threshold: {args.threshold}")

ip_counts = Counter()
try:
    with open(args.logfile , "r") as log_data :
        for line in log_data :
            if "Failed" in line and "from" in line :
                parts = line.split()
                ip_index = parts.index("from") + 1
                ip = parts[ip_index]
                ip_counts[ip] += 1
except FileNotFoundError:
     print(f"Error: could not find log file '{args.logfile}'")
     sys.exit(1)
            
ranked_ips = ip_counts.most_common()
for ip, count in ranked_ips:
    if count >= args.threshold :
        print("Ip suspected of brute force attempt " ,ip , "Failed Attempts",count)