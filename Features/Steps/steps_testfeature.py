from behave import *
import requests

'''
from Features.contants import BASE_URL

print(f'Accessing endpoint as a constant: {BASE_URL}')
'''

global_general_variables = {}
http_request_header = {}


@given(u'return list of articles using baseURL')
def step_impl(context):
    print(context.baseURL)
    assert True


@when(u'"{http_req_type}" http returns {responseCode:d}')
def step_impl(context, http_req_type, responseCode):
    if http_req_type == "GET" or http_req_type == "HEAD":
        context.responseFULL = requests.get(context.baseURL)
        actualCode = global_general_variables["actualStatuscode"] = context.responseFULL.status_code

        if actualCode == responseCode:
            # print(context.responseFULL.text)
            assert True
        else:
            assert False, "Error {actualCode}"


@then(u'return single article url')
def step_impl(context):
    if global_general_variables["actualStatuscode"] == 200:
        context.singleURL = context.baseURL + "?id=2"
        # print(context.singleURL)
        assert True
    else:
        assert False
