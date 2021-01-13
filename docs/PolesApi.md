# explorer_client.PolesApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pole**](PolesApi.md#create_pole) | **POST** /poles | Create Pole
[**delete_pole**](PolesApi.md#delete_pole) | **DELETE** /poles/{id} | Delete Pole
[**get_pole**](PolesApi.md#get_pole) | **GET** /poles/{id} | Get Pole
[**get_poles**](PolesApi.md#get_poles) | **GET** /poles | Get Poles
[**get_suggestions_for_pole**](PolesApi.md#get_suggestions_for_pole) | **GET** /poles/{id}/suggest | Get Pole Suggestions
[**update_pole**](PolesApi.md#update_pole) | **PUT** /poles/{id} | Update Pole


# **create_pole**
> Pole create_pole(pole_request=pole_request)

Create Pole

For an authenticated user, this method allows the user to create a pole

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
    api_instance = explorer_client.PolesApi(api_client)
    pole_request = explorer_client.PoleRequest() # PoleRequest | The pole to be created (optional)

    try:
        # Create Pole
        api_response = api_instance.create_pole(pole_request=pole_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolesApi->create_pole: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pole_request** | [**PoleRequest**](PoleRequest.md)| The pole to be created | [optional] 

### Return type

[**Pole**](Pole.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created pole, with the id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pole**
> Pole delete_pole(id)

Delete Pole

For an authenticated user, this method deletes a pole, if he has sufficient rights

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
    api_instance = explorer_client.PolesApi(api_client)
    id = 56 # int | The poleId which is to be deleted

    try:
        # Delete Pole
        api_response = api_instance.delete_pole(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolesApi->delete_pole: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The poleId which is to be deleted | 

### Return type

[**Pole**](Pole.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted pole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pole**
> Pole get_pole(id)

Get Pole

For an authenticated user, this method retrieves the details of a pole specified by an id, if the user has access to it.

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
    api_instance = explorer_client.PolesApi(api_client)
    id = 56 # int | The id of the pole to retrieve

    try:
        # Get Pole
        api_response = api_instance.get_pole(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolesApi->get_pole: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the pole to retrieve | 

### Return type

[**Pole**](Pole.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested pole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poles**
> PolesResponse get_poles()

Get Poles

For an authenticated user, this method retrieves the list of pole  which the user can edit

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
    api_instance = explorer_client.PolesApi(api_client)
    
    try:
        # Get Poles
        api_response = api_instance.get_poles()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolesApi->get_poles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PolesResponse**](PolesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The poles which the user can edit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suggestions_for_pole**
> PoleSuggestions get_suggestions_for_pole(id)

Get Pole Suggestions

For an authenticated user, this method retrieves suggestions for a pole, if he has access to it

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
    api_instance = explorer_client.PolesApi(api_client)
    id = 56 # int | The poleId for which suggestions are required

    try:
        # Get Pole Suggestions
        api_response = api_instance.get_suggestions_for_pole(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolesApi->get_suggestions_for_pole: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The poleId for which suggestions are required | 

### Return type

[**PoleSuggestions**](PoleSuggestions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The suggestions with the pole itself |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pole**
> Pole update_pole(id, clear_contents=clear_contents, pole_request=pole_request)

Update Pole

For an authenticated user, this method allows the user to update a pole, if he has access to it

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
    api_instance = explorer_client.PolesApi(api_client)
    id = 56 # int | The id of the pole to be updated
clear_contents = True # bool | If this flag is set, the pole parts are cleared and are populated with the pole parts in the json payload. If it is not set, the pole parts in the payload are appended to the existing pole parts (optional) (default to True)
pole_request = explorer_client.PoleRequest() # PoleRequest | The pole to be updated (optional)

    try:
        # Update Pole
        api_response = api_instance.update_pole(id, clear_contents=clear_contents, pole_request=pole_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolesApi->update_pole: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the pole to be updated | 
 **clear_contents** | **bool**| If this flag is set, the pole parts are cleared and are populated with the pole parts in the json payload. If it is not set, the pole parts in the payload are appended to the existing pole parts | [optional] [default to True]
 **pole_request** | [**PoleRequest**](PoleRequest.md)| The pole to be updated | [optional] 

### Return type

[**Pole**](Pole.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated pole, with the id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

