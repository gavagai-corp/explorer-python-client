# explorer_client.AccountsApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_manager_invitation**](AccountsApi.md#accept_manager_invitation) | **PUT** /account/invitations/{id}/accept | Acccept Manager Invitation
[**cancel_account**](AccountsApi.md#cancel_account) | **DELETE** /account/cancel | Cancel Account
[**cancel_product_plan_migration**](AccountsApi.md#cancel_product_plan_migration) | **DELETE** /account/product/migration | Cancel Product Plan Migration
[**create_manager_invitation**](AccountsApi.md#create_manager_invitation) | **POST** /account/invitations | Create Manager Invitation
[**delete_managed_user**](AccountsApi.md#delete_managed_user) | **DELETE** /account/managedUsers/{userId} | Delete Managed User
[**delete_manager**](AccountsApi.md#delete_manager) | **DELETE** /account/manager | Delete manager
[**delete_manager_invitation**](AccountsApi.md#delete_manager_invitation) | **DELETE** /account/invitations/{id} | Delete Manager Invitation
[**get_account**](AccountsApi.md#get_account) | **GET** /account | Get Account
[**get_account_balance**](AccountsApi.md#get_account_balance) | **GET** /account/balance | Get Account Balance
[**get_credit_statistics**](AccountsApi.md#get_credit_statistics) | **GET** /account/credits/statistics | Get Credit Statistics
[**get_credits**](AccountsApi.md#get_credits) | **GET** /account/credits | Get Credits
[**get_manager_invitations**](AccountsApi.md#get_manager_invitations) | **GET** /account/invitations | Get Manager Invitations
[**get_pending_payment**](AccountsApi.md#get_pending_payment) | **GET** /account/pendingPayment | Get Pending Payments
[**get_product_plan**](AccountsApi.md#get_product_plan) | **GET** /account/product | Get Product Plan
[**get_usage**](AccountsApi.md#get_usage) | **GET** /account/usage | Get Usage
[**get_user_settings**](AccountsApi.md#get_user_settings) | **GET** /account/settings | Get User Settings
[**purchase_credits**](AccountsApi.md#purchase_credits) | **POST** /account/credits | Purchase Credits
[**reactivate_account**](AccountsApi.md#reactivate_account) | **POST** /account/reactivate | Reactivate Account
[**reject_manager_invitation**](AccountsApi.md#reject_manager_invitation) | **PUT** /account/invitations/{id}/reject | Reject Manager Invitation
[**set_product_plan**](AccountsApi.md#set_product_plan) | **PUT** /account/product | Set Product Plan
[**update_user_settings**](AccountsApi.md#update_user_settings) | **PUT** /account/settings | Update User Settings


# **accept_manager_invitation**
> accept_manager_invitation(id)

Acccept Manager Invitation

Accept a manager invitation. By accepting the invitation payments will be handled by your manager account.

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
    api_instance = explorer_client.AccountsApi(api_client)
    id = 56 # int | Id of the invitation

    try:
        # Acccept Manager Invitation
        api_instance.accept_manager_invitation(id)
    except ApiException as e:
        print("Exception when calling AccountsApi->accept_manager_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the invitation | 

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

# **cancel_account**
> cancel_account()

Cancel Account

Cancel the logged in user's account

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Cancel Account
        api_instance.cancel_account()
    except ApiException as e:
        print("Exception when calling AccountsApi->cancel_account: %s\n" % e)
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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_product_plan_migration**
> cancel_product_plan_migration()

Cancel Product Plan Migration

Cancel an upcoming migration to a product plan. If there is no scheduled migration,an exception is thrown

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Cancel Product Plan Migration
        api_instance.cancel_product_plan_migration()
    except ApiException as e:
        print("Exception when calling AccountsApi->cancel_product_plan_migration: %s\n" % e)
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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manager_invitation**
> ManagerInvitation create_manager_invitation(user_id=user_id)

Create Manager Invitation

Invite a user to be managed by you. Payments will be charged on your registered account. Note that the managed user will be able to accept overage payments.

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
    api_instance = explorer_client.AccountsApi(api_client)
    user_id = 'user_id_example' # str | The username of the user to invite (optional)

    try:
        # Create Manager Invitation
        api_response = api_instance.create_manager_invitation(user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->create_manager_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The username of the user to invite | [optional] 

### Return type

[**ManagerInvitation**](ManagerInvitation.md)

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

# **delete_managed_user**
> delete_managed_user(user_id)

Delete Managed User

Remove a managed user that has accepted your invitation. Note that this will cancel the user's account and they will need to reactivate it manually.

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
    api_instance = explorer_client.AccountsApi(api_client)
    user_id = 'user_id_example' # str | The username of the managed user to remove

    try:
        # Delete Managed User
        api_instance.delete_managed_user(user_id)
    except ApiException as e:
        print("Exception when calling AccountsApi->delete_managed_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The username of the managed user to remove | 

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

# **delete_manager**
> delete_manager()

Delete manager

Deletes the user's manager. Note that this will cancel your account and you will need to add payment details and reactivate.

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Delete manager
        api_instance.delete_manager()
    except ApiException as e:
        print("Exception when calling AccountsApi->delete_manager: %s\n" % e)
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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manager_invitation**
> delete_manager_invitation(id)

Delete Manager Invitation

Delete an invitation created by you.

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
    api_instance = explorer_client.AccountsApi(api_client)
    id = 56 # int | Id of the invitation

    try:
        # Delete Manager Invitation
        api_instance.delete_manager_invitation(id)
    except ApiException as e:
        print("Exception when calling AccountsApi->delete_manager_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the invitation | 

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

# **get_account**
> Account get_account()

Get Account

Get the manager of the account and the list of users that are managed by this account.

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Get Account
        api_response = api_instance.get_account()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

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

# **get_account_balance**
> AccountBalance get_account_balance()

Get Account Balance

Get the Explorer balance available for the logged in user. If the user has a manager, the balance available to the manager will be returned

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Get Account Balance
        api_response = api_instance.get_account_balance()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountBalance**](AccountBalance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available explorer balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_statistics**
> CreditStatistics get_credit_statistics(start_date=start_date, end_date=end_date, group_by=group_by, user_id=user_id)

Get Credit Statistics

Get the credits statistics

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
    api_instance = explorer_client.AccountsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date of the period (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date of the period (optional)
group_by = 'DAY' # str | Time slot of the requested period (optional) (default to 'DAY')
user_id = 'user_id_example' # str | Used if statistics is wanted for a specific user (optional)

    try:
        # Get Credit Statistics
        api_response = api_instance.get_credit_statistics(start_date=start_date, end_date=end_date, group_by=group_by, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_credit_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| Start date of the period | [optional] 
 **end_date** | **datetime**| End date of the period | [optional] 
 **group_by** | **str**| Time slot of the requested period | [optional] [default to &#39;DAY&#39;]
 **user_id** | **str**| Used if statistics is wanted for a specific user | [optional] 

### Return type

[**CreditStatistics**](CreditStatistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datapoints |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credits**
> UserCredits get_credits()

Get Credits

Get the Explorer credits available for the logged in user. If the user has a manager, the credits available to the manager will be returned

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Get Credits
        api_response = api_instance.get_credits()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_credits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserCredits**](UserCredits.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available explorer credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manager_invitations**
> list[ManagerInvitation] get_manager_invitations()

Get Manager Invitations

Get all manager invitations sent to you. Each invitation is identified by an invitation id which is an integer. To accept or reject invitations, you need their id

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Get Manager Invitations
        api_response = api_instance.get_manager_invitations()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_manager_invitations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ManagerInvitation]**](ManagerInvitation.md)

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

# **get_pending_payment**
> PendingPayment get_pending_payment()

Get Pending Payments

Get the last pending payment for the user. Before any other payments/purchases can be made, this payment must be either completed or ignored.

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Get Pending Payments
        api_response = api_instance.get_pending_payment()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_pending_payment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PendingPayment**](PendingPayment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pending payment for the user, if any |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_plan**
> ProductPlan get_product_plan()

Get Product Plan

Get the Explorer product plan to which the user is currently subscribed, with the associated details

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Get Product Plan
        api_response = api_instance.get_product_plan()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_product_plan: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProductPlan**](ProductPlan.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the current Explorer product plan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage**
> UsageDetails get_usage(start_date=start_date, end_date=end_date)

Get Usage

Retrieves Explorer usage information for the authenticated user, that is, the number of projects started and verbatims used in the given time period.

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
    api_instance = explorer_client.AccountsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | The day starting the period for which the usage should be computed. The format of the date is yyyy-MM-dd. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | The day ending the period. Note that endDate must be after startDate. The format of the date is yyyy-MM-dd, e.g., 2016-09-01. For retrieving the usage for the first of september, 2016, startDate should be 2016-09-01 and endDate should be 2016-09-02. (optional)

    try:
        # Get Usage
        api_response = api_instance.get_usage(start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The day starting the period for which the usage should be computed. The format of the date is yyyy-MM-dd. | [optional] 
 **end_date** | **datetime**| The day ending the period. Note that endDate must be after startDate. The format of the date is yyyy-MM-dd, e.g., 2016-09-01. For retrieving the usage for the first of september, 2016, startDate should be 2016-09-01 and endDate should be 2016-09-02. | [optional] 

### Return type

[**UsageDetails**](UsageDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage information in terms of number of projects started and verbatims analyzed in the time period. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings**
> list[UserSetting] get_user_settings()

Get User Settings

Get all user settings, their current values and a brief description of each of them

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
    api_instance = explorer_client.AccountsApi(api_client)
    
    try:
        # Get User Settings
        api_response = api_instance.get_user_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_user_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserSetting]**](UserSetting.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_credits**
> CreditPurchaseResponse purchase_credits(credit_purchase=credit_purchase)

Purchase Credits

Purchase Explorer credits for the logged in user. If the issuing bank for the user requires verification for the transaction, the response will include a link for the verification. Following successful verification, the transaction will be reprocessed automatically.

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
    api_instance = explorer_client.AccountsApi(api_client)
    credit_purchase = explorer_client.CreditPurchase() # CreditPurchase | The purchase request for credits, specifying the number of credits to purchase (optional)

    try:
        # Purchase Credits
        api_response = api_instance.purchase_credits(credit_purchase=credit_purchase)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->purchase_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_purchase** | [**CreditPurchase**](CreditPurchase.md)| The purchase request for credits, specifying the number of credits to purchase | [optional] 

### Return type

[**CreditPurchaseResponse**](CreditPurchaseResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The outcome of the purchase credit request along with the balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_account**
> AccountReactivationResponse reactivate_account(account_reactivation_request=account_reactivation_request)

Reactivate Account

Reactive the logged in user's account after setting the product plan specified

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
    api_instance = explorer_client.AccountsApi(api_client)
    account_reactivation_request = explorer_client.AccountReactivationRequest() # AccountReactivationRequest | The reactivation request specifying which product plan the user would like to select (optional)

    try:
        # Reactivate Account
        api_response = api_instance.reactivate_account(account_reactivation_request=account_reactivation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->reactivate_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_reactivation_request** | [**AccountReactivationRequest**](AccountReactivationRequest.md)| The reactivation request specifying which product plan the user would like to select | [optional] 

### Return type

[**AccountReactivationResponse**](AccountReactivationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_manager_invitation**
> reject_manager_invitation(id)

Reject Manager Invitation

Reject a manager invitation

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
    api_instance = explorer_client.AccountsApi(api_client)
    id = 56 # int | Id of the invitation

    try:
        # Reject Manager Invitation
        api_instance.reject_manager_invitation(id)
    except ApiException as e:
        print("Exception when calling AccountsApi->reject_manager_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the invitation | 

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

# **set_product_plan**
> ProductChangeResponse set_product_plan(product_plan_update=product_plan_update)

Set Product Plan

Update the Explorer product plan to which the user is subscribed. If the change is an upgrade, the product plan is instantly changed and a prorated amount is charged and prorated credits are added to the account. If the change is a downgrade, a change is scheduled for the start of the next billing cycle

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
    api_instance = explorer_client.AccountsApi(api_client)
    product_plan_update = explorer_client.ProductPlanUpdate() # ProductPlanUpdate | The new product plan handle (optional)

    try:
        # Set Product Plan
        api_response = api_instance.set_product_plan(product_plan_update=product_plan_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->set_product_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_plan_update** | [**ProductPlanUpdate**](ProductPlanUpdate.md)| The new product plan handle | [optional] 

### Return type

[**ProductChangeResponse**](ProductChangeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response for the product change operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_settings**
> list[UserSetting] update_user_settings(user_setting=user_setting)

Update User Settings

Updates user setting. Send a GET to the same url to get all available settings and their possible values.

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
    api_instance = explorer_client.AccountsApi(api_client)
    user_setting = [explorer_client.UserSetting()] # list[UserSetting] | The settings (optional)

    try:
        # Update User Settings
        api_response = api_instance.update_user_settings(user_setting=user_setting)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->update_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_setting** | [**list[UserSetting]**](UserSetting.md)| The settings | [optional] 

### Return type

[**list[UserSetting]**](UserSetting.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

