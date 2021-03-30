# explorer_client.ProjectsApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_folder_to_folder**](ProjectsApi.md#add_folder_to_folder) | **PUT** /projects/folders/{id}/folders/{subFolderId} | Add sub folder to folder
[**add_project_to_folder**](ProjectsApi.md#add_project_to_folder) | **PUT** /projects/folders/{id}/projects/{projectId} | Add project to folder
[**append_to_project**](ProjectsApi.md#append_to_project) | **POST** /projects/{id}/append | Add data to project
[**append_file_to_project**](ProjectsApi.md#append_file_to_project) | **POST** /projects/{id}/append | Add data to project
[**apply_model**](ProjectsApi.md#apply_model) | **PUT** /projects/{id}/apply | Apply model to project
[**compare_project_versions**](ProjectsApi.md#compare_project_versions) | **GET** /projects/{id}/versions/{version}/compare/{comparingVersion} | Compare project versions
[**create_batch**](ProjectsApi.md#create_batch) | **POST** /projects/{id}/batches | Start Batch Calculation
[**create_folder**](ProjectsApi.md#create_folder) | **POST** /projects/folders | Create folder
[**create_report**](ProjectsApi.md#create_report) | **POST** /projects/{id}/reports | Create report
[**create_stories**](ProjectsApi.md#create_stories) | **POST** /projects/{id}/stories | Create Stories
[**explore_project**](ProjectsApi.md#explore_project) | **POST** /projects/{id}/explore | Explore project
[**find_suggestions**](ProjectsApi.md#find_suggestions) | **POST** /projects/{id}/suggestions | Get suggestions for terms
[**get_batch_result**](ProjectsApi.md#get_batch_result) | **GET** /projects/{id}/batches/{batchId} | Get Batch Calculation
[**get_cell_information**](ProjectsApi.md#get_cell_information) | **GET** /projects/{id}/result/cells | Get cell data
[**get_coverage_tonalities**](ProjectsApi.md#get_coverage_tonalities) | **GET** /projects/{id}/explore/coverageStatistics/tonalities | Get Coverage Tonalities
[**get_distinct_column_values**](ProjectsApi.md#get_distinct_column_values) | **GET** /projects/{id}/columns/{columnHeaderId} | Get distinct column values
[**get_exploration**](ProjectsApi.md#get_exploration) | **GET** /projects/{id}/explore | Get Explore Results
[**get_folder**](ProjectsApi.md#get_folder) | **GET** /projects/folders/{id} | Get folder
[**get_folders**](ProjectsApi.md#get_folders) | **GET** /projects/folders | Get folders
[**get_group_tonalities**](ProjectsApi.md#get_group_tonalities) | **GET** /projects/{id}/explore/groups/{groupId}/tonalities | Get tonality response
[**get_headers**](ProjectsApi.md#get_headers) | **GET** /projects/{id}/headers | Get project headers
[**get_matching_sentences_for_terms**](ProjectsApi.md#get_matching_sentences_for_terms) | **GET** /projects/{id}/sentences | Get sentences
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{id} | Get project
[**get_project_document_tonalities**](ProjectsApi.md#get_project_document_tonalities) | **GET** /projects/{id}/explore/projectTonalities/tonalities | Get Document Tonalities
[**get_project_languages**](ProjectsApi.md#get_project_languages) | **GET** /projects/{id}/languages | Get project languages
[**get_project_report**](ProjectsApi.md#get_project_report) | **GET** /projects/{id}/reports/{reportId} | Retrieve report
[**get_project_reports**](ProjectsApi.md#get_project_reports) | **GET** /projects/{id}/reports | Get reports
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Get all projects
[**get_sample_texts**](ProjectsApi.md#get_sample_texts) | **GET** /projects/{projectId}/headers/{columnHeaderId}/samples | Get sample texts
[**get_stories**](ProjectsApi.md#get_stories) | **GET** /projects/{id}/stories | Get Stories
[**get_supported_languages**](ProjectsApi.md#get_supported_languages) | **GET** /projects/languages | Get all supported languages
[**get_term_details**](ProjectsApi.md#get_term_details) | **GET** /projects/{id}/details | Get topic details
[**get_topic_tonalities**](ProjectsApi.md#get_topic_tonalities) | **GET** /projects/{id}/explore/groups/{groupId}/topics/{topicId}/tonalities | Get tonality response
[**get_versions**](ProjectsApi.md#get_versions) | **GET** /projects/{id}/versions | Get project versions
[**publish_version**](ProjectsApi.md#publish_version) | **PUT** /projects/{id}/versions/{version}/publish | Publish project version to model
[**remove_folder**](ProjectsApi.md#remove_folder) | **DELETE** /projects/folders/{id} | Remove folder
[**remove_folder_from_folder**](ProjectsApi.md#remove_folder_from_folder) | **DELETE** /projects/folders/{id}/folders/{subFolderId} | Remove sub folder from folder
[**remove_history**](ProjectsApi.md#remove_history) | **DELETE** /projects/{id}/history/{historyId} | Remove history log
[**remove_model_from_project**](ProjectsApi.md#remove_model_from_project) | **DELETE** /projects/{id}/model | Detach model from project
[**remove_project**](ProjectsApi.md#remove_project) | **DELETE** /projects/{id} | Remove project
[**remove_project_from_folder**](ProjectsApi.md#remove_project_from_folder) | **DELETE** /projects/folders/{id}/projects/{projectId} | Remove project from folder
[**remove_report**](ProjectsApi.md#remove_report) | **DELETE** /projects/{id}/reports/{reportId} | Remove report
[**revert_to_version**](ProjectsApi.md#revert_to_version) | **PUT** /projects/{id}/versions/{version}/revert | Revert to version
[**search_for_project_terms**](ProjectsApi.md#search_for_project_terms) | **GET** /projects/{id}/result/searchTerms | Search Project Terms
[**start_coverage_tonalities**](ProjectsApi.md#start_coverage_tonalities) | **POST** /projects/{id}/explore/coverageStatistics/tonalities | Start Coverage Tonalities Calculation
[**start_group_tonalities**](ProjectsApi.md#start_group_tonalities) | **POST** /projects/{id}/explore/groups/{groupId}/tonalities | Start tonality calculation
[**start_project_document_tonalities**](ProjectsApi.md#start_project_document_tonalities) | **POST** /projects/{id}/explore/projectTonalities/tonalities | Start Document Tonalities
[**start_topic_tonalities**](ProjectsApi.md#start_topic_tonalities) | **POST** /projects/{id}/explore/groups/{groupId}/topics/{topicId}/tonalities | Start tonality calculation
[**stop_subscribing_to_updates**](ProjectsApi.md#stop_subscribing_to_updates) | **DELETE** /projects/{id}/subscription | Stop subscribing to updates from a model
[**update_folder**](ProjectsApi.md#update_folder) | **PUT** /projects/folders/{folderId} | Update folder
[**update_header**](ProjectsApi.md#update_header) | **PUT** /projects/{id}/headers/{headerId} | Update project header
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{id} | Update project
[**update_project_model**](ProjectsApi.md#update_project_model) | **PUT** /projects/{id}/model | Update Project Model
[**update_version**](ProjectsApi.md#update_version) | **PUT** /projects/{id}/versions/{version} | Update version
[**upload_project**](ProjectsApi.md#upload_project) | **POST** /projects | Create project
[**upload_project_file**](ProjectsApi.md#upload_project_file) | **POST** /projects | Create project
[**validate_filter_date_format**](ProjectsApi.md#validate_filter_date_format) | **GET** /projects/{projectId}/headers/{columnHeaderId}/validateFilterFormat | Validate your data filter format


# **add_folder_to_folder**
> FolderInformation add_folder_to_folder(id, sub_folder_id)

Add sub folder to folder

Adds a sub folder to a folder.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the folder
sub_folder_id = 56 # int | The id of the sub folder which we will move

    try:
        # Add sub folder to folder
        api_response = api_instance.add_folder_to_folder(id, sub_folder_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->add_folder_to_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the folder | 
 **sub_folder_id** | **int**| The id of the sub folder which we will move | 

### Return type

[**FolderInformation**](FolderInformation.md)

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

# **add_project_to_folder**
> FolderInformation add_project_to_folder(id, project_id)

Add project to folder

Adds a project to a folder

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the folder
project_id = 56 # int | The id of the project

    try:
        # Add project to folder
        api_response = api_instance.add_project_to_folder(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->add_project_to_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the folder | 
 **project_id** | **int**| The id of the project | 

### Return type

[**FolderInformation**](FolderInformation.md)

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
# **append_to_project**
> ProjectId append_to_project(id, rows_data, encoding=encoding, message=message)

Add data to project

For an authenticated user, this method will upload data and append it to an existing project. When the data has been uploaded the ProjectStatus changes to ProjectStatus.APPENDING. You may query the project until it changes state to ProjectStatus#EXPLORABLE. The file to append should contain the same number of columns as the previously uploaded files to   the project, but (unlike initial files) no header row. (send a GET to /projects/{id}) until it changes status to EXPLORABLE}. 

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The numerical id of the project to append to.
rows_data = explorer_client.RowsData() # rows_data | the rows to append
encoding = 'encoding_example' # str | Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. (optional)
message = 'message_example' # str | The message that will be added to the log history. (optional)

    try:
        # Add data to project
        api_response = api_instance.append_to_project(id, rows_data, encoding=encoding, message=message)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->append_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numerical id of the project to append to. | 
 **rows_data** |  [**RowsData**](RowsData.md)| the rows of the project  | 
 **encoding** | **str**| Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. | [optional] 
 **message** | **str**| The message that will be added to the log history. | [optional] 

### Return type

[**ProjectId**](ProjectId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_file_to_project**
> ProjectId append_file_to_project(id, file, file_name, encoding=encoding, message=message)

Add data to project

For an authenticated user, this method will upload data and append it to an existing   project. When the data has been uploaded the ProjectStatus changes to ProjectStatus.APPENDING. You may query the project until it changes state to ProjectStatus#EXPLORABLE. The file to append should contain the same number of columns as the previously uploaded files to   the project, but (unlike initial files) no header row. (send a GET to /projects/{id}) until it changes status to EXPLORABLE}. In the case of multipart form data the parts need to be 'file' with the binary data and 'fileName' with the file name as plain text

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The numerical id of the project to append to.
file = '/path/to/file' # file | input file
file_name = 'file_name_example' # str | 
encoding = 'encoding_example' # str | Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. (optional)
message = 'message_example' # str | The message that will be added to the log history. (optional)

    try:
        # Add data to project
        api_response = api_instance.append_file_to_project(id, file, file_name, encoding=encoding, message=message)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->append_file_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numerical id of the project to append to. | 
 **file** | **file**| input file | 
 **file_name** | **str**|  | 
 **encoding** | **str**| Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. | [optional] 
 **message** | **str**| The message that will be added to the log history. | [optional] 

### Return type

[**ProjectId**](ProjectId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **apply_model**
> apply_model(id, apply_model_request)

Apply model to project

Apply a model to project. The model has to be created by the logged in user or share with the logged in user. If the model is applied to a project with different language the system will automatically translate the model.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
apply_model_request = explorer_client.ApplyModelRequest() # ApplyModelRequest | The request body

    try:
        # Apply model to project
        api_instance.apply_model(id, apply_model_request)
    except ApiException as e:
        print("Exception when calling ProjectsApi->apply_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **apply_model_request** | [**ApplyModelRequest**](ApplyModelRequest.md)| The request body | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compare_project_versions**
> ProjectVersionsChangeSet compare_project_versions(id, version, comparing_version)

Compare project versions

Get the comparison between 2 project versions

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
version = 56 # int | The project version
comparing_version = 56 # int | The project version to compare with

    try:
        # Compare project versions
        api_response = api_instance.compare_project_versions(id, version, comparing_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->compare_project_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **version** | **int**| The project version | 
 **comparing_version** | **int**| The project version to compare with | 

### Return type

[**ProjectVersionsChangeSet**](ProjectVersionsChangeSet.md)

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

# **create_batch**
> BatchId create_batch(id, batch_request)

Start Batch Calculation

This method starts a process where all texts in the request will be matched against all topics in the project. The request can also specify if a tonality calculation should be made. <br/>Maximum number of texts in one batch is 100 and each text can not have more than 32767 characters. One credit per text will deducted from the users account

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
batch_request = explorer_client.BatchRequest() # BatchRequest | The batch request

    try:
        # Start Batch Calculation
        api_response = api_instance.create_batch(id, batch_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **batch_request** | [**BatchRequest**](BatchRequest.md)| The batch request | 

### Return type

[**BatchId**](BatchId.md)

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

# **create_folder**
> FolderInformation create_folder(folder_request)

Create folder

Creates a folder in user's account

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
    api_instance = explorer_client.ProjectsApi(api_client)
    folder_request = explorer_client.FolderRequest() # FolderRequest | The request

    try:
        # Create folder
        api_response = api_instance.create_folder(folder_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_request** | [**FolderRequest**](FolderRequest.md)| The request | 

### Return type

[**FolderInformation**](FolderInformation.md)

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

# **create_report**
> ProjectReport create_report(id, type, pole_id=pole_id, pole_ids=pole_ids, keywords=keywords, topic_ids=topic_ids, sort_alphabetically=sort_alphabetically)

Create report

Begins to generates a report of the current contents in the project. Note that although this is a POST request, the parameters are passed through the URL. To check the progress of the requested report, call a GET request on /projects/{id}/reports and refer to the corresponding report id.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The identifier for the project
type = 'PDF' # str | The type of report to generate, for example 'EXCEL' or 'PDF'. (default to 'PDF')
pole_id = 0 # int | The id of the pole or concept to filter texts by (if desired). Corresponds to target concept in the GUI. (optional) (default to 0)
pole_ids = [56] # list[int] | The ids of the poles (soon concepts) to analyse for strength in the texts. (optional)
keywords = True # bool | Boolean to control if keywords columns will be created. (optional) (default to True)
topic_ids = [56] # list[int] | ids of topics that you want to get the sentiment scores for them for each individual text. When you specify a topicId here, each text in your project will be analyzed with respect to the sentiments around that topic, and columns for the combination of the topic and each sentiment will be added to the resulting report. To find out the topic ids for the project, call GET on /projects/{id}/explore, to see the current ProjectExplorationResponse. (optional)
sort_alphabetically = False # bool | Turn on alphabetically sorted topics. (optional) (default to False)

    try:
        # Create report
        api_response = api_instance.create_report(id, type, pole_id=pole_id, pole_ids=pole_ids, keywords=keywords, topic_ids=topic_ids, sort_alphabetically=sort_alphabetically)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the project | 
 **type** | **str**| The type of report to generate, for example &#39;EXCEL&#39; or &#39;PDF&#39;. | [default to &#39;PDF&#39;]
 **pole_id** | **int**| The id of the pole or concept to filter texts by (if desired). Corresponds to target concept in the GUI. | [optional] [default to 0]
 **pole_ids** | [**list[int]**](int.md)| The ids of the poles (soon concepts) to analyse for strength in the texts. | [optional] 
 **keywords** | **bool**| Boolean to control if keywords columns will be created. | [optional] [default to True]
 **topic_ids** | [**list[int]**](int.md)| ids of topics that you want to get the sentiment scores for them for each individual text. When you specify a topicId here, each text in your project will be analyzed with respect to the sentiments around that topic, and columns for the combination of the topic and each sentiment will be added to the resulting report. To find out the topic ids for the project, call GET on /projects/{id}/explore, to see the current ProjectExplorationResponse. | [optional] 
 **sort_alphabetically** | **bool**| Turn on alphabetically sorted topics. | [optional] [default to False]

### Return type

[**ProjectReport**](ProjectReport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stories**
> create_stories(id, stories_request)

Create Stories

Creates stories for the given title and url column. The project needs to be explored before you can call this method. If you have created stories it will appear as a column in the report.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
stories_request = explorer_client.StoriesRequest() # StoriesRequest | The request containing the required data for the stories generation

    try:
        # Create Stories
        api_instance.create_stories(id, stories_request)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **stories_request** | [**StoriesRequest**](StoriesRequest.md)| The request containing the required data for the stories generation | 

### Return type

void (empty response body)

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

# **explore_project**
> explore_project(id, project_exploration_context)

Explore project

Starts an exploration of the project. This is only possible if the project has the  ProjectStatus.EXPLORABLE status. This call will return instantly after starting the explore process (with HTTP status 204  since there will be no content). You should supply a ProjectExplorationContext giving the specifics of the exploration. Use the same call but with GET to get a status for the explore process.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project to explore
project_exploration_context = explorer_client.ProjectExplorationContext() # ProjectExplorationContext | The exploration context to use

    try:
        # Explore project
        api_instance.explore_project(id, project_exploration_context)
    except ApiException as e:
        print("Exception when calling ProjectsApi->explore_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project to explore | 
 **project_exploration_context** | [**ProjectExplorationContext**](ProjectExplorationContext.md)| The exploration context to use | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_suggestions**
> SuggestionsResult find_suggestions(id, suggestions_request)

Get suggestions for terms

Get suggestions for topics terms. This endpoint retrieves semantically similar words from the Gavagai Lexicon for each term in the request body. These words are filtered so that suggestions returned are only those that are present in the project text data. The response body contains much more detailed information than that which is presented in the GUI, such as a neighbourCounter (how many terms in the request a suggestion is relevant for) and whether the suggestion displays string similarity with any request term.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The identifier of the project
suggestions_request = explorer_client.SuggestionsRequest() # SuggestionsRequest | The request containing relevant terms

    try:
        # Get suggestions for terms
        api_response = api_instance.find_suggestions(id, suggestions_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->find_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the project | 
 **suggestions_request** | [**SuggestionsRequest**](SuggestionsRequest.md)| The request containing relevant terms | 

### Return type

[**SuggestionsResult**](SuggestionsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project containing the updated information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_result**
> BatchResponse get_batch_result(id, batch_id)

Get Batch Calculation

Get the results of the batch calculation process. Once the results are available and retrieved successfully the result will be deleted.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
batch_id = 'batch_id_example' # str | The id of the created batch request

    try:
        # Get Batch Calculation
        api_response = api_instance.get_batch_result(id, batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_batch_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **batch_id** | **str**| The id of the created batch request | 

### Return type

[**BatchResponse**](BatchResponse.md)

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

# **get_cell_information**
> CellTopicInformation get_cell_information(id, header_ids=header_ids, first_result=first_result, page_size=page_size, calculate_tonality=calculate_tonality)

Get cell data

Return a CellTopicInformation for the given range which includes the matching topics, sentiment scores and metadata information for the corresponding texts.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The numerical id of the project
header_ids = [56] # list[int] | The ids of the columns that you would like to receive as extra data with every row (optional)
first_result = 0 # int | Where to start reading cells. Defaults to 0, which means the first pageSize number of cells (optional) (default to 0)
page_size = 100 # int | The number of cells to return. Defaults to 100, max 1000 (optional) (default to 100)
calculate_tonality = False # bool | Boolean value indicating if tonality should be calculated (optional) (default to False)

    try:
        # Get cell data
        api_response = api_instance.get_cell_information(id, header_ids=header_ids, first_result=first_result, page_size=page_size, calculate_tonality=calculate_tonality)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_cell_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numerical id of the project | 
 **header_ids** | [**list[int]**](int.md)| The ids of the columns that you would like to receive as extra data with every row | [optional] 
 **first_result** | **int**| Where to start reading cells. Defaults to 0, which means the first pageSize number of cells | [optional] [default to 0]
 **page_size** | **int**| The number of cells to return. Defaults to 100, max 1000 | [optional] [default to 100]
 **calculate_tonality** | **bool**| Boolean value indicating if tonality should be calculated | [optional] [default to False]

### Return type

[**CellTopicInformation**](CellTopicInformation.md)

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

# **get_coverage_tonalities**
> TonalitiesResponse get_coverage_tonalities(id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality)

Get Coverage Tonalities

Get tonalities for documents not covered by existing topic structure. Includes tonality scores broken down for each unclassified document and an aggregated score for all such documents. This call is asynchronous: the information must first be requested through a POST call to the same endpoint (see below).

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
first_result = 0 # int | An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. Note that this is a paginated API, controlled using the firstResult and pageSize parameters. (optional) (default to 0)
page_size = 15 # int | The number of examples to return. Defaults to 15. (optional) (default to 15)
filter_by_tonality = False # bool | Filter by tonality (optional) (default to False)

    try:
        # Get Coverage Tonalities
        api_response = api_instance.get_coverage_tonalities(id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_coverage_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **first_result** | **int**| An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. Note that this is a paginated API, controlled using the firstResult and pageSize parameters. | [optional] [default to 0]
 **page_size** | **int**| The number of examples to return. Defaults to 15. | [optional] [default to 15]
 **filter_by_tonality** | **bool**| Filter by tonality | [optional] [default to False]

### Return type

[**TonalitiesResponse**](TonalitiesResponse.md)

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

# **get_distinct_column_values**
> list[str] get_distinct_column_values(id, column_header_id)

Get distinct column values

When you want to create a filter you need to know the different existing values in the filter column. This method retrieves the distinct values of a given column in a given project. You may wish to check if the column is actually filterable by looking at the information given in the project. If you try this method on a non-filterable column you will get an error. Once you have at least two values you can create filters with one or more of them and other columns as well. Example: if the 'filterable' column contains many rows of 'male' or 'female' or 'unspecified', this call will return the set of three possible filter values 'male', 'female', and 'unspecified'.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The identifier for the project from which to retrieve the column values
column_header_id = 56 # int | The header identifier for the column for which to retrieve the distinct values

    try:
        # Get distinct column values
        api_response = api_instance.get_distinct_column_values(id, column_header_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_distinct_column_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the project from which to retrieve the column values | 
 **column_header_id** | **int**| The header identifier for the column for which to retrieve the distinct values | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set containing all values available in the given column. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exploration**
> ProjectExplorationResponse get_exploration(id, retry=retry)

Get Explore Results

Retrieves the result of a project exploration if it is ready, and the status of the project exploration while it is ongoing.  <p></p>Use this method for polling the status of a recently started exploration (see POST  documentation for the same endpoint). When the status indicates that the exploration has been  completed use the same method to retrieve the result. The possible states are in  ExplorationState. The exploration starts in the ExplorationState.STARTED state and finishes in  ExplorationState.FINISHED.You may get the state ExplorationState.TIMEOUT if the process did not finish within the permitted time range (because the project contains  too much data). If there was a problem and the state is ExplorationState.ERROR you can check the status message for the reason.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project to explore
retry = False # bool | Tf current status is TIMEOUT or ERROR, setting retry to true means that a new explore session is beeing started with the latest context (optional) (default to False)

    try:
        # Get Explore Results
        api_response = api_instance.get_exploration(id, retry=retry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_exploration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project to explore | 
 **retry** | **bool**| Tf current status is TIMEOUT or ERROR, setting retry to true means that a new explore session is beeing started with the latest context | [optional] [default to False]

### Return type

[**ProjectExplorationResponse**](ProjectExplorationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the current status of an ongoing exploration, or the result of a completed exploration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FolderInformation get_folder(id)

Get folder

Gets the content of the given folder

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the folder

    try:
        # Get folder
        api_response = api_instance.get_folder(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the folder | 

### Return type

[**FolderInformation**](FolderInformation.md)

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

# **get_folders**
> FolderStructure get_folders()

Get folders

Get a user's folders and projects

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
    api_instance = explorer_client.ProjectsApi(api_client)
    
    try:
        # Get folders
        api_response = api_instance.get_folders()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_folders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FolderStructure**](FolderStructure.md)

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

# **get_group_tonalities**
> TonalitiesResponse get_group_tonalities(id, group_id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality, meta_data_columns=meta_data_columns)

Get tonality response

Get result of a group tonality calculation

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier
group_id = 56 # int | The group identifier.
first_result = 0 # int | An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. (optional) (default to 0)
page_size = 15 # int | The number of examples to return. Defaults to 15. (optional) (default to 15)
filter_by_tonality = False # bool | Filter the sentences by only keeping sentences that has a score above 0 for the given tonality. (optional) (default to False)
meta_data_columns = 'meta_data_columns_example' # str | Comma separated array of column header id:s which row data will be returned. (optional)

    try:
        # Get tonality response
        api_response = api_instance.get_group_tonalities(id, group_id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality, meta_data_columns=meta_data_columns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_group_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **group_id** | **int**| The group identifier. | 
 **first_result** | **int**| An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. | [optional] [default to 0]
 **page_size** | **int**| The number of examples to return. Defaults to 15. | [optional] [default to 15]
 **filter_by_tonality** | **bool**| Filter the sentences by only keeping sentences that has a score above 0 for the given tonality. | [optional] [default to False]
 **meta_data_columns** | **str**| Comma separated array of column header id:s which row data will be returned. | [optional] 

### Return type

[**TonalitiesResponse**](TonalitiesResponse.md)

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

# **get_headers**
> list[ColumnHeader] get_headers(id)

Get project headers

Get headers of the project

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project

    try:
        # Get project headers
        api_response = api_instance.get_headers(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_headers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 

### Return type

[**list[ColumnHeader]**](ColumnHeader.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of headers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matching_sentences_for_terms**
> Sentences get_matching_sentences_for_terms(id, terms, max_sentences=max_sentences)

Get sentences

Get sentences matching any of the specified terms. The project must be explored prior to making this request

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
terms = ['terms_example'] # list[str] | The terms for which sentences must be retrieved
max_sentences = 10 # int | The maximum number of sentences to include (maximum 20). The actual number will be equal or less to the number specified (optional) (default to 10)

    try:
        # Get sentences
        api_response = api_instance.get_matching_sentences_for_terms(id, terms, max_sentences=max_sentences)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_matching_sentences_for_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **terms** | [**list[str]**](str.md)| The terms for which sentences must be retrieved | 
 **max_sentences** | **int**| The maximum number of sentences to include (maximum 20). The actual number will be equal or less to the number specified | [optional] [default to 10]

### Return type

[**Sentences**](Sentences.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sentences matching any of the topic terms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(id)

Get project

Return a {@link com.gavagai.ethersource.api.explorer.marshal.project.Project} for the given projectId. This includes information like project's status, settings, number of rows, time of creation, column headers, history of uploads, etc.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The numerical id of the project

    try:
        # Get project
        api_response = api_instance.get_project(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numerical id of the project | 

### Return type

[**Project**](Project.md)

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

# **get_project_document_tonalities**
> TonalitiesResponse get_project_document_tonalities(id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality)

Get Document Tonalities

Returns document tonalities information. The calculation works asynchronously and must first be set in motion by calling a POST method on this same endpoint (documented below). Meta-information about the status of the calculation and a percentage progress is also included. If the calculation has not been started, the status will be NOT_STARTED. Note that this is a paginated API, controlled using the firstResult and pageSize parameters.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
first_result = 0 # int | An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. (optional) (default to 0)
page_size = 15 # int | The number of examples to return (optional) (default to 15)
filter_by_tonality = False # bool | Filter the sentences by only keeping sentences that has a score above 0 for the given tonality (optional) (default to False)

    try:
        # Get Document Tonalities
        api_response = api_instance.get_project_document_tonalities(id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_document_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **first_result** | **int**| An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. | [optional] [default to 0]
 **page_size** | **int**| The number of examples to return | [optional] [default to 15]
 **filter_by_tonality** | **bool**| Filter the sentences by only keeping sentences that has a score above 0 for the given tonality | [optional] [default to False]

### Return type

[**TonalitiesResponse**](TonalitiesResponse.md)

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

# **get_project_languages**
> list[ProjectLanguage] get_project_languages(id)

Get project languages

Get languages that is available in the project

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier

    try:
        # Get project languages
        api_response = api_instance.get_project_languages(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 

### Return type

[**list[ProjectLanguage]**](ProjectLanguage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of languages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_report**
> file get_project_report(id, report_id)

Retrieve report

Retrieve a completed report, according to the format specified when the report was requested (through a POST method to the /{id}/reports endpoint). Note that in the data tab which contains the original data, all cells will be formatted as text, even if they were of a different format originally.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | 
report_id = 56 # int | 

    try:
        # Retrieve report
        api_response = api_instance.get_project_report(id, report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **report_id** | **int**|  | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/vnd.ms-excel, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The report file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_reports**
> list[ProjectReport] get_project_reports(id)

Get reports

Get a list of all reports of the given project

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The identifier for the project

    try:
        # Get reports
        api_response = api_instance.get_project_reports(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the project | 

### Return type

[**list[ProjectReport]**](ProjectReport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all created reports for the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[ProjectInfo] get_projects()

Get all projects

For an authenticated user, this method returns all projects accessible by that user.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    
    try:
        # Get all projects
        api_response = api_instance.get_projects()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProjectInfo]**](ProjectInfo.md)

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

# **get_sample_texts**
> list[str] get_sample_texts(project_id, column_header_id, number_of_text_samples=number_of_text_samples)

Get sample texts

Returning a chosen number of rows from a given column in your upload file. In the Explorer GUI the returned samples are shown to the user to verify they are selecting the correct column of text data to analyse.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    project_id = 56 # int | The id of the project
column_header_id = 56 # int | The id of column header to retrieve samples from.
number_of_text_samples = 5 # int | The number of sample texts to return from the corresponding column (optional) (default to 5)

    try:
        # Get sample texts
        api_response = api_instance.get_sample_texts(project_id, column_header_id, number_of_text_samples=number_of_text_samples)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_sample_texts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The id of the project | 
 **column_header_id** | **int**| The id of column header to retrieve samples from. | 
 **number_of_text_samples** | **int**| The number of sample texts to return from the corresponding column | [optional] [default to 5]

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set containing all values available in the given column. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stories**
> StoriesResponse get_stories(id, header_ids=header_ids)

Get Stories

For an authenticated user, this method returns all created stories for the specified project.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
header_ids = [56] # list[int] | The ids of the columns that you would like to receive as extra data with every document (optional)

    try:
        # Get Stories
        api_response = api_instance.get_stories(id, header_ids=header_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **header_ids** | [**list[int]**](int.md)| The ids of the columns that you would like to receive as extra data with every document | [optional] 

### Return type

[**StoriesResponse**](StoriesResponse.md)

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

# **get_supported_languages**
> list[str] get_supported_languages()

Get all supported languages

This method returns all currently supported languages in the Explorer.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    
    try:
        # Get all supported languages
        api_response = api_instance.get_supported_languages()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_supported_languages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

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

# **get_term_details**
> TermDetails get_term_details(id, terms=terms, associations=associations, first_result=first_result, page_size=page_size, sort_by_tonality=sort_by_tonality)

Get topic details

Gets the details of topic terms and associations combinations; e.g.text examples and tonality scores.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier
terms = ['terms_example'] # list[str] | Specify the terms you are interested in getting details for. One query paramter per term like this: ?terms=a_term&amp;terms=some_other_term&amp;... (optional)
associations = ['associations_example'] # list[str] | Optionally specify the associations you are interested in as well. Same format as for the terms: ?associations=association1&amp;associations=assoc2 (optional)
first_result = 0 # int | An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. (optional) (default to 0)
page_size = 15 # int | The number of examples to return. Defaults to 15. (optional) (default to 15)
sort_by_tonality = 'sort_by_tonality_example' # str | The tonality to sort by. From highest value to lowest (optional)

    try:
        # Get topic details
        api_response = api_instance.get_term_details(id, terms=terms, associations=associations, first_result=first_result, page_size=page_size, sort_by_tonality=sort_by_tonality)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_term_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **terms** | [**list[str]**](str.md)| Specify the terms you are interested in getting details for. One query paramter per term like this: ?terms&#x3D;a_term&amp;amp;terms&#x3D;some_other_term&amp;amp;... | [optional] 
 **associations** | [**list[str]**](str.md)| Optionally specify the associations you are interested in as well. Same format as for the terms: ?associations&#x3D;association1&amp;amp;associations&#x3D;assoc2 | [optional] 
 **first_result** | **int**| An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. | [optional] [default to 0]
 **page_size** | **int**| The number of examples to return. Defaults to 15. | [optional] [default to 15]
 **sort_by_tonality** | **str**| The tonality to sort by. From highest value to lowest | [optional] 

### Return type

[**TermDetails**](TermDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the topic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_tonalities**
> TonalitiesResponse get_topic_tonalities(id, group_id, topic_id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality)

Get tonality response

Get result of a topic tonality calculation.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier
group_id = 56 # int | The group identifier
topic_id = 56 # int | The topic identifier. The topic must belong to the group identified by the groupId parameter
first_result = 0 # int | An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. (optional) (default to 0)
page_size = 15 # int | The number of examples to return. Defaults to 15. (optional) (default to 15)
filter_by_tonality = False # bool | Filter the sentences by only keeping sentences that has a score above 0 for the given tonality. (optional) (default to False)

    try:
        # Get tonality response
        api_response = api_instance.get_topic_tonalities(id, group_id, topic_id, first_result=first_result, page_size=page_size, filter_by_tonality=filter_by_tonality)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_topic_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **group_id** | **int**| The group identifier | 
 **topic_id** | **int**| The topic identifier. The topic must belong to the group identified by the groupId parameter | 
 **first_result** | **int**| An index into all available examples matching combination of terms and association. Defaults to 0, which means the first pageSize number of examples. | [optional] [default to 0]
 **page_size** | **int**| The number of examples to return. Defaults to 15. | [optional] [default to 15]
 **filter_by_tonality** | **bool**| Filter the sentences by only keeping sentences that has a score above 0 for the given tonality. | [optional] [default to False]

### Return type

[**TonalitiesResponse**](TonalitiesResponse.md)

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

# **get_versions**
> list[ProjectVersion] get_versions(id)

Get project versions

Get versions of the project

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project

    try:
        # Get project versions
        api_response = api_instance.get_versions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 

### Return type

[**list[ProjectVersion]**](ProjectVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_version**
> ModelVersion publish_version(id, version)

Publish project version to model

Publish project version to model

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
version = 56 # int | The version number

    try:
        # Publish project version to model
        api_response = api_instance.publish_version(id, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->publish_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **version** | **int**| The version number | 

### Return type

[**ModelVersion**](ModelVersion.md)

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

# **remove_folder**
> remove_folder(id)

Remove folder

Removes the folder and the projects and sub folders that are in the folder.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the folder.

    try:
        # Remove folder
        api_instance.remove_folder(id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the folder. | 

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

# **remove_folder_from_folder**
> FolderInformation remove_folder_from_folder(id, sub_folder_id)

Remove sub folder from folder

Remove a sub folder from a folder

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the folder
sub_folder_id = 56 # int | The id of the sub folder

    try:
        # Remove sub folder from folder
        api_response = api_instance.remove_folder_from_folder(id, sub_folder_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_folder_from_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the folder | 
 **sub_folder_id** | **int**| The id of the sub folder | 

### Return type

[**FolderInformation**](FolderInformation.md)

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

# **remove_history**
> remove_history(id, history_id)

Remove history log

Asynchronously removes history data from the project (and the data). When the remove is in progress the project status changes state to ProjectStatus.DELETING. You may query the project to check when then history element is removed. It's not sufficient to only check the ProjectStatus, since it might have status ProjectStatus.EXPLORABLE if the remove operation fails. Additionally, the exploration result of the project is marked 'outdated' to nce the history log data is removed.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
history_id = 56 # int | The id of the history element

    try:
        # Remove history log
        api_instance.remove_history(id, history_id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **history_id** | **int**| The id of the history element | 

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

# **remove_model_from_project**
> remove_model_from_project(id)

Detach model from project

Detach the model from the project. If the dynamic model was created from the project, all dependent projects will receive the corresponding update. Alternatively, if the model was applied to the project, only that version of the model will be impacted. Note that the only possible update in this scenario is an update of translations.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier

    try:
        # Detach model from project
        api_instance.remove_model_from_project(id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_model_from_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 

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
**200** | The model containing the updated information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project**
> remove_project(id)

Remove project

Removes the project. This call will return at once and the project will enter the ProjectStatus#DELETING} status. You could optionally repeatedly query the /projects endpoint to see when the project disappears.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The identifier for the project to remove

    try:
        # Remove project
        api_instance.remove_project(id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the project to remove | 

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

# **remove_project_from_folder**
> FolderInformation remove_project_from_folder(id, project_id)

Remove project from folder

Removes a project from a folder (the project itself is not removed).

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the folder
project_id = 56 # int | The id of the project

    try:
        # Remove project from folder
        api_response = api_instance.remove_project_from_folder(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_project_from_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the folder | 
 **project_id** | **int**| The id of the project | 

### Return type

[**FolderInformation**](FolderInformation.md)

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

# **remove_report**
> remove_report(id, report_id)

Remove report

Removes the project report

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The identifier for the project
report_id = 56 # int | 

    try:
        # Remove report
        api_instance.remove_report(id, report_id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier for the project | 
 **report_id** | **int**|  | 

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

# **revert_to_version**
> revert_to_version(id, version)

Revert to version

Revert to a project version. A version revert will result in a new project version

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
version = 56 # int | The project version

    try:
        # Revert to version
        api_instance.revert_to_version(id, version)
    except ApiException as e:
        print("Exception when calling ProjectsApi->revert_to_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **version** | **int**| The project version | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_for_project_terms**
> list[str] search_for_project_terms(id, lookfor)

Search Project Terms

Get all the terms in the project that begin with the provided string (corpus search)

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
lookfor = 'lookfor_example' # str | String to search for. Needs to be 2 characters or more

    try:
        # Search Project Terms
        api_response = api_instance.search_for_project_terms(id, lookfor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->search_for_project_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **lookfor** | **str**| String to search for. Needs to be 2 characters or more | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of terms. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_coverage_tonalities**
> start_coverage_tonalities(id, sort_by_tonality=sort_by_tonality, order_by=order_by)

Start Coverage Tonalities Calculation

Starts an asynchronous coverage tonalities calculation. The information returned includes tonality scores broken down for each document not included in any topic and an aggregated score for all such documents. A GET request to the same url will fetch the progress of the calculations. To be able to use this function, coverage analysis must be enabled in either the account settings (see Accounts section of docs) or the project settings (through /explorer/projects/{id}).

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier
sort_by_tonality = 'sort_by_tonality_example' # str | Which tonality you want to sort by. Name of tonality must be capitalized (optional)
order_by = 'SENTIMENT_DESC' # str | Which order you want the results (optional) (default to 'SENTIMENT_DESC')

    try:
        # Start Coverage Tonalities Calculation
        api_instance.start_coverage_tonalities(id, sort_by_tonality=sort_by_tonality, order_by=order_by)
    except ApiException as e:
        print("Exception when calling ProjectsApi->start_coverage_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **sort_by_tonality** | **str**| Which tonality you want to sort by. Name of tonality must be capitalized | [optional] 
 **order_by** | **str**| Which order you want the results | [optional] [default to &#39;SENTIMENT_DESC&#39;]

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

# **start_group_tonalities**
> start_group_tonalities(id, group_id, tonalities_request_context, terms=terms, associations=associations, sort_by_tonality=sort_by_tonality, order_by=order_by)

Start tonality calculation

Starts an asynchronous group tonalities calculation. A GET request to the same url will fetch the progress. <br/><br/> NOTE: The existing method of specifying terms and associations as query parameters has been deprecated. Please use the request body object TonalitiesRequestContext to specify these fields instead

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier.
group_id = 56 # int | The group identifier.
tonalities_request_context = explorer_client.TonalitiesRequestContext() # TonalitiesRequestContext | The context of the tonalities request, specifically with regards to terms to include. If the context element provided in the request, the corresponding query parameters are ignored.
terms = ['terms_example'] # list[str] | DEPRECATED - please use the request body object to specify terms instead. Specify the terms you are interested in getting details for. If left empty all group terms will be taken into account. One query parameter per term like this: ?terms=a_term&amp;terms=some_other_term&amp;... (optional)
associations = ['associations_example'] # list[str] | DEPRECATED - please use the request body object to specify associations instead. Optionally specify the associations you are interested in as well. Same format as for the terms: ?associations=association1&amp;associations=assoc2 (optional)
sort_by_tonality = 'sort_by_tonality_example' # str | Which tonality you want to sort by. (optional)
order_by = 'SENTIMENT_DESC' # str | The order of the examples to return. Defaults to SENTIMENT_DESC. (optional) (default to 'SENTIMENT_DESC')

    try:
        # Start tonality calculation
        api_instance.start_group_tonalities(id, group_id, tonalities_request_context, terms=terms, associations=associations, sort_by_tonality=sort_by_tonality, order_by=order_by)
    except ApiException as e:
        print("Exception when calling ProjectsApi->start_group_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier. | 
 **group_id** | **int**| The group identifier. | 
 **tonalities_request_context** | [**TonalitiesRequestContext**](TonalitiesRequestContext.md)| The context of the tonalities request, specifically with regards to terms to include. If the context element provided in the request, the corresponding query parameters are ignored. | 
 **terms** | [**list[str]**](str.md)| DEPRECATED - please use the request body object to specify terms instead. Specify the terms you are interested in getting details for. If left empty all group terms will be taken into account. One query parameter per term like this: ?terms&#x3D;a_term&amp;amp;terms&#x3D;some_other_term&amp;amp;... | [optional] 
 **associations** | [**list[str]**](str.md)| DEPRECATED - please use the request body object to specify associations instead. Optionally specify the associations you are interested in as well. Same format as for the terms: ?associations&#x3D;association1&amp;amp;associations&#x3D;assoc2 | [optional] 
 **sort_by_tonality** | **str**| Which tonality you want to sort by. | [optional] 
 **order_by** | **str**| The order of the examples to return. Defaults to SENTIMENT_DESC. | [optional] [default to &#39;SENTIMENT_DESC&#39;]

### Return type

void (empty response body)

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

# **start_project_document_tonalities**
> start_project_document_tonalities(id, sort_by_tonality=sort_by_tonality, order_by=order_by)

Start Document Tonalities

Starts an asynchronous document tonalities calculation. A GET request to the same url will fetch the progress of such a calculation. The result will be based on all documents in the project, unless the project has filters is applied (in which case the result be based documents that fulfil the filtering conditions).

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
sort_by_tonality = 'sort_by_tonality_example' # str | Which tonality you want to sort by. Name of tonality must be capitalized. (optional)
order_by = 'SENTIMENT_DESC' # str | The order of the examples to return. Defaults to SENTIMENT_DESC. (optional) (default to 'SENTIMENT_DESC')

    try:
        # Start Document Tonalities
        api_instance.start_project_document_tonalities(id, sort_by_tonality=sort_by_tonality, order_by=order_by)
    except ApiException as e:
        print("Exception when calling ProjectsApi->start_project_document_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **sort_by_tonality** | **str**| Which tonality you want to sort by. Name of tonality must be capitalized. | [optional] 
 **order_by** | **str**| The order of the examples to return. Defaults to SENTIMENT_DESC. | [optional] [default to &#39;SENTIMENT_DESC&#39;]

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

# **start_topic_tonalities**
> start_topic_tonalities(id, group_id, topic_id, tonalities_request_context, terms=terms, associations=associations, sort_by_tonality=sort_by_tonality, order_by=order_by)

Start tonality calculation

Starts an asynchronous topic tonalities calculation. A GET request to the same url will fetchthe progress. <br/><br/>NOTE: The existing method of specifying terms and associations as query parameters has beendeprecated. Please use the request body object TonalitiesRequestContext tospecify these fields instead

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The project identifier.
group_id = 56 # int | The group identifier.
topic_id = 56 # int | The topic identifier. The topic must belong to the group identified by the groupId parameter
tonalities_request_context = explorer_client.TonalitiesRequestContext() # TonalitiesRequestContext | The context of the tonalities request, specifically with regards to terms to include. If the context element provided in the request, the corresponding query parameters are ignored.
terms = ['terms_example'] # list[str] | DEPRECATED - please use the request body object to specify terms instead. Specify the terms you are interested in getting details for. If left empty all group terms will be taken into account One query paramter per term like this:?terms=a_term&amp;terms=some_other_term&amp;... (optional)
associations = ['associations_example'] # list[str] | DEPRECATED - please use the request body object to specify associations instead. Optionally specify the associations you are interested in as well. Same format as for the terms: ?associations=association1&amp;associations=assoc2 (optional)
sort_by_tonality = 'sort_by_tonality_example' # str | Which tonality you want to sort by. (optional)
order_by = 'SENTIMENT_DESC' # str | The order of the examples to return. Defaults to SENTIMENT_DESC. (optional) (default to 'SENTIMENT_DESC')

    try:
        # Start tonality calculation
        api_instance.start_topic_tonalities(id, group_id, topic_id, tonalities_request_context, terms=terms, associations=associations, sort_by_tonality=sort_by_tonality, order_by=order_by)
    except ApiException as e:
        print("Exception when calling ProjectsApi->start_topic_tonalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier. | 
 **group_id** | **int**| The group identifier. | 
 **topic_id** | **int**| The topic identifier. The topic must belong to the group identified by the groupId parameter | 
 **tonalities_request_context** | [**TonalitiesRequestContext**](TonalitiesRequestContext.md)| The context of the tonalities request, specifically with regards to terms to include. If the context element provided in the request, the corresponding query parameters are ignored. | 
 **terms** | [**list[str]**](str.md)| DEPRECATED - please use the request body object to specify terms instead. Specify the terms you are interested in getting details for. If left empty all group terms will be taken into account One query paramter per term like this:?terms&#x3D;a_term&amp;amp;terms&#x3D;some_other_term&amp;amp;... | [optional] 
 **associations** | [**list[str]**](str.md)| DEPRECATED - please use the request body object to specify associations instead. Optionally specify the associations you are interested in as well. Same format as for the terms: ?associations&#x3D;association1&amp;amp;associations&#x3D;assoc2 | [optional] 
 **sort_by_tonality** | **str**| Which tonality you want to sort by. | [optional] 
 **order_by** | **str**| The order of the examples to return. Defaults to SENTIMENT_DESC. | [optional] [default to &#39;SENTIMENT_DESC&#39;]

### Return type

void (empty response body)

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

# **stop_subscribing_to_updates**
> stop_subscribing_to_updates(id)

Stop subscribing to updates from a model

Stop subscribing to updates from the model that the project is currently subscribing to.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project

    try:
        # Stop subscribing to updates from a model
        api_instance.stop_subscribing_to_updates(id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->stop_subscribing_to_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> FolderInformation update_folder(folder_id, folder_request)

Update folder

Updates the folder meta-information, such as the name.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    folder_id = 56 # int | The id of the folder
folder_request = explorer_client.FolderRequest() # FolderRequest | The folder update request

    try:
        # Update folder
        api_response = api_instance.update_folder(folder_id, folder_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The id of the folder | 
 **folder_request** | [**FolderRequest**](FolderRequest.md)| The folder update request | 

### Return type

[**FolderInformation**](FolderInformation.md)

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

# **update_header**
> ColumnHeader update_header(id, header_id, column_header_update)

Update project header

Update a project header

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
header_id = 56 # int | The id of the header
column_header_update = explorer_client.ColumnHeaderUpdate() # ColumnHeaderUpdate | The request body

    try:
        # Update project header
        api_response = api_instance.update_header(id, header_id, column_header_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **header_id** | **int**| The id of the header | 
 **column_header_update** | [**ColumnHeaderUpdate**](ColumnHeaderUpdate.md)| The request body | 

### Return type

[**ColumnHeader**](ColumnHeader.md)

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

# **update_project**
> Project update_project(id, project_request)

Update project

Updates the project name, the project specific settings or connect the project to a model. To see the possible values for project settings, along with an explanation for each field, call a GET request on this same endpoint. <br/><br/>Note that the model identified by the modelId field must be a dynamic model, in which case the project will be dependent on the model.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The identifier of the project
project_request = explorer_client.ProjectRequest() # ProjectRequest | The information with which to update the project

    try:
        # Update project
        api_response = api_instance.update_project(id, project_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the project | 
 **project_request** | [**ProjectRequest**](ProjectRequest.md)| The information with which to update the project | 

### Return type

[**Project**](Project.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | he project containing the updated information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_model**
> Model update_project_model(id, model_input)

Update Project Model

Updates the model to which a project is connected. If the dynamic model was created from the project, all dependent projects will receive the corresponding update. Alternatively, if the model was applied to the project, only that version of the model will be impacted. Note that the only possible update in this scenario is an update of translations.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
model_input = explorer_client.ModelInput() # ModelInput | The information with which to update the project.

    try:
        # Update Project Model
        api_response = api_instance.update_project_model(id, model_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_project_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **model_input** | [**ModelInput**](ModelInput.md)| The information with which to update the project. | 

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
**200** | The model containing the updated information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> ProjectVersion update_version(id, version, project_version_update)

Update version

Update a project version

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
    api_instance = explorer_client.ProjectsApi(api_client)
    id = 56 # int | The id of the project
version = 56 # int | The project version
project_version_update = explorer_client.ProjectVersionUpdate() # ProjectVersionUpdate | The update request

    try:
        # Update version
        api_response = api_instance.update_version(id, version, project_version_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project | 
 **version** | **int**| The project version | 
 **project_version_update** | [**ProjectVersionUpdate**](ProjectVersionUpdate.md)| The update request | 

### Return type

[**ProjectVersion**](ProjectVersion.md)

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

# **upload_project_file**
> ProjectId upload_project_file(file, file_name, encoding=encoding, title=title, analyzing_column_index=analyzing_column_index, rows_to_analyse=rows_to_analyse)

Create project

For an authenticated user, this method will upload a CSV file that will be used to create a project. This will send the data to the server and return a response (with the project id) when the data is sent. The new project will then enter the INITIALIZING status and you may query the project (send a GET to /projects/{id}) until it changes status to EXPLORABLE}. In the case of multipart form data the parts need to be 'file' with the binary data and 'fileName' with the file name as plain text 

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
    api_instance = explorer_client.ProjectsApi(api_client)
    file = '/path/to/file' # file | input file
file_name = 'file_name_example' # str | 
encoding = 'encoding_example' # str | Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. (optional)
title = 'title_example' # str | Title of the project. In absence of this parameter, the project will be initialized with a null title. (optional)
analyzing_column_index = 56 # int | The index of the column in the sheet containing the data to be analyzed. Indices are counted starting from 1. (optional)
rows_to_analyse = 56 # int | The number of rows of the file provided that should be used in analysis. This parameter should be used if you do not wish to analyse all rows of the file you have uploaded but only a subset of the file. (optional)

    try:
        # Create project
        api_response = api_instance.upload_project_file(file, file_name, encoding=encoding, title=title, analyzing_column_index=analyzing_column_index, rows_to_analyse=rows_to_analyse)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->upload_project_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| input file | 
 **file_name** | **str**|  | 
 **encoding** | **str**| Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. | [optional] 
 **title** | **str**| Title of the project. In absence of this parameter, the project will be initialized with a null title. | [optional] 
 **analyzing_column_index** | **int**| The index of the column in the sheet containing the data to be analyzed. Indices are counted starting from 1. | [optional] 
 **rows_to_analyse** | **int**| The number of rows of the file provided that should be used in analysis. This parameter should be used if you do not wish to analyse all rows of the file you have uploaded but only a subset of the file. | [optional] 

### Return type

[**ProjectId**](ProjectId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project**
> ProjectId upload_project(rows_data, encoding=encoding, title=title, analyzing_column_index=analyzing_column_index, rows_to_analyse=rows_to_analyse)

Create project

For an authenticated user, this method will upload rows that will be used to create a project. This will send the data to the server and return a response (with the project id) when the data is sent. The new project will then enter the INITIALIZING status and you may query the project (send a GET to /projects/{id}) until it changes status to EXPLORABLE}.

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
    api_instance = explorer_client.ProjectsApi(api_client)
    rows_data = explorer_client.RowsData() # rows_data | the rows of the project
encoding = 'encoding_example' # str | Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. (optional)
title = 'title_example' # str | Title of the project. In absence of this parameter, the project will be initialized with a null title. (optional)
analyzing_column_index = 56 # int | The index of the column in the sheet containing the data to be analyzed. Indices are counted starting from 1. (optional)
rows_to_analyse = 56 # int | The number of rows of the file provided that should be used in analysis. This parameter should be used if you do not wish to analyse all rows of the file you have uploaded but only a subset of the file. (optional)

    try:
        # Create project
        api_response = api_instance.upload_project(rows_data, encoding=encoding, title=title, analyzing_column_index=analyzing_column_index, rows_to_analyse=rows_to_analyse)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->upload_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rows_data** |  [**RowsData**](RowsData.md)| the rows of the project  | 
 **encoding** | **str**| Use this parameter if you know exactly what the encoding of the file is. If nothing is provided a best guess is performed. | [optional] 
 **title** | **str**| Title of the project. In absence of this parameter, the project will be initialized with a null title. | [optional] 
 **analyzing_column_index** | **int**| The index of the column in the sheet containing the data to be analyzed. Indices are counted starting from 1. | [optional] 
 **rows_to_analyse** | **int**| The number of rows of the file provided that should be used in analysis. This parameter should be used if you do not wish to analyse all rows of the file you have uploaded but only a subset of the file. | [optional] 

### Return type

[**ProjectId**](ProjectId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_filter_date_format**
> FilterValidation validate_filter_date_format(project_id, column_header_id, value_format)

Validate your data filter format

In Explorer there is the possibility to filter your documents using meta-information. When filtering by date, it is important that the system correctly parses the date information column. This is done according to a provided value format for the input info. This API call can be used to validate the value format provided, to check the system will correctly interpret the date format in your file. Reference: <a href=\"https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_str-to-date\">https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_str-to-date</a>

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
    api_instance = explorer_client.ProjectsApi(api_client)
    project_id = 56 # int | The id of the project
column_header_id = 56 # int | The id of the column with date information to be validated
value_format = 'value_format_example' # str | The valueFormat Example: To map column data in the format '2018-06-18 11:33:23' you need a valueFormat like '%Y-%m-%d %T'

    try:
        # Validate your data filter format
        api_response = api_instance.validate_filter_date_format(project_id, column_header_id, value_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->validate_filter_date_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The id of the project | 
 **column_header_id** | **int**| The id of the column with date information to be validated | 
 **value_format** | **str**| The valueFormat Example: To map column data in the format &#39;2018-06-18 11:33:23&#39; you need a valueFormat like &#39;%Y-%m-%d %T&#39; | 

### Return type

[**FilterValidation**](FilterValidation.md)

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
