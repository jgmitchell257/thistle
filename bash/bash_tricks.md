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

# Searching for sensitive data and strings in files and folders
`grep -r "my secert pattern" .`