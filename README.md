## How it works

The tool scans the log line by line. For each line recording a failed login, it pulls
out the source IP (the value following "from") and tallies it. Once the whole file is
processed, it ranks every offending IP by failure count and reports those at or above
the chosen threshold, so an analyst can tune sensitivity to their environment.

## Limitations / known blind spots

This is an intentionally simple detector, and being honest about what it *can't* catch
is part of understanding it:

- **Volume, not rate.** It counts total failures and ignores time. 10 failures in 10
  seconds (an attack) and 10 over a month (a forgetful user) look identical to it.
- **Evadable by "low and slow" attacks.** An attacker who stays just under the threshold
  is invisible to it.
- **Evadable by distributed attacks.** A botnet where 200 IPs each try 3 times slips
  through entirely, despite being a large coordinated attack.
- **Environment-dependent threshold.** The default of 10 suits this sample data; a busy
  production server may need a higher number to avoid false positives.
- **One log format.** It's tuned to the OpenSSH "Failed password ... from ..." pattern
  and won't parse other formats.

## Future improvements

- Time-window / rate-based detection (failures per minute, not just in total)
- Detect a *successful* login immediately following a burst of failures (a likely compromise)
- Support multiple log formats
- Output results to CSV or JSON for use by other tools
- More robust parsing using regular expressions

## What I learned

*(Rewrite this in your own words — it's the part a reviewer reads most closely. Some honest
starting points from building it:)*

- Parsing real-world log data, and why fixed-width assumptions break on variable-length
  fields like IP addresses
- Counting and ranking with Python's `collections.Counter`
- Building a proper command-line interface with `argparse`
- Writing defensive code — handling missing files and malformed lines instead of crashing
- The detection trade-off behind choosing a threshold (false positives vs. false negatives)

## Data source

Sample logs are from the [loghub](https://github.com/logpai/loghub) collection (OpenSSH
dataset), a freely available set of system logs for research.

## License

MIT