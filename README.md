# Auth Log Analyzer

A Python tool that scans authentication logs and flags IP addresses
making suspicious numbers of failed login attempts — a common sign
of a brute-force attack.

## Why I built this
[A sentence or two: I'm learning blue-team/SOC fundamentals, and log
analysis is the bread and butter of detection work. This is project 1
of a series building toward a small detection pipeline.]

## Features
- Parses standard auth log files
- Counts failed login attempts per IP
- Flags IPs that cross a configurable threshold
- (more as you add them)

## Installation
\`\`\`
git clone https://aabusa/auth-log-analyzer
cd auth-log-analyzer
python -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\activate
\`\`\`

## Usage
\`\`\`
python src/analyzer.py data/sample_auth.log
\`\`\`

## Example output
[paste real output here once it works]

## What I learned
[fill this in as you go — this section is gold for recruiters]

## Future improvements
- [ ] Support multiple log formats
- [ ] Add time-window detection

## License
MIT