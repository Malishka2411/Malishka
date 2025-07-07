def convert_data_format_1(data):
    # convert from ISO timestamp to milliseconds
    pass

def convert_data_format_2(data):
    # might already be in the right format, just wrap appropriately
    pass
from datetime import datetime

def iso_to_millis(iso_str):
    dt = datetime.fromisoformat(iso_str.replace('Z', '+00:00'))
    return int(dt.timestamp() * 1000)
