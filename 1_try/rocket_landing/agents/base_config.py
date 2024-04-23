import os
import json

license_key = os.environ["COMPOSABL_LICENSE"]
PATH: str = os.path.dirname(os.path.realpath(__file__))
PATH_HISTORY: str = f"{PATH}/history"

from sensors import sensors

config = {
        "target": {
            "docker": {
                "image": "composabl/sim-starship"
            },
        },
        "env": {
            "name": "starship",
        },
        "training": {},
        "runtime": {
            "workers": 1
        }
    }

def load_agent_config():
# this must be run after the  os.chdir

# Read the JSON file into a dictionary
    config_data={}
    try:
        with open('agent_config.json', 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        print(f" The file was not found. no agent config overrides applied")
    except json.JSONDecodeError:
        print(f"Error: The file ' is not a valid JSON file.")
    # Handle other potential exceptions, such as permission errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return config_data

def merge_configs( config_data):
    print("merging")
    
merge_configs( {})