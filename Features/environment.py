# -- FILE: Features/environment.py

def before_all(context):
    context.baseURL = context.config.userdata['baseURL']
