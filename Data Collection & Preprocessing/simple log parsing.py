import re      
           
def parse_generic_log(log_line):
    # This regex is a placeholder. You'll need to craft one
    # specific to the log format you're parsing (e.g., Sysmon, Apache, etc.).
    # Look for patterns that indicate process creation, file writes, etc. 
    match =     re.search(r"timestamp=(.*?)\s+event_type=(.*?)\s+user=(.*?)\s+process=(.*?)\s+file=(.*)", log_line)
    if match:
        # Return a dictionary with extracted fields
        return {
            'timestamp': match.group(1),
            'event_type': match.group(2),
            'user': match.group(3),
            'process': match.group(4),
            'file': match.group(5)
        }
    return None
  
# Example usage:
# with open("path/to/your/endpoint_log.txt", "r") as f:
#     for line in f:
#         parsed_event = parse_generic_log(line.strip())
#         if parsed_event:
#             print(parsed_event) # Store this in a list or database
