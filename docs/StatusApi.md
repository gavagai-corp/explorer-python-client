# explorer_client.StatusApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_service**](StatusApi.md#ping_service) | **GET** /status | Get System Status


# **ping_service**
> HealthCheckReport ping_service()

Get System Status

Check if the Explorer service is healthy

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import explorer_client
from explorer_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.gavagai.se/explorer/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = explorer_client.Configuration(
    host = "https://api.gavagai.se/explorer/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = explorer_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with explorer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = explorer_client.StatusApi(api_client)
    
    try:
        # Get System Status
        api_response = api_instance.ping_service()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->ping_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheckReport**](HealthCheckReport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | an object of the type HealthCheckReport containing results from all the contained health checks. Currently, the following health checks are enabled:&lt;p&gt;&lt;ul&gt;&lt;li&gt; DB_CHECK_TIMESTAMP: a database query to find the current time of the database server and compare it to the current time of the client server.&lt;/li&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

