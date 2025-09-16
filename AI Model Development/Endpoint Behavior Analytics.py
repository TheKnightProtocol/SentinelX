import numpy as np             
    
def  detect_process_activity_anomaly(historical_counts, current_count, std_dev_multiplier=3):
    # This is a very simple statistical approach. ML models would be more robust.
    mean_count = np.mean(historical_counts)
    std_dev_count = np.std(historical_counts)

    upper_bound = mean_count + std_dev_multiplier * std_dev_count
    lower_bound = mean_count - std_dev_multiplier * std_dev_count

    if not (lower_bound <= current_count <= upper_bound):
        return True # Anomaly detected
    return False

# Usage:
# historical_daily_process_creations = [50, 55, 48, 60, 52] # From previous days
# current_day_creations = 150 # A spike!
# if detect_process_activity_anomaly(historical_daily_process_creations, current_day_creations):
#     print("Alert: Unusual number of processes created on endpoint!")
