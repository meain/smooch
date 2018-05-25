from synapse import synapse

model = load_model()

'''
GET and POST will both be enable by default
auth_lambda_callback: callback function which get request info like origin, headers, data (optional) [returns bool]
log_lambda_callback: callback function which get request info like origin, headers, data (optional) [returns None]
'''

@synapse('/user', auth=auth_lambda_callback, log=log_lambda_callback)
def fit(text, user=0):
    result = { user: user }
    return result


synapse.start(url, port, debug=True)
