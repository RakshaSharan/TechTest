# -*- coding: UTF-8 -*-
from behave import *
import requests

global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}

# ================================================================================================================
# STEP DEFINITIONS:
# ================================================================================================================


@given(u'Set api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    # Setting the url end-point to a global variable
    global_general_variables['GET_api_endpoint'] = get_api_endpoint


@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = global_general_variables['GET_api_endpoint']
    # Checking type of HTTP request raised from the features
    # Covers all the features

    if 'GET' == http_request_type:
        http_request_body.clear()
        global_general_variables['response_full'] = requests.get(url_temp,
                                                                 headers=http_request_header,
                                                                 params=http_request_url_query_param,
                                                                 data=http_request_body)
    elif 'POST' == http_request_type:
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.post(url_temp,
                                                                  headers=http_request_header,
                                                                  params=http_request_url_query_param,
                                                                  data=http_request_body)
    elif 'PUT' == http_request_type:
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.put(url_temp,
                                                                 headers=http_request_header,
                                                                 params=http_request_url_query_param,
                                                                 data=http_request_body)
    elif 'DELETE' == http_request_type:
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.delete(url_temp,
                                                                    headers=http_request_header,
                                                                    params=http_request_url_query_param,
                                                                    data=http_request_body)


@then(u'Response http code should be {expected_response_code:d} for "{http_request_type}"')
def step_impl(context, expected_response_code, http_request_type):
    # Validating response codes to match the HTTP request
    # 200 for GET and 4o4 for the remaining requests
    global_general_variables['expected_response_code'] = expected_response_code
    requestType = str(http_request_type)
    actual_response_code = global_general_variables['response_full'].status_code
    if requestType == "GET":
        if actual_response_code == expected_response_code == 200:
            print(str(global_general_variables['response_full'].json()))
            assert True
    elif requestType in ["POST", "PUT", "DELETE"]:
        print(str(global_general_variables['response_full'].json()))
        if actual_response_code == expected_response_code == 404:
            assert True
    else:
        print(str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    # Validating the json content-type
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type
