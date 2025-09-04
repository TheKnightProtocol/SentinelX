import subprocess   
        
def block_ip_address(ip_to_block):
    # This requires elevated privileges (sudo) and is specific to Linux iptables.
    # In a real system, you'd interact with a firewall API or similar.     
    try: 
        command = ['sudo', 'iptables', '-A', 'INPUT', '-s', ip_to_block, '-j', 'DROP']
        subprocess.run(command, check=True) # check=True raises an error for non-zero exit codes
        print(f"Successfully added iptables rule to block {ip_to_block}")
    except subprocess.CalledProcessError as e:
        print(f"Error blocking IP {ip_to_block}: {e}")
    except FileNotFoundError:
        print("iptables command not found. Is it installed and in your PATH?")

# When your AI determines an IP is malicious and needs blocking:
# malicious_ip = "1.2.3.4".   
# block_ip_address(malicious_ip)
