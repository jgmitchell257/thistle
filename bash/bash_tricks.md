# Open editor for extended/complex commands
ctrl+x+e

# Get DNS and networking information
dig <hostname>
whois -v <ip_address> | grep origin -i

Create a file of patterns to search for and use that to search for multiple strings at once:
whois -v <ip_address> | grep -i --file=patterns

-i ignores case
-E allows for regex in the patterns file:
grep -E -i --file=patterns



# Useful links
https://spyse.com/
https://dnschecker.org/all-tools.php
https://iplocation.io/
https://awebanalysis.com/en/ip-tools/