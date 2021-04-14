# explorer_client.ModelsApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_model_versions**](ModelsApi.md#compare_model_versions) | **GET** /models/{id}/versions/{version}/compare/{comparingVersion} | Compare Model versions
[**create_model**](ModelsApi.md#create_model) | **POST** /models/create | Create Model
[**create_model_access**](ModelsApi.md#create_model_access) | **POST** /models/{id}/usersAccess | Control Model Access
[**delete_model_access**](ModelsApi.md#delete_model_access) | **DELETE** /models/{id}/usersAccess/{accessId} | Remove Model Access
[**get_model**](ModelsApi.md#get_model) | **GET** /models/{id} | Get Model
[**get_model_translation_candidates**](ModelsApi.md#get_model_translation_candidates) | **GET** /models/{id}/{language}/translationCandidates | Get translation candidates
[**get_model_versions**](ModelsApi.md#get_model_versions) | **GET** /models/{id}/versions | Get Model Versions
[**get_models**](ModelsApi.md#get_models) | **GET** /models | Get Models
[**get_versioned_model**](ModelsApi.md#get_versioned_model) | **GET** /models/{id}/versions/{version} | Get Model Version
[**remove_model**](ModelsApi.md#remove_model) | **DELETE** /models/{id} | Delete Model
[**update_model**](ModelsApi.md#update_model) | **PUT** /models/{id} | Update Model
[**update_model_version**](ModelsApi.md#update_model_version) | **PUT** /models/{id}/versions/{version} | Update version
[**upload_model_from_file**](ModelsApi.md#upload_model_from_file) | **POST** /models | Upload Model


# **compare_model_versions**
> ModelChangeSet compare_model_versions(id, version, comparing_version)

Compare Model versions

Get the comparison between 2 model versions

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
version = 56 # int | The model version
comparing_version = 56 # int | The model version to compare with

    try:
        # Compare Model versions
        api_response = api_instance.compare_model_versions(id, version, comparing_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->compare_model_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the model | 
 **version** | **int**| The model version | 
 **comparing_version** | **int**| The model version to compare with | 

### Return type

[**ModelChangeSet**](ModelChangeSet.md)

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

# **create_model**
> Model create_model(model_update, project_id=project_id)

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
    model_update = explorer_client.ModelUpdate() # ModelUpdate | The modelUpdate with which to create the model.
project_id = 56 # int | The identifier of the project to import model from (optional)

    try:
        # Create Model
        api_response = api_instance.create_model(model_update, project_id=project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_update** | [**ModelUpdate**](ModelUpdate.md)| The modelUpdate with which to create the model. | 
 **project_id** | **int**| The identifier of the project to import model from | [optional] 

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

# **create_model_access**
> ModelAccess create_model_access(id, user_id)

Control Model Access

Gives a user access to the model

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
user_id = 'user_id_example' # str | The userId of the user you want to share the model with

    try:
        # Control Model Access
        api_response = api_instance.create_model_access(id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->create_model_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the model | 
 **user_id** | **str**| The userId of the user you want to share the model with | 

### Return type

[**ModelAccess**](ModelAccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created ModelAccess containing the information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_access**
> delete_model_access(id, access_id)

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
        api_instance.delete_model_access(id, access_id)
    except ApiException as e:
        print("Exception when calling ModelsApi->delete_model_access: %s\n" % e)
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

# **get_model_translation_candidates**
> ModelTranslationCandidates get_model_translation_candidates(id, language)

Get translation candidates

Get the list of projects that are receiving updates from the model, from which the translations can be re-used.

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
language = 'language_example' # str | The language for which translation candidates should be retrieved

    try:
        # Get translation candidates
        api_response = api_instance.get_model_translation_candidates(id, language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_model_translation_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the model | 
 **language** | **str**| The language for which translation candidates should be retrieved | 

### Return type

[**ModelTranslationCandidates**](ModelTranslationCandidates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The translation candidates for model, in the specified language. |  -  |

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

# **remove_model**
> remove_model(id)

Delete Model

Removes the model. All projects receiving updates from the model will no longer do so. If you are not the owner of the model, only your access will be impacted.

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

# **update_model**
> Model update_model(id, model_input)

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
model_input = explorer_client.ModelInput() # ModelInput | The ModelInput with which to update the model.

    try:
        # Update Model
        api_response = api_instance.update_model(id, model_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the model | 
 **model_input** | [**ModelInput**](ModelInput.md)| The ModelInput with which to update the model. | 

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

# **update_model_version**
> ModelVersion update_model_version(id, version, model_version_update)

Update version

Update a model version

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
version = 56 # int | The model version
model_version_update = explorer_client.ModelVersionUpdate() # ModelVersionUpdate | The update request

    try:
        # Update version
        api_response = api_instance.update_model_version(id, version, model_version_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->update_model_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the model | 
 **version** | **int**| The model version | 
 **model_version_update** | [**ModelVersionUpdate**](ModelVersionUpdate.md)| The update request | 

### Return type

[**ModelVersion**](ModelVersion.md)

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

