import os
import sys


print( "start of the agent===============================")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from base_config import *

print("after agent=============================================")
from composabl import Agent, Runtime, Scenario, Sensor, Skill
from teacher import NavigationTeacher


from scenarios import Navigation_scenarios



def run_agent():
    Navigation_skill = Skill("Navigation", NavigationTeacher)

    for scenario_dict in Navigation_scenarios:
        scenario = Scenario(scenario_dict)
        Navigation_skill.add_scenario(scenario)

    runtime = Runtime(config)
    agent = Agent()
    agent.add_sensors(sensors)

    agent.add_skill(Navigation_skill)

    # Load a pre-trained agent
    try:
        if len(os.listdir(PATH_CHECKPOINTS)) > 0:
            agent.load(PATH_CHECKPOINTS)
    except Exception:
        print("|-- No checkpoints found. Training from scratch...")

    # Start training the agent
    runtime.train(agent, train_iters=2)

    # Save the trained agent
    agent.export(PATH_CHECKPOINTS)


if __name__ == "__main__":
    print("the agent")
    #run_agent()
