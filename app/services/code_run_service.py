# import judge0

# def code_run(payload: str):
#     return judge0.api.async_execute(client=None, submissions=None, source_code=payload, test_cases=None)


# Pass an empty dictionary for globals, and turn off standard built-ins
restricted_globals = {"__builtins__": {}} 
restricted_locals = {}


def code_run(payload: str):
    exec(payload, restricted_globals, restricted_locals)
    return restricted_locals['x']

