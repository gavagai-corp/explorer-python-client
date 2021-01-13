# explorer_client.DashboardsApi

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_graph**](DashboardsApi.md#create_dashboard_graph) | **POST** /projects/{id}/explore/dashboard/graphs | Create Graph
[**create_topic_graph**](DashboardsApi.md#create_topic_graph) | **POST** /projects/{id}/explore/dashboard/topic_graphs | Create topic Graphs
[**delete_dashboard_graph**](DashboardsApi.md#delete_dashboard_graph) | **DELETE** /projects/{id}/explore/dashboard/graphs/{graphId} | Delete Graph
[**delete_topic_graph**](DashboardsApi.md#delete_topic_graph) | **DELETE** /projects/{id}/explore/dashboard/topic_graphs/{graphId} | Delete Topic Graph
[**get_associations_timeseries_graph_data**](DashboardsApi.md#get_associations_timeseries_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/associations_timeseries | Get the Associations Timeseries graph data
[**get_average_score_graph_data**](DashboardsApi.md#get_average_score_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore | Get AvgScore Graph
[**get_average_score_matrix_graph_data**](DashboardsApi.md#get_average_score_matrix_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore_matrix | Get Average Score Matrix Data
[**get_compiled_graph_share_data**](DashboardsApi.md#get_compiled_graph_share_data) | **GET** /projects/{id}/explore/dashboard/graphs/sharedata | Retrieve the compiled graph data
[**get_compiled_graph_share_data_progress**](DashboardsApi.md#get_compiled_graph_share_data_progress) | **GET** /projects/{id}/explore/dashboard/graphs/sharedata/progress | Retrieve the progress
[**get_graphs_for_project**](DashboardsApi.md#get_graphs_for_project) | **GET** /projects/{id}/explore/dashboard/graphs | Get a list of graphs.
[**get_grouped_comparison_graph_context**](DashboardsApi.md#get_grouped_comparison_graph_context) | **GET** /projects/{id}/explore/dashboard/graphs/comparison_grouped_context | Get Grouped Comparison Graph Context
[**get_grouped_comparison_graph_data**](DashboardsApi.md#get_grouped_comparison_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/grouped_comparison | Get Grouped Comparison Graph
[**get_high_impact_association_graph_container**](DashboardsApi.md#get_high_impact_association_graph_container) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpactassociation | Get High Impact Topic Associations Graph
[**get_high_impact_graph_data**](DashboardsApi.md#get_high_impact_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpact | Get High Impact Topics Graph
[**get_net_sentiment_timeseries_graph_data**](DashboardsApi.md#get_net_sentiment_timeseries_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/netsentiment_timeseries | Get the Net Sentiment Timeseries
[**get_timeseries_comparison_graph_data**](DashboardsApi.md#get_timeseries_comparison_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/timeseries_comparison | Get Time Series Comparison Graph
[**get_topic_associations_graph_data**](DashboardsApi.md#get_topic_associations_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/associations | Get the association graph data
[**get_topic_average_score_matrix_graph_data**](DashboardsApi.md#get_topic_average_score_matrix_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/averagescore_matrix | Get the average score matrix
[**get_topic_graphs**](DashboardsApi.md#get_topic_graphs) | **GET** /projects/{id}/explore/dashboard/topic_graphs | Get topic Graphs
[**get_topic_information_graph_data**](DashboardsApi.md#get_topic_information_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/topic_information | Get the topic information graph
[**get_topic_text_examples**](DashboardsApi.md#get_topic_text_examples) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/text_examples | Get the text examples for the selected topic
[**initialize_dashboard**](DashboardsApi.md#initialize_dashboard) | **POST** /projects/{id}/explore/dashboard/initialize | Initialize Dashboard
[**modify_dashboard_graph**](DashboardsApi.md#modify_dashboard_graph) | **PUT** /projects/{id}/explore/dashboard/graphs/{graphId} | Update Graph
[**set_associations_timeseries_graph_context**](DashboardsApi.md#set_associations_timeseries_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/associations_timeseries | Update the context of the Associations Timeseries graph data
[**set_net_sentiment_timeseries_graph_context**](DashboardsApi.md#set_net_sentiment_timeseries_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/netsentiment_timeseries | Update Net Sentiment Timeseries Context
[**set_topic_average_score_matrix_graph_context**](DashboardsApi.md#set_topic_average_score_matrix_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/averagescore_matrix | Put the context of the Average Score Matrix
[**set_topic_information_graph_context**](DashboardsApi.md#set_topic_information_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topic_information | Put the context of the Topic Information graph data
[**set_topic_text_examples_context**](DashboardsApi.md#set_topic_text_examples_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/text_examples | Put the context of the Topic Text examples graph data
[**start_associations_timeseries_graph_data**](DashboardsApi.md#start_associations_timeseries_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/associations_timeseries | Start the Associations Timeseries
[**start_average_score_graph_data**](DashboardsApi.md#start_average_score_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore | Start AvgScore Calculation
[**start_average_score_matrix_graph_data**](DashboardsApi.md#start_average_score_matrix_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore_matrix | Start Average Score Matrix Calculation
[**start_compile_graph_share_data**](DashboardsApi.md#start_compile_graph_share_data) | **POST** /projects/{id}/explore/dashboard/graphs/sharedata | Start Compiling Dashboard graphs
[**start_grouped_comparison_graph_data**](DashboardsApi.md#start_grouped_comparison_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/grouped_comparison | Start Grouped Comparison Calculation
[**start_high_impact_association_graph_container**](DashboardsApi.md#start_high_impact_association_graph_container) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpactassociation | Start High Impact Topic Associations Calculation
[**start_high_impact_graph_data**](DashboardsApi.md#start_high_impact_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpact | Start High Impact Topic Calculation
[**start_net_sentiment_timeseries_graph_data**](DashboardsApi.md#start_net_sentiment_timeseries_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/netsentiment_timeseries | Start the Net Sentiment Timeseries
[**start_timeseries_comparison_graph_data**](DashboardsApi.md#start_timeseries_comparison_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/timeseries_comparison | Start Time Series Comparison Calculation
[**start_topic_average_score_matrix_graph_data**](DashboardsApi.md#start_topic_average_score_matrix_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/averagescore_matrix | Start the computation of the Average Score Matrix
[**start_topic_information_graph_data**](DashboardsApi.md#start_topic_information_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/topic_information | Start the computation of the Topic Information
[**start_topic_text_examples**](DashboardsApi.md#start_topic_text_examples) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/text_examples | Start the computation of the Topic Text
[**update_topic_graph**](DashboardsApi.md#update_topic_graph) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId} | Update topic Graphs


# **create_dashboard_graph**
> GraphInfo create_dashboard_graph(id, create_graph_request)

Create Graph

Creates a graph in the dashboard

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
create_graph_request = explorer_client.CreateGraphRequest() # CreateGraphRequest | The graph creation request

    try:
        # Create Graph
        api_response = api_instance.create_dashboard_graph(id, create_graph_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->create_dashboard_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **create_graph_request** | [**CreateGraphRequest**](CreateGraphRequest.md)| The graph creation request | 

### Return type

[**GraphInfo**](GraphInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The representation of the created graph |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_topic_graph**
> TopicGraphInfo create_topic_graph(id, topic_graph_create_request)

Create topic Graphs

Creates a topic graph

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
topic_graph_create_request = explorer_client.TopicGraphCreateRequest() # TopicGraphCreateRequest | The topic graph creation request

    try:
        # Create topic Graphs
        api_response = api_instance.create_topic_graph(id, topic_graph_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->create_topic_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **topic_graph_create_request** | [**TopicGraphCreateRequest**](TopicGraphCreateRequest.md)| The topic graph creation request | 

### Return type

[**TopicGraphInfo**](TopicGraphInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The representation of the created graph |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_graph**
> delete_dashboard_graph(id, graph_id)

Delete Graph

Delete the created graph

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Delete Graph
        api_instance.delete_dashboard_graph(id, graph_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->delete_dashboard_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

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

# **delete_topic_graph**
> delete_topic_graph(id, graph_id)

Delete Topic Graph

Delete the created topic graph

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Delete Topic Graph
        api_instance.delete_topic_graph(id, graph_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->delete_topic_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

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

# **get_associations_timeseries_graph_data**
> AssociationsTimeseriesGraphResponse get_associations_timeseries_graph_data(id, topic_id, graph_id)

Get the Associations Timeseries graph data

Get the Associations Timeseries graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
topic_id = 56 # int | The topic identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get the Associations Timeseries graph data
        api_response = api_instance.get_associations_timeseries_graph_data(id, topic_id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_associations_timeseries_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **topic_id** | **int**| The topic identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**AssociationsTimeseriesGraphResponse**](AssociationsTimeseriesGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The associations time series graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_average_score_graph_data**
> AverageScoreGraphResponse get_average_score_graph_data(id, graph_id)

Get AvgScore Graph

Get the Average Score graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get AvgScore Graph
        api_response = api_instance.get_average_score_graph_data(id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_average_score_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**AverageScoreGraphResponse**](AverageScoreGraphResponse.md)

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

# **get_average_score_matrix_graph_data**
> AverageScoreMatrixGraphResponse get_average_score_matrix_graph_data(id, graph_id)

Get Average Score Matrix Data

Get average score matrix graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get Average Score Matrix Data
        api_response = api_instance.get_average_score_matrix_graph_data(id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_average_score_matrix_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**AverageScoreMatrixGraphResponse**](AverageScoreMatrixGraphResponse.md)

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

# **get_compiled_graph_share_data**
> CompiledGraphData get_compiled_graph_share_data(id)

Retrieve the compiled graph data

Retrieve the compiled graph data required needed for sharing the dashboards for the specified project

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project id for which the data is required

    try:
        # Retrieve the compiled graph data
        api_response = api_instance.get_compiled_graph_share_data(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_compiled_graph_share_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project id for which the data is required | 

### Return type

[**CompiledGraphData**](CompiledGraphData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response containing all data needed for sharing the dashboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compiled_graph_share_data_progress**
> GraphDataProgress get_compiled_graph_share_data_progress(id)

Retrieve the progress

Retrieve the progress of the data compilation process for the specified project

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project id for which the progress is required

    try:
        # Retrieve the progress
        api_response = api_instance.get_compiled_graph_share_data_progress(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_compiled_graph_share_data_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project id for which the progress is required | 

### Return type

[**GraphDataProgress**](GraphDataProgress.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The progress of the data compilation process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_graphs_for_project**
> GraphInfoResponse get_graphs_for_project(id)

Get a list of graphs.

Get average score matrix graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier

    try:
        # Get a list of graphs.
        api_response = api_instance.get_graphs_for_project(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_graphs_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 

### Return type

[**GraphInfoResponse**](GraphInfoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of graphs with relevant fields. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grouped_comparison_graph_context**
> ComparisonGraphContext get_grouped_comparison_graph_context(id)

Get Grouped Comparison Graph Context

Get grouped comparison graph context

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier

    try:
        # Get Grouped Comparison Graph Context
        api_response = api_instance.get_grouped_comparison_graph_context(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_grouped_comparison_graph_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 

### Return type

[**ComparisonGraphContext**](ComparisonGraphContext.md)

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

# **get_grouped_comparison_graph_data**
> GroupedComparisonGraphResponse get_grouped_comparison_graph_data(id, graph_id)

Get Grouped Comparison Graph

Get grouped comparison graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get Grouped Comparison Graph
        api_response = api_instance.get_grouped_comparison_graph_data(id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_grouped_comparison_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**GroupedComparisonGraphResponse**](GroupedComparisonGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the comparison calculation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_high_impact_association_graph_container**
> HighImpactAssociationsGraphResponse get_high_impact_association_graph_container(id, graph_id)

Get High Impact Topic Associations Graph

Get the High Impact Topic Associations graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get High Impact Topic Associations Graph
        api_response = api_instance.get_high_impact_association_graph_container(id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_high_impact_association_graph_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**HighImpactAssociationsGraphResponse**](HighImpactAssociationsGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The high impact graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_high_impact_graph_data**
> HighImpactGraphResponse get_high_impact_graph_data(id, graph_id)

Get High Impact Topics Graph

Get the High Impact Topics graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get High Impact Topics Graph
        api_response = api_instance.get_high_impact_graph_data(id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_high_impact_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**HighImpactGraphResponse**](HighImpactGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The high impact graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_net_sentiment_timeseries_graph_data**
> NetSentimentTimeseriesGraphResponse get_net_sentiment_timeseries_graph_data(id, topic_id, graph_id)

Get the Net Sentiment Timeseries

Get the Net Sentiment Timeseries graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
topic_id = 56 # int | The topic identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get the Net Sentiment Timeseries
        api_response = api_instance.get_net_sentiment_timeseries_graph_data(id, topic_id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_net_sentiment_timeseries_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **topic_id** | **int**| The topic identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**NetSentimentTimeseriesGraphResponse**](NetSentimentTimeseriesGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The net sentiment timeseries graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timeseries_comparison_graph_data**
> TimeseriesComparisonGraphResponse get_timeseries_comparison_graph_data(id, graph_id)

Get Time Series Comparison Graph

Get timeseries comparison graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get Time Series Comparison Graph
        api_response = api_instance.get_timeseries_comparison_graph_data(id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_timeseries_comparison_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**TimeseriesComparisonGraphResponse**](TimeseriesComparisonGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of all lines in the graph and it&#39;s corresponding request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_associations_graph_data**
> TopicAssociationsGraphResponse get_topic_associations_graph_data(id, topic_id, graph_id)

Get the association graph data

Get the association graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
topic_id = 56 # int | The topic identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get the association graph data
        api_response = api_instance.get_topic_associations_graph_data(id, topic_id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_topic_associations_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **topic_id** | **int**| The topic identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**TopicAssociationsGraphResponse**](TopicAssociationsGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The topic associations graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_average_score_matrix_graph_data**
> TopicAverageScoreMatrixGraphResponse get_topic_average_score_matrix_graph_data(id, topic_id, graph_id)

Get the average score matrix

Get the average score matrix for the selected topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
topic_id = 56 # int | The topic identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get the average score matrix
        api_response = api_instance.get_topic_average_score_matrix_graph_data(id, topic_id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_topic_average_score_matrix_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **topic_id** | **int**| The topic identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**TopicAverageScoreMatrixGraphResponse**](TopicAverageScoreMatrixGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The average score matrix graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_graphs**
> TopicGraphInfoResponse get_topic_graphs(id)

Get topic Graphs

Get a list of topic graphs

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier

    try:
        # Get topic Graphs
        api_response = api_instance.get_topic_graphs(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_topic_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 

### Return type

[**TopicGraphInfoResponse**](TopicGraphInfoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of graphs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_information_graph_data**
> TopicInformationGraphResponse get_topic_information_graph_data(id, topic_id, graph_id)

Get the topic information graph

Get the topic information graph for the selected topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
topic_id = 56 # int | The topic identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get the topic information graph
        api_response = api_instance.get_topic_information_graph_data(id, topic_id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_topic_information_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **topic_id** | **int**| The topic identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**TopicInformationGraphResponse**](TopicInformationGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The topic information graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_text_examples**
> TopicTextExamplesGraphResponse get_topic_text_examples(id, topic_id, graph_id)

Get the text examples for the selected topic

Get the text examples for the selected topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
topic_id = 56 # int | The topic identifier
graph_id = 'graph_id_example' # str | The graph identifier

    try:
        # Get the text examples for the selected topic
        api_response = api_instance.get_topic_text_examples(id, topic_id, graph_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_topic_text_examples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **topic_id** | **int**| The topic identifier | 
 **graph_id** | **str**| The graph identifier | 

### Return type

[**TopicTextExamplesGraphResponse**](TopicTextExamplesGraphResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The text examples graph response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_dashboard**
> initialize_dashboard(id)

Initialize Dashboard

Initialize the dashboard with all the default graphs

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier

    try:
        # Initialize Dashboard
        api_instance.initialize_dashboard(id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->initialize_dashboard: %s\n" % e)
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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_dashboard_graph**
> GraphInfo modify_dashboard_graph(id, graph_id, create_graph_request)

Update Graph

Modifies the the graph

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
create_graph_request = explorer_client.CreateGraphRequest() # CreateGraphRequest | The graph update request

    try:
        # Update Graph
        api_response = api_instance.modify_dashboard_graph(id, graph_id, create_graph_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->modify_dashboard_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **create_graph_request** | [**CreateGraphRequest**](CreateGraphRequest.md)| The graph update request | 

### Return type

[**GraphInfo**](GraphInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The modified graph |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_associations_timeseries_graph_context**
> set_associations_timeseries_graph_context(id, graph_id, associations_timeseries_graph_context)

Update the context of the Associations Timeseries graph data

Put the context of the Associations Timeseries graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
associations_timeseries_graph_context = explorer_client.AssociationsTimeseriesGraphContext() # AssociationsTimeseriesGraphContext | The request body

    try:
        # Update the context of the Associations Timeseries graph data
        api_instance.set_associations_timeseries_graph_context(id, graph_id, associations_timeseries_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->set_associations_timeseries_graph_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **associations_timeseries_graph_context** | [**AssociationsTimeseriesGraphContext**](AssociationsTimeseriesGraphContext.md)| The request body | 

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

# **set_net_sentiment_timeseries_graph_context**
> set_net_sentiment_timeseries_graph_context(id, graph_id, net_sentiment_timeseries_graph_context)

Update Net Sentiment Timeseries Context

Put the context of the Net Sentiment Timeseries graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
net_sentiment_timeseries_graph_context = explorer_client.NetSentimentTimeseriesGraphContext() # NetSentimentTimeseriesGraphContext | The request body

    try:
        # Update Net Sentiment Timeseries Context
        api_instance.set_net_sentiment_timeseries_graph_context(id, graph_id, net_sentiment_timeseries_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->set_net_sentiment_timeseries_graph_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **net_sentiment_timeseries_graph_context** | [**NetSentimentTimeseriesGraphContext**](NetSentimentTimeseriesGraphContext.md)| The request body | 

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

# **set_topic_average_score_matrix_graph_context**
> set_topic_average_score_matrix_graph_context(id, graph_id, topic_average_score_matrix_graph_context)

Put the context of the Average Score Matrix

Put the context of the Average Score Matrix graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_average_score_matrix_graph_context = explorer_client.TopicAverageScoreMatrixGraphContext() # TopicAverageScoreMatrixGraphContext | The request body

    try:
        # Put the context of the Average Score Matrix
        api_instance.set_topic_average_score_matrix_graph_context(id, graph_id, topic_average_score_matrix_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->set_topic_average_score_matrix_graph_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_average_score_matrix_graph_context** | [**TopicAverageScoreMatrixGraphContext**](TopicAverageScoreMatrixGraphContext.md)| The request body | 

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

# **set_topic_information_graph_context**
> set_topic_information_graph_context(id, graph_id, topic_information_graph_context)

Put the context of the Topic Information graph data

Put the context of the Topic Information graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_information_graph_context = explorer_client.TopicInformationGraphContext() # TopicInformationGraphContext | The request body

    try:
        # Put the context of the Topic Information graph data
        api_instance.set_topic_information_graph_context(id, graph_id, topic_information_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->set_topic_information_graph_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_information_graph_context** | [**TopicInformationGraphContext**](TopicInformationGraphContext.md)| The request body | 

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

# **set_topic_text_examples_context**
> set_topic_text_examples_context(id, graph_id, topic_text_examples_graph_context)

Put the context of the Topic Text examples graph data

Put the context of the Topic Text examples graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_text_examples_graph_context = explorer_client.TopicTextExamplesGraphContext() # TopicTextExamplesGraphContext | The request body

    try:
        # Put the context of the Topic Text examples graph data
        api_instance.set_topic_text_examples_context(id, graph_id, topic_text_examples_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->set_topic_text_examples_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_text_examples_graph_context** | [**TopicTextExamplesGraphContext**](TopicTextExamplesGraphContext.md)| The request body | 

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

# **start_associations_timeseries_graph_data**
> start_associations_timeseries_graph_data(id, graph_id, topic_id)

Start the Associations Timeseries

Start the Associations Timeseries graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_id = 56 # int | The topic identifier

    try:
        # Start the Associations Timeseries
        api_instance.start_associations_timeseries_graph_data(id, graph_id, topic_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_associations_timeseries_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_id** | **int**| The topic identifier | 

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

# **start_average_score_graph_data**
> start_average_score_graph_data(id, graph_id, average_score_graph_context)

Start AvgScore Calculation

Starts the process of generating Average Score graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
average_score_graph_context = explorer_client.AverageScoreGraphContext() # AverageScoreGraphContext | The request body

    try:
        # Start AvgScore Calculation
        api_instance.start_average_score_graph_data(id, graph_id, average_score_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_average_score_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **average_score_graph_context** | [**AverageScoreGraphContext**](AverageScoreGraphContext.md)| The request body | 

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

# **start_average_score_matrix_graph_data**
> start_average_score_matrix_graph_data(id, graph_id, average_score_matrix_graph_context)

Start Average Score Matrix Calculation

Starts the process of generating average score matrix graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
average_score_matrix_graph_context = explorer_client.AverageScoreMatrixGraphContext() # AverageScoreMatrixGraphContext | The request body

    try:
        # Start Average Score Matrix Calculation
        api_instance.start_average_score_matrix_graph_data(id, graph_id, average_score_matrix_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_average_score_matrix_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **average_score_matrix_graph_context** | [**AverageScoreMatrixGraphContext**](AverageScoreMatrixGraphContext.md)| The request body | 

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

# **start_compile_graph_share_data**
> start_compile_graph_share_data(id)

Start Compiling Dashboard graphs

Start the process that compiles graph data needed for sharing the dashboards for the specified project

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier

    try:
        # Start Compiling Dashboard graphs
        api_instance.start_compile_graph_share_data(id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_compile_graph_share_data: %s\n" % e)
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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_grouped_comparison_graph_data**
> start_grouped_comparison_graph_data(id, graph_id, grouped_comparison_graph_context)

Start Grouped Comparison Calculation

Starts the process of generating grouped comparison graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
grouped_comparison_graph_context = explorer_client.GroupedComparisonGraphContext() # GroupedComparisonGraphContext | The request body

    try:
        # Start Grouped Comparison Calculation
        api_instance.start_grouped_comparison_graph_data(id, graph_id, grouped_comparison_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_grouped_comparison_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **grouped_comparison_graph_context** | [**GroupedComparisonGraphContext**](GroupedComparisonGraphContext.md)| The request body | 

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

# **start_high_impact_association_graph_container**
> start_high_impact_association_graph_container(id, graph_id, high_impact_associations_graph_context)

Start High Impact Topic Associations Calculation

Starts the process of generating High Impact Topic Associations graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
high_impact_associations_graph_context = explorer_client.HighImpactAssociationsGraphContext() # HighImpactAssociationsGraphContext | The request body

    try:
        # Start High Impact Topic Associations Calculation
        api_instance.start_high_impact_association_graph_container(id, graph_id, high_impact_associations_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_high_impact_association_graph_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **high_impact_associations_graph_context** | [**HighImpactAssociationsGraphContext**](HighImpactAssociationsGraphContext.md)| The request body | 

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

# **start_high_impact_graph_data**
> start_high_impact_graph_data(id, graph_id, high_impact_graph_context)

Start High Impact Topic Calculation

Starts the process of generating High Impact Topics graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
high_impact_graph_context = explorer_client.HighImpactGraphContext() # HighImpactGraphContext | The request body

    try:
        # Start High Impact Topic Calculation
        api_instance.start_high_impact_graph_data(id, graph_id, high_impact_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_high_impact_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **high_impact_graph_context** | [**HighImpactGraphContext**](HighImpactGraphContext.md)| The request body | 

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

# **start_net_sentiment_timeseries_graph_data**
> start_net_sentiment_timeseries_graph_data(id, graph_id, topic_id)

Start the Net Sentiment Timeseries

Start the process of generating Net Sentiment Timeseries graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_id = 56 # int | The topic identifier

    try:
        # Start the Net Sentiment Timeseries
        api_instance.start_net_sentiment_timeseries_graph_data(id, graph_id, topic_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_net_sentiment_timeseries_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_id** | **int**| The topic identifier | 

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

# **start_timeseries_comparison_graph_data**
> start_timeseries_comparison_graph_data(id, graph_id, timeseries_comparison_graph_context)

Start Time Series Comparison Calculation

Starts the process of generating time series comparison graph data

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
timeseries_comparison_graph_context = explorer_client.TimeseriesComparisonGraphContext() # TimeseriesComparisonGraphContext | The the request

    try:
        # Start Time Series Comparison Calculation
        api_instance.start_timeseries_comparison_graph_data(id, graph_id, timeseries_comparison_graph_context)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_timeseries_comparison_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **timeseries_comparison_graph_context** | [**TimeseriesComparisonGraphContext**](TimeseriesComparisonGraphContext.md)| The the request | 

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

# **start_topic_average_score_matrix_graph_data**
> start_topic_average_score_matrix_graph_data(id, graph_id, topic_id)

Start the computation of the Average Score Matrix

Start the computation of the Average Score Matrix graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_id = 56 # int | The topic identifier

    try:
        # Start the computation of the Average Score Matrix
        api_instance.start_topic_average_score_matrix_graph_data(id, graph_id, topic_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_topic_average_score_matrix_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_id** | **int**| The topic identifier | 

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

# **start_topic_information_graph_data**
> start_topic_information_graph_data(id, graph_id, topic_id)

Start the computation of the Topic Information

Start the computation of the Topic Information graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_id = 56 # int | The topic identifier

    try:
        # Start the computation of the Topic Information
        api_instance.start_topic_information_graph_data(id, graph_id, topic_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_topic_information_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_id** | **int**| The topic identifier | 

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

# **start_topic_text_examples**
> start_topic_text_examples(id, graph_id, topic_id)

Start the computation of the Topic Text

Start the computation of the Topic Text examples graph data for a specific topic

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_id = 56 # int | The topic identifier

    try:
        # Start the computation of the Topic Text
        api_instance.start_topic_text_examples(id, graph_id, topic_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->start_topic_text_examples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_id** | **int**| The topic identifier | 

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

# **update_topic_graph**
> TopicGraphInfo update_topic_graph(id, graph_id, topic_graph_create_request)

Update topic Graphs

Modifies the topic graph

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
    api_instance = explorer_client.DashboardsApi(api_client)
    id = 56 # int | The project identifier
graph_id = 'graph_id_example' # str | The graph identifier
topic_graph_create_request = explorer_client.TopicGraphCreateRequest() # TopicGraphCreateRequest | The topic graph update request

    try:
        # Update topic Graphs
        api_response = api_instance.update_topic_graph(id, graph_id, topic_graph_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->update_topic_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project identifier | 
 **graph_id** | **str**| The graph identifier | 
 **topic_graph_create_request** | [**TopicGraphCreateRequest**](TopicGraphCreateRequest.md)| The topic graph update request | 

### Return type

[**TopicGraphInfo**](TopicGraphInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The modified graph |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

