# explorer_client.ProductsApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credit_price**](ProductsApi.md#get_credit_price) | **GET** /products/creditPrice | Get Credit Price
[**get_product_plans**](ProductsApi.md#get_product_plans) | **GET** /products | Get Product Plans


# **get_credit_price**
> CreditPrice get_credit_price()

Get Credit Price

Retrieves the credit price for the user, which can be used to purchase credits

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
    api_instance = explorer_client.ProductsApi(api_client)
    
    try:
        # Get Credit Price
        api_response = api_instance.get_credit_price()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_credit_price: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreditPrice**](CreditPrice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available credit tiers and associated credits and prices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_plans**
> list[ProductPlan] get_product_plans()

Get Product Plans

Retrieves the available product plans to which the logged in user can subscribe

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
    api_instance = explorer_client.ProductsApi(api_client)
    
    try:
        # Get Product Plans
        api_response = api_instance.get_product_plans()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductPlan]**](ProductPlan.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available product plans |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

