# Cybersecurity Skills Roadmap

## Basics
- [ ] Understand computer networks ([TryHackMe: Introduction to Networking](https://tryhackme.com/room/introtonetworking)) 
- [ ] Learn Linux basics ([TryHackMe: Linux Fundamentals 1](https://tryhackme.com/room/linuxfundamentalspart1)) 
- [ ] Get comfortable with Windows internals ([TryHackMe: Windows Fundamentals 1](https://tryhackme.com/room/windowsfundamentals1xbx)) 
- [ ] Understand basic programming (see [Python for Hackers](#python-for-hackers--practice-tasks)) 

## Tools & Platforms
- [ ] Set up and use Virtual Machines ([VirtualBox Download](https://www.virtualbox.org/wiki/Downloads)) 
- [ ] Practice on TryHackMe beginner labs ([Pre Security Path](https://tryhackme.com/path/outline/presecurity)) 
- [ ] Learn how to use OpenVPN ([TryHackMe: OpenVPN](https://tryhackme.com/room/openvpn)) 
- [ ] Get familiar with pentesting tools ([TryHackMe: CC: Pentesting](https://tryhackme.com/room/ccpentesting)) 

## Skills Development
- [ ] Learn scanning & enumeration ([TryHackMe: Nmap](https://tryhackme.com/room/furthernmap)) 
- [ ] Practice exploiting vulnerabilities ([TryHackMe: Vulnversity](https://tryhackme.com/room/vulnversity)) 
- [ ] Understand privilege escalation ([Linux PrivEsc](https://tryhackme.com/room/linuxprivesc), [Windows PrivEsc](https://tryhackme.com/room/windowsprivesc20)) 
- [ ] Learn basic web hacking ([OWASP Top 10](https://tryhackme.com/room/owasptop10)) 
- [ ] Study password attacks ([Hydra](https://tryhackme.com/room/hydra)) 
- [ ] Practice social engineering basics ([Introduction to Social Engineering](https://tryhackme.com/room/socialengineeringbasics)) 

## Theory & Methodology
- [ ] Understand hacker methodology ([The Hacker Methodology](https://tryhackme.com/room/hackermethodology)) 
- [ ] Learn security concepts ([Pre Security Path: Security Principles](https://tryhackme.com/room/securityprinciples)) 
- [ ] Study cryptography basics ([Cryptography for Beginners](https://tryhackme.com/room/cryptographybeginners)) 
- [ ] Study incident response basics ([TryHackMe: Intro to Incident Response](https://tryhackme.com/room/introtoincidentresponse)) 

## Projects & Practice
- [ ] Complete at least 10 beginner-level TryHackMe rooms 
- [ ] Document learnings ([GitHub Pages Guide](https://pages.github.com/)) 
- [ ] Participate in Capture The Flag (CTF) ([CTFtime.org](https://ctftime.org/)) 
- [ ] Build a home lab ([TryHackMe: Intro to Cybersecurity Lab Setup](https://tryhackme.com/room/labsetup)) 

---

## Python for Hackers – Practice Tasks

- [ ] **Variables & Math:**  
  Write a script that takes two numbers, adds them, and prints the result.

- [ ] **If/Else:**  
  Ask the user for an IP address. If it starts with "192.168", print "Local network", else print "External".

- [ ] **Loops:**  
  Loop through the numbers 1–5 and print `Scanning port X` for each.

- [ ] **Functions:**  
  Write a function `scan_target(ip)` that just prints `Scanning {ip}` and call it on a list of 3 IPs.

- [ ] **File Read/Write:**  
  Read a file called `targets.txt` (one IP per line) and print them.

- [ ] **Command-line Arguments:**  
  A script that takes a filename from `sys.argv` and prints its contents.

- [ ] **Lists & Dictionaries:**  
  Store IPs in a list and service names in a dictionary, then print them.

- [ ] **os & subprocess:**  
  Use `subprocess.run()` to execute `ping -c 1 <target>` for each IP in a list.

- [ ] **Requests Library:**  
  Fetch the HTML from `https://example.com` and print the first 200 characters.

- [ ] **BeautifulSoup:**  
  Find and print all links (`<a>` tags) from a given webpage.

- [ ] **Regex (re module):**  
  Extract all email addresses from a string.

- [ ] **JSON:**  
  Load a JSON file containing `{"username": "admin", "password": "1234"}` and print the password.

- [ ] **Automation:**  
  Read IPs from a file and run `nmap -sV` on each (use `subprocess`).

- [ ] **Modify Exploit Scripts:**  
  Download a Python exploit from Exploit-DB, change the target IP, and run it in a safe lab environment.
