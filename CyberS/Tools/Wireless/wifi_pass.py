import subprocess
import re

def get_profiles():
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], 
                                       shell=True, 
                                       stderr=subprocess.DEVNULL, 
                                       stdin=subprocess.DEVNULL).decode('latin-1')
        return re.findall(r":\s(.*?)\r", output)
    except:
        return []

def get_password(profile):
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', 
                                        profile, 'key=clear'], 
                                       shell=True, 
                                       stderr=subprocess.DEVNULL, 
                                       stdin=subprocess.DEVNULL).decode('latin-1')
        return re.search(r"Key Content\s*:\s(.*?)\r", output).group(1)
    except:
        return None

profiles = get_profiles()
print("="*60)
for p in profiles:
    pwd = get_password(p)
    print(f"{p:<30} | {pwd if pwd else '<Não disponível>'}")