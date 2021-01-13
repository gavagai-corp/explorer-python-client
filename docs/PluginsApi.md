# explorer_client.PluginsApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plugin_details**](PluginsApi.md#get_plugin_details) | **GET** /plugins/{id} | Get Plugin
[**get_plugins**](PluginsApi.md#get_plugins) | **GET** /plugins | Get Plugins
[**get_survey**](PluginsApi.md#get_survey) | **GET** /plugins/survey_monkey/surveys/{id} | Get Survey
[**get_surveys**](PluginsApi.md#get_surveys) | **GET** /plugins/survey_monkey/surveys | Get Surveys
[**import_survey**](PluginsApi.md#import_survey) | **POST** /plugins/survey_monkey/surveys/{id}/import | Import Survey
[**survey_monkey_auth**](PluginsApi.md#survey_monkey_auth) | **GET** /plugins/survey_monkey/auth | Authenticate the survey monkey plugin
[**survey_monkey_callback**](PluginsApi.md#survey_monkey_callback) | **GET** /plugins/survey_monkey/callback | Callback endpoint for the survey monkey plugin


# **get_plugin_details**
> PluginDetails get_plugin_details(id)

Get Plugin

Get plugin information by pluginId

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
    api_instance = explorer_client.PluginsApi(api_client)
    id = 56 # int | 

    try:
        # Get Plugin
        api_response = api_instance.get_plugin_details(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugin_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginDetails**](PluginDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins**
> list[Plugin] get_plugins()

Get Plugins

Get the list of supported plugins

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
    api_instance = explorer_client.PluginsApi(api_client)
    
    try:
        # Get Plugins
        api_response = api_instance.get_plugins()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Plugin]**](Plugin.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey**
> Survey get_survey(id)

Get Survey

Get the details of a Survey available in your Survey Monkey account

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
    api_instance = explorer_client.PluginsApi(api_client)
    id = 56 # int | 

    try:
        # Get Survey
        api_response = api_instance.get_survey(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Survey**](Survey.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surveys**
> list[SurveyInfo] get_surveys()

Get Surveys

Get the list of Surveys available in your Survey Monkey account

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
    api_instance = explorer_client.PluginsApi(api_client)
    
    try:
        # Get Surveys
        api_response = api_instance.get_surveys()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_surveys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SurveyInfo]**](SurveyInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_survey**
> PluginDetails import_survey(id)

Import Survey

Import the survey as a project in explorer. This method will return a HTTP 200 response if the import was successfully started. The project will be saved once the import is complete

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
    api_instance = explorer_client.PluginsApi(api_client)
    id = 56 # int | 

    try:
        # Import Survey
        api_response = api_instance.import_survey(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->import_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginDetails**](PluginDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **survey_monkey_auth**
> survey_monkey_auth(redirect_url=redirect_url)

Authenticate the survey monkey plugin

Create a link with this url and let the user click on it to initialize survey monkey's oauth process. The redirectUrl is the final destination the browser ends up. The method will not return any data; it just redirects the browser.

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
    api_instance = explorer_client.PluginsApi(api_client)
    redirect_url = 'redirect_url_example' # str |  (optional)

    try:
        # Authenticate the survey monkey plugin
        api_instance.survey_monkey_auth(redirect_url=redirect_url)
    except ApiException as e:
        print("Exception when calling PluginsApi->survey_monkey_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_url** | **str**|  | [optional] 

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **survey_monkey_callback**
> survey_monkey_callback()

Callback endpoint for the survey monkey plugin

Endpoint called by survey monkey oauth process. This endpoint should not be used by any client. The method will not return any data; it just redirects the browser.

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
    api_instance = explorer_client.PluginsApi(api_client)
    
    try:
        # Callback endpoint for the survey monkey plugin
        api_instance.survey_monkey_callback()
    except ApiException as e:
        print("Exception when calling PluginsApi->survey_monkey_callback: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

