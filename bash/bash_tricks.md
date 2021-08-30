# Open editor for extended/complex commands
`ctrl+x+e`

# Get DNS and networking information
`dig <hostname>`

`whois -v <ip_address> | grep origin -i`

Create a file of patterns to search for and use that to search for multiple strings at once:

`whois -v <ip_address> | grep -i --file=patterns`

-i ignores case

-E allows for regex in the patterns file:

`grep -E -i --file=patterns`

# Searching for sensitive data and strings in files and folders
`grep -r "my secert pattern" .`


```
$ grep -r password .
./thistle/cisco/expressway_v1.py:    >>> demoserver = expressway.Expressway('exp.example.com', 'username', 'password')
./thistle/cisco/expressway_v1.py:        password: admin password for accessing the web GUI
./thistle/cisco/expressway_v1.py:    def __init__(self, hostname: str, username: str, password: str):
./thistle/cisco/expressway_v1.py:        self.exp_pass = password
./thistle/cisco/expressway_v1.py:    def __init__(self, hostname, username, password):
./thistle/cisco/expressway_v1.py:        super().__init__(hostname, username, password)
./thistle/cisco/expressway_v1.py:    def __init__(self, hostname, username, password):
./thistle/cisco/expressway_v1.py:        super().__init__(hostname, username, password)
```

AWK + GREP + SED
https://arstechnica.com/gadgets/2021/08/linux-bsd-command-line-101-using-awk-sed-and-grep-in-the-terminal/
