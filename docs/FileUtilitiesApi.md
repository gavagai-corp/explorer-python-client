# explorer_client.FileUtilitiesApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_details**](FileUtilitiesApi.md#get_file_details) | **POST** /file-utilities/details | Get File Details
[**get_first_row**](FileUtilitiesApi.md#get_first_row) | **POST** /file-utilities/header_row | Get First Row


# **get_file_details**
> FileDetails get_file_details(file, file_name, encoding=encoding)

Get File Details

For an authenticated user, this method will upload a file and return details pertaining to the file. The supported file types are Microsoft Excel 2007-20013 (.xlsx), Microsoft Excel 97-2003 (.xls) and Text CSV (.csv). If the file has any other prefix or if the parsing fails, an error message will be returned. The maximum allowed file size is 200MB. The multipart form data parts need to be 'file' with the binary data and 'fileName' with the file name as plain text

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
    api_instance = explorer_client.FileUtilitiesApi(api_client)
    file = '/path/to/file' # file | input file
file_name = 'file_name_example' # str | 
encoding = 'encoding_example' # str | Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. (optional)

    try:
        # Get File Details
        api_response = api_instance.get_file_details(file, file_name, encoding=encoding)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileUtilitiesApi->get_file_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| input file | 
 **file_name** | **str**|  | 
 **encoding** | **str**| Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. | [optional] 

### Return type

[**FileDetails**](FileDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON structure representing the details pertaining to the file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_first_row**
> HeaderRow get_first_row(file, file_name, encoding=encoding)

Get First Row

For an authenticated user, this method will upload a file and return the first row in the file. The supported file types are Microsoft Excel 2007-20013 (.xlsx), Microsoft Excel 97-2003 (.xls) and Text CSV (.csv). If the file has any other prefix or if the parsing fails, an error message will be returned. The multipart form data parts need to be 'file' with the binary data and 'fileName' with the file name as plain text

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
    api_instance = explorer_client.FileUtilitiesApi(api_client)
    file = '/path/to/file' # file | input file
file_name = 'file_name_example' # str | 
encoding = 'encoding_example' # str | Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. (optional)

    try:
        # Get First Row
        api_response = api_instance.get_first_row(file, file_name, encoding=encoding)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileUtilitiesApi->get_first_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| input file | 
 **file_name** | **str**|  | 
 **encoding** | **str**| Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. | [optional] 

### Return type

[**HeaderRow**](HeaderRow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of strings, one for each field in the first row. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

