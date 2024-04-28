#! /bin/python3

import os
import subprocess
# Check if the environment variable 'COMPOSABL_LICENSE' is set
composabl_license = os.getenv('COMPOSABL_LICENSE')
if not composabl_license:
    print("COMPOSABL_LICENSE is not set.")
    print( "you must get a license from Compsosabl and EXPORT it as an environment variable")
else:
    print("license is set" )


import json

def generate_config(license_key, target, image, env_name, workers, num_gpus):
    # Assuming this function generates a configuration dictionary based on the input parameters
    return {
        "target": target,
        "image": image,
        "env_name": env_name,
        "workers": workers,
        "num_gpus": num_gpus
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
 

def update_agent_config(config_data):
    dirty=False
    print( config_data)

    if not 'runtime' in config_data:
        print( "no runtuime")
        config_data['runtime']={}
        config_data['runtime']["workers"]=1
        config_data['runtime']["num_gpus"] = 0
        dirty =True
 
    if 'workers' in config_data['runtime'] and args.workers != -1:
        if config_data['runtime']["workers"] != args.workers:
            config_data['runtime']["workers"] = args.workers
            dirty = True
    if 'num_gpus' in config_data['runtime'] and args.num_gpus != -1 :
        if config_data['runtime']["num_gpus"] != args.num_gpus:
            config_data['runtime']["num_gpus"] = args.num_gpus
            dirty = True

    print(config_data)      
    if dirty == True:
        print( "is dirty")

        # Read the JSON file into a dictionary
        try:
            with open('agent_config.json', 'w') as file:
                json.dump(config_data,file)
        except FileNotFoundError:
            print(f" The file was not found. no agent config overrides applied")
        except json.JSONDecodeError:
            print(f"Error: The file ' is not a valid JSON file.")
        # Handle other potential exceptions, such as permission errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}")




        


import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Process some inputs.")

# Define positional arguments
parser.add_argument("command", type=str, help="The command to execute - teach or operate")
parser.add_argument("name", type=str, help="The name of the approch")

# Define optional arguments
parser.add_argument("--workers", type=int, help="Number of workers", default=-1)
parser.add_argument("--num_gpus", type=int, help="Number of GPUs", default=-1)

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Command: {args.command}")
print(f"Name: {args.name}")
print(f"Workers: {args.workers}")
print(f"Number of GPUs: {args.num_gpus}")


import subprocess


# This line ensures that the function runs only when the script is executed directly,python
# and not when imported as
#  a module.
if __name__ == '__main__':
    print( 'foo')
    if args.command =='teach':
        print(f'run {args.name}')
        cur_dir=os.getcwd()
        agent_dir=f'{cur_dir}/{args.name}'
        print(agent_dir)
        os.chdir( agent_dir)
        agent_config = load_agent_config()
        update_agent_config( agent_config )
        result = subprocess.call(["python3","agent.py"])
        #print(result)



