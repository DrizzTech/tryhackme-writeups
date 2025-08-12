# 7-Day Skill Building Roadmap

## Day 1 – Networking 101  
**Goal:** Understand how devices talk to each other.

- [ ] Learn IP addresses (IPv4 basics)  
- [ ] Learn Ports & protocols (TCP vs UDP)  
- [x] Learn What DNS does  

### Practice  
- [x] Run `ping`, `traceroute`, `nslookup`, `curl` on your own network (at least 3 times each)  
- [x] Complete TryHackMe room: Intro to Networking  

### Quota  
- [ ] Complete the TryHackMe room  
- [x] Run all commands at least 3 times  

---

## Day 2 – Linux Basics  
**Goal:** Move confidently in a Linux terminal.

- [ ] Learn commands: `ls`, `cd`, `pwd`, `mkdir`, `rm`, `cat`, `nano`  
- [ ] Learn File permissions (`chmod`, `chown`)  

### Practice  
- [ ] Make a folder, create a file, change its permissions, delete it  
- [ ] Complete TryHackMe room: Linux Fundamentals Part 1  

### Quota  
- [ ] Finish Part 1  
- [ ] Create a “hacker playground” folder for future work  

---

## Day 3 – More Linux + Navigation  
**Goal:** Be able to find anything in a system.

- [ ] Learn commands: `find`, `grep`, `head`, `tail`, `less`, `history`  
- [ ] Understand `$PATH` and environment variables  

### Practice  
- [ ] Search for a file with `find`  
- [ ] Search for a keyword in a file with `grep`  
- [ ] Complete TryHackMe: Linux Fundamentals Part 2  

### Quota  
- [ ] Complete Part 2  
- [ ] Find and grep at least 3 things in your home directory  

---

## Day 4 – Basic Python for Security  
**Goal:** Automate small tasks with Python.

- [ ] Learn Variables, loops, conditionals  
- [ ] Learn reading & writing files  
- [ ] Learn using the `requests` library  

### Practice  
- [ ] Make a Python script to request a web page and print the first 200 characters  
- [ ] Bonus: Write a port scanner for ports 1–100 on `scanme.nmap.org`  

### Quota  
- [ ] 2 small scripts working without errors  

---

## Day 5 – Reconnaissance  
**Goal:** Find info about a target before touching it.

- [ ] Learn Whois lookups, DNS lookups, Google Dorking basics  
- [ ] Learn What Shodan is and why it’s powerful  

### Practice  
- [ ] Use `whois` on a domain you own or a public one  
- [ ] Find an interesting result with a Google dork query  
- [ ] Complete TryHackMe: Intro to Researching  

### Quota  
- [ ] Document 3 pieces of intel you find  

---

## Day 6 – Linux Fundamentals Part 3  
**Goal:** Learn enough Linux to operate like a hacker.

- [ ] Learn Package managers (`apt`, `yum`)  
- [ ] Learn Archiving/compression (`tar`, `zip`, `unzip`)  
- [ ] Learn Process management (`ps`, `top`, `kill`)  

### Practice  
- [ ] Install a package  
- [ ] Compress a folder  
- [ ] Kill a process you start  
- [ ] Complete TryHackMe Linux Fundamentals Part 3  

### Quota  
- [ ] Complete Part 3  
- [ ] Install and run `nmap`  

---

## Day 7 – Mini-Project: Your First Recon Script  
**Goal:** Combine skills into something real.

- [ ] Learn how to parse command-line arguments in Python (`argparse`)  

### Project  
- [ ] Make a Python script that:  
  - Takes a domain name as input  
  - Runs `whois` on it  
  - Runs `nslookup` on it  
  - Saves results to a text file  

### Quota  
- [ ] Script runs without errors  
- [ ] Works on at least 2 domains  
