# falsk with better defaults as a wrapper

from synapse import Synapse

synapse = Synapse()


@synapse.connect('/hello')
def robo(name, robot=False):
    if robot:
        return f"{name} is a robot"
    else:
        return f"{name} is not a robot"


# @synapse.connect('/ok')
# def ok(okn):
#     return ( f"{okn}" )

synapse.start()
