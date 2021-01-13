# explorer_client.TonalityCustomizationApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tonality_customization**](TonalityCustomizationApi.md#create_tonality_customization) | **POST** /tonality-customizations | Create Tonality Customization
[**delete_tonality_customization**](TonalityCustomizationApi.md#delete_tonality_customization) | **DELETE** /tonality-customizations/{id} | Delete Tonality Customization
[**get_tonality_customization**](TonalityCustomizationApi.md#get_tonality_customization) | **GET** /tonality-customizations/{id} | Get Tonality Customization
[**get_tonality_customizations**](TonalityCustomizationApi.md#get_tonality_customizations) | **GET** /tonality-customizations | Get Tonality Customizations
[**get_tonality_details_for_terms**](TonalityCustomizationApi.md#get_tonality_details_for_terms) | **GET** /tonality-customizations/details | Get Term Tonalitites
[**update_tonality_customization**](TonalityCustomizationApi.md#update_tonality_customization) | **PUT** /tonality-customizations/{id} | Update Tonality Customization


# **create_tonality_customization**
> TonalityCustomization create_tonality_customization(tonality_customization_request)

Create Tonality Customization

Create a new tonality customization

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
    api_instance = explorer_client.TonalityCustomizationApi(api_client)
    tonality_customization_request = explorer_client.TonalityCustomizationRequest() # TonalityCustomizationRequest | TonalityCustomization the tonality customization to create

    try:
        # Create Tonality Customization
        api_response = api_instance.create_tonality_customization(tonality_customization_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TonalityCustomizationApi->create_tonality_customization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tonality_customization_request** | [**TonalityCustomizationRequest**](TonalityCustomizationRequest.md)| TonalityCustomization the tonality customization to create | 

### Return type

[**TonalityCustomization**](TonalityCustomization.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The suggestions with the pole itself |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tonality_customization**
> delete_tonality_customization(id)

Delete Tonality Customization

Delete a tonality customization

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
    api_instance = explorer_client.TonalityCustomizationApi(api_client)
    id = 56 # int | The id of the customization to delete

    try:
        # Delete Tonality Customization
        api_instance.delete_tonality_customization(id)
    except ApiException as e:
        print("Exception when calling TonalityCustomizationApi->delete_tonality_customization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the customization to delete | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tonality_customization**
> TonalityCustomization get_tonality_customization(id)

Get Tonality Customization

Retrieve a tonality customization identified by the specified id

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
    api_instance = explorer_client.TonalityCustomizationApi(api_client)
    id = 56 # int | The id of the customization to retrieve

    try:
        # Get Tonality Customization
        api_response = api_instance.get_tonality_customization(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TonalityCustomizationApi->get_tonality_customization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the customization to retrieve | 

### Return type

[**TonalityCustomization**](TonalityCustomization.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tonality customization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tonality_customizations**
> list[TonalityCustomizationInfo] get_tonality_customizations()

Get Tonality Customizations

Get the available tonality customizations available to the logged in user.

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
    api_instance = explorer_client.TonalityCustomizationApi(api_client)
    
    try:
        # Get Tonality Customizations
        api_response = api_instance.get_tonality_customizations()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TonalityCustomizationApi->get_tonality_customizations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TonalityCustomizationInfo]**](TonalityCustomizationInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tonality customizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tonality_details_for_terms**
> TermsTonalityDetails get_tonality_details_for_terms(terms, language)

Get Term Tonalitites

Get the tonality details of terms, currently, the list of tones to which they belong.

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
    api_instance = explorer_client.TonalityCustomizationApi(api_client)
    terms = ['terms_example'] # list[str] | The terms for which the details are required
language = 'language_example' # str | The language

    try:
        # Get Term Tonalitites
        api_response = api_instance.get_tonality_details_for_terms(terms, language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TonalityCustomizationApi->get_tonality_details_for_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terms** | [**list[str]**](str.md)| The terms for which the details are required | 
 **language** | **str**| The language | 

### Return type

[**TermsTonalityDetails**](TermsTonalityDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for the terms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tonality_customization**
> TonalityCustomization update_tonality_customization(id, tonality_customization_request)

Update Tonality Customization

Update a tonality customization identified by the specified id

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
    api_instance = explorer_client.TonalityCustomizationApi(api_client)
    id = 56 # int | The id of the customization to update
tonality_customization_request = explorer_client.TonalityCustomizationRequest() # TonalityCustomizationRequest | The updated tonality customization

    try:
        # Update Tonality Customization
        api_response = api_instance.update_tonality_customization(id, tonality_customization_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TonalityCustomizationApi->update_tonality_customization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the customization to update | 
 **tonality_customization_request** | [**TonalityCustomizationRequest**](TonalityCustomizationRequest.md)| The updated tonality customization | 

### Return type

[**TonalityCustomization**](TonalityCustomization.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The saved tonality customization  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

