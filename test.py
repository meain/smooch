from synapse import Synapse

synapse = Synapse()


@synapse.connect('/hello')
def robo(name, robot=False):
    if robot:
        return f"{name} is a robot"
    else:
        return f"{name} is not a robot"


@synapse.connect('/ok')
def ok(okn):
    return ( f"{okn}" )

# robo('meain')

synapse.start(debug=True)
# synapse.start()

