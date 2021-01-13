# explorer_client.ModelsApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation**](ModelsApi.md#accept_invitation) | **PUT** /models/invitations/{invitationId}/accept | Accept Model Invitations
[**create_model**](ModelsApi.md#create_model) | **POST** /models/create | Create Model
[**get_model**](ModelsApi.md#get_model) | **GET** /models/{id} | Get Model
[**get_model_invitations**](ModelsApi.md#get_model_invitations) | **GET** /models/invitations | Get Model Invitations
[**get_model_projects**](ModelsApi.md#get_model_projects) | **GET** /models/{id}/projects | Get Projects
[**get_model_versions**](ModelsApi.md#get_model_versions) | **GET** /models/{id}/versions | Get Model Versions
[**get_models**](ModelsApi.md#get_models) | **GET** /models | Get Models
[**get_versioned_model**](ModelsApi.md#get_versioned_model) | **GET** /models/{id}/versions/{version} | Get Model Version
[**reject_invitation**](ModelsApi.md#reject_invitation) | **PUT** /models/invitations/{invitationId}/reject | Reject Model Invitations
[**remove_model**](ModelsApi.md#remove_model) | **DELETE** /models/{id} | Delete Model
[**remove_model_access**](ModelsApi.md#remove_model_access) | **DELETE** /models/{id}/userRights/{accessId} | Remove Model Access
[**remove_model_invitation**](ModelsApi.md#remove_model_invitation) | **DELETE** /models/{id}/invitations/{invitationId} | Remove Model Invitation
[**share_model**](ModelsApi.md#share_model) | **POST** /models/{id}/share | Share Model
[**update_model**](ModelsApi.md#update_model) | **PUT** /models/{id} | Update Model
[**upload_model_from_file**](ModelsApi.md#upload_model_from_file) | **POST** /models | Upload Model


# **accept_invitation**
> accept_invitation(invitation_id)

Accept Model Invitations

Accept ModelInvitation which makes the model accessible. The invitation will be removed after a successful accept

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
    api_instance = explorer_client.ModelsApi(api_client)
    invitation_id = 56 # int | The identifier of the invitation

    try:
        # Accept Model Invitations
        api_instance.accept_invitation(invitation_id)
    except ApiException as e:
        print("Exception when calling ModelsApi->accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **int**| The identifier of the invitation | 

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
**200** | A list of invitations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model**
> Model create_model(project_id=project_id, model_update=model_update)

Create Model

Creates a model from a given project. The ModelUpdate field specifies if the project is to be connected with the model (All changes to the model will be reflected in all master and dependent projects after the exploration)

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
    api_instance = explorer_client.ModelsApi(api_client)
    project_id = 56 # int | The identifier of the project to import model from (optional)
model_update = explorer_client.ModelUpdate() # ModelUpdate |  (optional)

    try:
        # Create Model
        api_response = api_instance.create_model(project_id=project_id, model_update=model_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The identifier of the project to import model from | [optional] 
 **model_update** | [**ModelUpdate**](ModelUpdate.md)|  | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The model containing the information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id)

Get Model

Return a Model for the given modelId

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The id of the model to fetch.

    try:
        # Get Model
        api_response = api_instance.get_model(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the model to fetch. | 

### Return type

[**Model**](Model.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of models |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_invitations**
> list[ModelInvitation] get_model_invitations()

Get Model Invitations

Return all ModelInvitation put out to logged in user

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
    api_instance = explorer_client.ModelsApi(api_client)
    
    try:
        # Get Model Invitations
        api_response = api_instance.get_model_invitations()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_model_invitations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ModelInvitation]**](ModelInvitation.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of invitations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_projects**
> ModelProjects get_model_projects(id)

Get Projects

Return the projects which are connected and dependent to a model. The response fields will be empty if the model is not a dynamic model

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The id of the Model for which the information is required

    try:
        # Get Projects
        api_response = api_instance.get_model_projects(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_model_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Model for which the information is required | 

### Return type

[**ModelProjects**](ModelProjects.md)

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

# **get_model_versions**
> list[ModelVersion] get_model_versions(id)

Get Model Versions

Return all versions of a model that are available for a specified model. The versioning applies only to the groups and the ignore terms of a model.

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The id of the model

    try:
        # Get Model Versions
        api_response = api_instance.get_model_versions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_model_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the model | 

### Return type

[**list[ModelVersion]**](ModelVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of ModelVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> list[ModelInfo] get_models()

Get Models

For an authenticated user, this method returns all ModelInfo accessible by that user. ModelInfo refers to a version of a Model containing meta-information, but not the full Model details).

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
    api_instance = explorer_client.ModelsApi(api_client)
    
    try:
        # Get Models
        api_response = api_instance.get_models()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ModelInfo]**](ModelInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of models |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versioned_model**
> Model get_versioned_model(id, version)

Get Model Version

Returns a specific version of a {@link Model} for the given modelId and version. The versioning applies only to the groups and the ignore terms of a model

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The id of the model to fetch
version = 56 # int | The version of the model to fetch

    try:
        # Get Model Version
        api_response = api_instance.get_versioned_model(id, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_versioned_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the model to fetch | 
 **version** | **int**| The version of the model to fetch | 

### Return type

[**Model**](Model.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A version of a model. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_invitation**
> reject_invitation(invitation_id)

Reject Model Invitations

Reject ModelInvitation which will remove the invitation.

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
    api_instance = explorer_client.ModelsApi(api_client)
    invitation_id = 56 # int | The identifier of the invitation

    try:
        # Reject Model Invitations
        api_instance.reject_invitation(invitation_id)
    except ApiException as e:
        print("Exception when calling ModelsApi->reject_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **int**| The identifier of the invitation | 

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
**200** | A list of invitations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_model**
> remove_model(id)

Delete Model

Removes the model. If the model is a dynamic model, all dependent projects will be detached from the model.

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The identifier for the model to remove

    try:
        # Delete Model
        api_instance.remove_model(id)
    except ApiException as e:
        print("Exception when calling ModelsApi->remove_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the model to remove | 

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
**200** | Model containing the updated information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_model_access**
> remove_model_access(id, access_id)

Remove Model Access

Removes an access permission for this model. Removing the access permission means that the respective user no longer will have access to this model. The accessId can be found by sending a GET to /models/{id}.

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The identifier for the model
access_id = 56 # int | The identifier for the ModelAccess

    try:
        # Remove Model Access
        api_instance.remove_model_access(id, access_id)
    except ApiException as e:
        print("Exception when calling ModelsApi->remove_model_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the model | 
 **access_id** | **int**| The identifier for the ModelAccess | 

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

# **remove_model_invitation**
> remove_model_invitation(id, invitation_id)

Remove Model Invitation

Removes a model invitation sent to another user. Removing the invitation means that the user no longer will be able to accept/reject the invitation.

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The identifier for the model
invitation_id = 56 # int | The identifier for the invitation

    try:
        # Remove Model Invitation
        api_instance.remove_model_invitation(id, invitation_id)
    except ApiException as e:
        print("Exception when calling ModelsApi->remove_model_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the model | 
 **invitation_id** | **int**| The identifier for the invitation | 

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

# **share_model**
> ModelInvitation share_model(id, user_id=user_id)

Share Model

Create a ModelInvitation to share a model with a different user. When the user accepts the invitation the Model will be available to the user.

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The identifier of the model.
user_id = 'user_id_example' # str | The userId of the user you want to share the model with (optional)

    try:
        # Share Model
        api_response = api_instance.share_model(id, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->share_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the model. | 
 **user_id** | **str**| The userId of the user you want to share the model with | [optional] 

### Return type

[**ModelInvitation**](ModelInvitation.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ModelInvitation containing the information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> Model update_model(id, model_input=model_input)

Update Model

Updates the {@link Model} information for the model identified by the id parameter. The model structure (groups and ignore terms) and the model name by updated. Each update of the model structure will result in a new version of the model being created. If the model is a dynamic model, the master project and dependent projects will reflect the change after the next explore.

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
    api_instance = explorer_client.ModelsApi(api_client)
    id = 56 # int | The identifier of the model
model_input = explorer_client.ModelInput() # ModelInput | The ModelInput with which to update the model. (optional)

    try:
        # Update Model
        api_response = api_instance.update_model(id, model_input=model_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the model | 
 **model_input** | [**ModelInput**](ModelInput.md)| The ModelInput with which to update the model. | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Model containing the updated information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_model_from_file**
> Model upload_model_from_file(file, file_name, encoding=encoding, title=title)

Upload Model

Upload a model from a file (\".csv\" , \".xls\" , \".xlsx\" supported). 3 columns need to be present in the file, namely: \"Index\", \"Label\" and \"Terms\". Index is used as group indicator. Index Label Terms 1 Burger burger, cheeseburger, veggie burger 2 Fries fries, chips, the chips 3.1 Nice nice, good 3.2 Sweet sweet, 4 Soda soda, drinks \"Label\" is the name of each topic and finally \"Terms\" is a comma separated list of terms that should be included in the topic. An optional \"Pinned\" column can be present. The value should be \"true\" or \"false\".The multipart form data parts need to be 'file' with the binary data and 'fileName' with the file name as plain text

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
    api_instance = explorer_client.ModelsApi(api_client)
    file = '/path/to/file' # file | input file
file_name = 'file_name_example' # str | 
encoding = 'encoding_example' # str | Encoding of the input file. If this is left blank a 'best guess' will be made (optional)
title = 'title_example' # str | The title of the model. If this parameter is omitted the model will be initialized with a null title. (optional)

    try:
        # Upload Model
        api_response = api_instance.upload_model_from_file(file, file_name, encoding=encoding, title=title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->upload_model_from_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| input file | 
 **file_name** | **str**|  | 
 **encoding** | **str**| Encoding of the input file. If this is left blank a &#39;best guess&#39; will be made | [optional] 
 **title** | **str**| The title of the model. If this parameter is omitted the model will be initialized with a null title. | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

