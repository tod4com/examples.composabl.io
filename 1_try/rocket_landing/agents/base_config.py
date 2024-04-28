import os
import json
import sys

license_key = os.environ["COMPOSABL_LICENSE"]
PATH: str = os.path.dirname(os.path.realpath(__file__))
PATH_HISTORY: str = f"{PATH}/history"

from sensors import sensors

from use_case_config import use_case_config
def load_agent_config():
# this must be run after the  os.chdir in the launcher

# Read the JSON file into a dictionary
    config_data={}
    json_filename=f"agent_config.json"
    print( json_filename)
    try:
        with open(json_filename, 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        print(f" The file was not found. no agent config overrides applied")
    except json.JSONDecodeError:
        print(f"Error: The file ' is not a valid JSON file.")
    # Handle other potential exceptions, such as permission errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return config_data

def merge_configs( ):
    merged_dict = {**use_case_config, **agent_config}
    return merged_dict

    
agent_config = load_agent_config()
config=merge_configs( )

