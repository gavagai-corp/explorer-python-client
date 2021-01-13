# explorer-client
<p>This is the technical documentation for the Gavagai Explorer API.</p><p>We recommend that you get familiar with using <a href=\"https://explorer.gavagai.se/\">Gavagai Explorer</a> before you start developing with the API. The Explorer has its own <a href=\"https://gavagai-corp.github.io/explorer/\"> general documentation</a>.</p><p>Make sure that you understand the basic procedures, such as creating projects and uploading texts, exploring and refining your project, or creating reports and applying models. All functionality in Gavagai Explorer is built on this API, so you will have a much easier time understanding the different steps if you have already seen them in the Explorer web interface.</p> <p>The <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/99319872/Gavagai+Explorer+API+Tutorial\">Getting Started</a> tutorial and the <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/322797577/Explorer+API+Common+Use+Cases\"> Common Use Cases </a>section provide more guidance in understanding how the different API calls can be fitted together to create a workflow. The documentation below then provides full technical specifics for each endpoint.</p>

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

You can install the python package directly using:

```sh
pip install git+https://github.com/gavagai-corp/explorer-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/gavagai-corp/explorer-python-client.git`)

Then import the package:
```python
import explorer_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import explorer_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.gavagai.se/explorer/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**accept_manager_invitation**](docs/AccountsApi.md#accept_manager_invitation) | **PUT** /account/invitations/{id}/accept | Acccept Manager Invitation
*AccountsApi* | [**cancel_account**](docs/AccountsApi.md#cancel_account) | **DELETE** /account/cancel | Cancel Account
*AccountsApi* | [**cancel_product_plan_migration**](docs/AccountsApi.md#cancel_product_plan_migration) | **DELETE** /account/product/migration | Cancel Product Plan Migration
*AccountsApi* | [**create_manager_invitation**](docs/AccountsApi.md#create_manager_invitation) | **POST** /account/invitations | Create Manager Invitation
*AccountsApi* | [**delete_managed_user**](docs/AccountsApi.md#delete_managed_user) | **DELETE** /account/managedUsers/{userId} | Delete Managed User
*AccountsApi* | [**delete_manager**](docs/AccountsApi.md#delete_manager) | **DELETE** /account/manager | Delete manager
*AccountsApi* | [**delete_manager_invitation**](docs/AccountsApi.md#delete_manager_invitation) | **DELETE** /account/invitations/{id} | Delete Manager Invitation
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /account | Get Account
*AccountsApi* | [**get_account_balance**](docs/AccountsApi.md#get_account_balance) | **GET** /account/balance | Get Account Balance
*AccountsApi* | [**get_credit_statistics**](docs/AccountsApi.md#get_credit_statistics) | **GET** /account/credits/statistics | Get Credit Statistics
*AccountsApi* | [**get_credits**](docs/AccountsApi.md#get_credits) | **GET** /account/credits | Get Credits
*AccountsApi* | [**get_manager_invitations**](docs/AccountsApi.md#get_manager_invitations) | **GET** /account/invitations | Get Manager Invitations
*AccountsApi* | [**get_pending_payment**](docs/AccountsApi.md#get_pending_payment) | **GET** /account/pendingPayment | Get Pending Payments
*AccountsApi* | [**get_product_plan**](docs/AccountsApi.md#get_product_plan) | **GET** /account/product | Get Product Plan
*AccountsApi* | [**get_usage**](docs/AccountsApi.md#get_usage) | **GET** /account/usage | Get Usage
*AccountsApi* | [**get_user_settings**](docs/AccountsApi.md#get_user_settings) | **GET** /account/settings | Get User Settings
*AccountsApi* | [**purchase_credits**](docs/AccountsApi.md#purchase_credits) | **POST** /account/credits | Purchase Credits
*AccountsApi* | [**reactivate_account**](docs/AccountsApi.md#reactivate_account) | **POST** /account/reactivate | Reactivate Account
*AccountsApi* | [**reject_manager_invitation**](docs/AccountsApi.md#reject_manager_invitation) | **PUT** /account/invitations/{id}/reject | Reject Manager Invitation
*AccountsApi* | [**set_product_plan**](docs/AccountsApi.md#set_product_plan) | **PUT** /account/product | Set Product Plan
*AccountsApi* | [**update_user_settings**](docs/AccountsApi.md#update_user_settings) | **PUT** /account/settings | Update User Settings
*DashboardsApi* | [**create_dashboard_graph**](docs/DashboardsApi.md#create_dashboard_graph) | **POST** /projects/{id}/explore/dashboard/graphs | Create Graph
*DashboardsApi* | [**create_topic_graph**](docs/DashboardsApi.md#create_topic_graph) | **POST** /projects/{id}/explore/dashboard/topic_graphs | Create topic Graphs
*DashboardsApi* | [**delete_dashboard_graph**](docs/DashboardsApi.md#delete_dashboard_graph) | **DELETE** /projects/{id}/explore/dashboard/graphs/{graphId} | Delete Graph
*DashboardsApi* | [**delete_topic_graph**](docs/DashboardsApi.md#delete_topic_graph) | **DELETE** /projects/{id}/explore/dashboard/topic_graphs/{graphId} | Delete Topic Graph
*DashboardsApi* | [**get_associations_timeseries_graph_data**](docs/DashboardsApi.md#get_associations_timeseries_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/associations_timeseries | Get the Associations Timeseries graph data
*DashboardsApi* | [**get_average_score_graph_data**](docs/DashboardsApi.md#get_average_score_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore | Get AvgScore Graph
*DashboardsApi* | [**get_average_score_matrix_graph_data**](docs/DashboardsApi.md#get_average_score_matrix_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore_matrix | Get Average Score Matrix Data
*DashboardsApi* | [**get_compiled_graph_share_data**](docs/DashboardsApi.md#get_compiled_graph_share_data) | **GET** /projects/{id}/explore/dashboard/graphs/sharedata | Retrieve the compiled graph data
*DashboardsApi* | [**get_compiled_graph_share_data_progress**](docs/DashboardsApi.md#get_compiled_graph_share_data_progress) | **GET** /projects/{id}/explore/dashboard/graphs/sharedata/progress | Retrieve the progress
*DashboardsApi* | [**get_graphs_for_project**](docs/DashboardsApi.md#get_graphs_for_project) | **GET** /projects/{id}/explore/dashboard/graphs | Get a list of graphs.
*DashboardsApi* | [**get_groupd_comparison_graph_data**](docs/DashboardsApi.md#get_groupd_comparison_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/grouped_comparison | Get Grouped Comparison Graph
*DashboardsApi* | [**get_grouped_comparison_graph_context**](docs/DashboardsApi.md#get_grouped_comparison_graph_context) | **GET** /projects/{id}/explore/dashboard/graphs/comparison_grouped_context | Get Grouped Comparison Graph Context
*DashboardsApi* | [**get_high_impact_association_graph_container**](docs/DashboardsApi.md#get_high_impact_association_graph_container) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpactassociation | Get High Impact Topic Associations Graph
*DashboardsApi* | [**get_high_impact_graph_data**](docs/DashboardsApi.md#get_high_impact_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpact | Get High Impact Topics Graph
*DashboardsApi* | [**get_net_sentiment_timeseries_graph_data**](docs/DashboardsApi.md#get_net_sentiment_timeseries_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/netsentiment_timeseries | Get the Net Sentiment Timeseries
*DashboardsApi* | [**get_timeseries_comparison_graph_data**](docs/DashboardsApi.md#get_timeseries_comparison_graph_data) | **GET** /projects/{id}/explore/dashboard/graphs/{graphId}/timeseries_comparison | Get Time Series Comparison Graph
*DashboardsApi* | [**get_topic_associations_graph_data**](docs/DashboardsApi.md#get_topic_associations_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/associations | Get the association graph data
*DashboardsApi* | [**get_topic_average_score_matrix_graph_data**](docs/DashboardsApi.md#get_topic_average_score_matrix_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/averagescore_matrix | Get the average score matrix
*DashboardsApi* | [**get_topic_graphs**](docs/DashboardsApi.md#get_topic_graphs) | **GET** /projects/{id}/explore/dashboard/topic_graphs | Get topic Graphs
*DashboardsApi* | [**get_topic_information_graph_data**](docs/DashboardsApi.md#get_topic_information_graph_data) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/topic_information | Get the topic information graph
*DashboardsApi* | [**get_topic_text_examples**](docs/DashboardsApi.md#get_topic_text_examples) | **GET** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/text_examples | Get the text examples for the selected topic
*DashboardsApi* | [**initialize_dashboard**](docs/DashboardsApi.md#initialize_dashboard) | **POST** /projects/{id}/explore/dashboard/initialize | Initialize Dashboard
*DashboardsApi* | [**modify_dashboard_graph**](docs/DashboardsApi.md#modify_dashboard_graph) | **PUT** /projects/{id}/explore/dashboard/graphs/{graphId} | Update Graph
*DashboardsApi* | [**set_associations_timeseries_graph_context**](docs/DashboardsApi.md#set_associations_timeseries_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/associations_timeseries | Update the context of the Associations Timeseries graph data
*DashboardsApi* | [**set_net_sentiment_timeseries_graph_context**](docs/DashboardsApi.md#set_net_sentiment_timeseries_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/netsentiment_timeseries | Update Net Sentiment Timeseries Context
*DashboardsApi* | [**set_topic_average_score_matrix_graph_context**](docs/DashboardsApi.md#set_topic_average_score_matrix_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/averagescore_matrix | Put the context of the Average Score Matrix
*DashboardsApi* | [**set_topic_information_graph_context**](docs/DashboardsApi.md#set_topic_information_graph_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topic_information | Put the context of the Topic Information graph data
*DashboardsApi* | [**set_topic_text_examples_context**](docs/DashboardsApi.md#set_topic_text_examples_context) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/text_examples | Put the context of the Topic Text examples graph data
*DashboardsApi* | [**start_associations_timeseries_graph_data**](docs/DashboardsApi.md#start_associations_timeseries_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/associations_timeseries | Start the Associations Timeseries
*DashboardsApi* | [**start_average_score_graph_data**](docs/DashboardsApi.md#start_average_score_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore | Start AvgScore Calculation
*DashboardsApi* | [**start_average_score_matrix_graph_data**](docs/DashboardsApi.md#start_average_score_matrix_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/averagescore_matrix | Start Average Score Matrix Calculation
*DashboardsApi* | [**start_compile_graph_share_data**](docs/DashboardsApi.md#start_compile_graph_share_data) | **POST** /projects/{id}/explore/dashboard/graphs/sharedata | Start Compiling Dashboard graphs
*DashboardsApi* | [**start_grouped_comparison_graph_data**](docs/DashboardsApi.md#start_grouped_comparison_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/grouped_comparison | Start Grouped Comparison Calculation
*DashboardsApi* | [**start_high_impact_association_graph_container**](docs/DashboardsApi.md#start_high_impact_association_graph_container) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpactassociation | Start High Impact Topic Associations Calculation
*DashboardsApi* | [**start_high_impact_graph_data**](docs/DashboardsApi.md#start_high_impact_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/highimpact | Start High Impact Topic Calculation
*DashboardsApi* | [**start_net_sentiment_timeseries_graph_data**](docs/DashboardsApi.md#start_net_sentiment_timeseries_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/netsentiment_timeseries | Start the Net Sentiment Timeseries
*DashboardsApi* | [**start_timeseries_comparison_graph_data**](docs/DashboardsApi.md#start_timeseries_comparison_graph_data) | **POST** /projects/{id}/explore/dashboard/graphs/{graphId}/timeseries_comparison | Start Time Series Comparison Calculation
*DashboardsApi* | [**start_topic_average_score_matrix_graph_data**](docs/DashboardsApi.md#start_topic_average_score_matrix_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/averagescore_matrix | Start the computation of the Average Score Matrix
*DashboardsApi* | [**start_topic_information_graph_data**](docs/DashboardsApi.md#start_topic_information_graph_data) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/topic_information | Start the computation of the Topic Information
*DashboardsApi* | [**start_topic_text_examples**](docs/DashboardsApi.md#start_topic_text_examples) | **POST** /projects/{id}/explore/dashboard/topic_graphs/{graphId}/topics/{topicId}/text_examples | Start the computation of the Topic Text
*DashboardsApi* | [**update_topic_graph**](docs/DashboardsApi.md#update_topic_graph) | **PUT** /projects/{id}/explore/dashboard/topic_graphs/{graphId} | Update topic Graphs
*FileUtilitiesApi* | [**get_file_details**](docs/FileUtilitiesApi.md#get_file_details) | **POST** /file-utilities/details | Get File Details
*FileUtilitiesApi* | [**get_first_row**](docs/FileUtilitiesApi.md#get_first_row) | **POST** /file-utilities/header_row | Get First Row
*ModelsApi* | [**accept_invitation**](docs/ModelsApi.md#accept_invitation) | **PUT** /models/invitations/{invitationId}/accept | Accept Model Invitations
*ModelsApi* | [**create_model**](docs/ModelsApi.md#create_model) | **POST** /models/create | Create Model
*ModelsApi* | [**get_model**](docs/ModelsApi.md#get_model) | **GET** /models/{id} | Get Model
*ModelsApi* | [**get_model_invitations**](docs/ModelsApi.md#get_model_invitations) | **GET** /models/invitations | Get Model Invitations
*ModelsApi* | [**get_model_projects**](docs/ModelsApi.md#get_model_projects) | **GET** /models/{id}/projects | Get Projects
*ModelsApi* | [**get_model_versions**](docs/ModelsApi.md#get_model_versions) | **GET** /models/{id}/versions | Get Model Versions
*ModelsApi* | [**get_models**](docs/ModelsApi.md#get_models) | **GET** /models | Get Models
*ModelsApi* | [**get_versioned_model**](docs/ModelsApi.md#get_versioned_model) | **GET** /models/{id}/versions/{version} | Get Model Version
*ModelsApi* | [**reject_invitation**](docs/ModelsApi.md#reject_invitation) | **PUT** /models/invitations/{invitationId}/reject | Reject Model Invitations
*ModelsApi* | [**remove_model**](docs/ModelsApi.md#remove_model) | **DELETE** /models/{id} | Delete Model
*ModelsApi* | [**remove_model_access**](docs/ModelsApi.md#remove_model_access) | **DELETE** /models/{id}/userRights/{accessId} | Remove Model Access
*ModelsApi* | [**remove_model_invitation**](docs/ModelsApi.md#remove_model_invitation) | **DELETE** /models/{id}/invitations/{invitationId} | Remove Model Invitation
*ModelsApi* | [**share_model**](docs/ModelsApi.md#share_model) | **POST** /models/{id}/share | Share Model
*ModelsApi* | [**update_model**](docs/ModelsApi.md#update_model) | **PUT** /models/{id} | Update Model
*ModelsApi* | [**upload_model_from_file**](docs/ModelsApi.md#upload_model_from_file) | **POST** /models | Upload Model
*PluginsApi* | [**get_plugin_details**](docs/PluginsApi.md#get_plugin_details) | **GET** /plugins/{id} | Get Plugin
*PluginsApi* | [**get_plugins**](docs/PluginsApi.md#get_plugins) | **GET** /plugins | Get Plugins
*PluginsApi* | [**get_survey**](docs/PluginsApi.md#get_survey) | **GET** /plugins/survey_monkey/surveys/{id} | Get Survey
*PluginsApi* | [**get_surveys**](docs/PluginsApi.md#get_surveys) | **GET** /plugins/survey_monkey/surveys | Get Surveys
*PluginsApi* | [**import_survey**](docs/PluginsApi.md#import_survey) | **POST** /plugins/survey_monkey/surveys/{id}/import | Import Survey
*PluginsApi* | [**survey_monkey_auth**](docs/PluginsApi.md#survey_monkey_auth) | **GET** /plugins/survey_monkey/auth | Authenticate the survey monkey plugin
*PluginsApi* | [**survey_monkey_callback**](docs/PluginsApi.md#survey_monkey_callback) | **GET** /plugins/survey_monkey/callback | Callback endpoint for the survey monkey plugin
*PolesApi* | [**create_pole**](docs/PolesApi.md#create_pole) | **POST** /poles | Create Pole
*PolesApi* | [**delete_pole**](docs/PolesApi.md#delete_pole) | **DELETE** /poles/{id} | Delete Pole
*PolesApi* | [**get_pole**](docs/PolesApi.md#get_pole) | **GET** /poles/{id} | Get Pole
*PolesApi* | [**get_poles**](docs/PolesApi.md#get_poles) | **GET** /poles | Get Poles
*PolesApi* | [**get_suggestions_for_pole**](docs/PolesApi.md#get_suggestions_for_pole) | **GET** /poles/{id}/suggest | Get Pole Suggestions
*PolesApi* | [**update_pole**](docs/PolesApi.md#update_pole) | **PUT** /poles/{id} | Update Pole
*ProductsApi* | [**get_credit_price**](docs/ProductsApi.md#get_credit_price) | **GET** /products/creditPrice | Get Credit Price
*ProductsApi* | [**get_product_plans**](docs/ProductsApi.md#get_product_plans) | **GET** /products | Get Product Plans
*ProjectsApi* | [**add_folder_to_folder**](docs/ProjectsApi.md#add_folder_to_folder) | **PUT** /projects/folders/{id}/folders/{subFolderId} | Add sub folder to folder
*ProjectsApi* | [**add_project_to_folder**](docs/ProjectsApi.md#add_project_to_folder) | **PUT** /projects/folders/{id}/projects/{projectId} | Add project to folder
*ProjectsApi* | [**append_to_project**](docs/ProjectsApi.md#append_to_project) | **POST** /projects/{id}/append | Add data to project
*ProjectsApi* | [**append_file_to_project**](docs/ProjectsApi.md#append_file_to_project) | **POST** /projects/{id}/append | Add data to project
*ProjectsApi* | [**create_batch**](docs/ProjectsApi.md#create_batch) | **POST** /projects/{id}/batches | Start Batch Calculation
*ProjectsApi* | [**create_folder**](docs/ProjectsApi.md#create_folder) | **POST** /projects/folders | Create folder
*ProjectsApi* | [**create_report**](docs/ProjectsApi.md#create_report) | **POST** /projects/{id}/reports | Create report
*ProjectsApi* | [**create_stories**](docs/ProjectsApi.md#create_stories) | **POST** /projects/{id}/stories | Create Stories
*ProjectsApi* | [**explore_project**](docs/ProjectsApi.md#explore_project) | **POST** /projects/{id}/explore | Explore project
*ProjectsApi* | [**find_suggestions**](docs/ProjectsApi.md#find_suggestions) | **POST** /projects/{id}/suggestions | Get suggestions for terms
*ProjectsApi* | [**get_batch_result**](docs/ProjectsApi.md#get_batch_result) | **GET** /projects/{id}/batches/{batchId} | Get Batch Calculation
*ProjectsApi* | [**get_cell_information**](docs/ProjectsApi.md#get_cell_information) | **GET** /projects/{id}/result/cells | Get cell data
*ProjectsApi* | [**get_coverage_tonalities**](docs/ProjectsApi.md#get_coverage_tonalities) | **GET** /projects/{id}/explore/coverageStatistics/tonalities | Get Coverage Tonalities
*ProjectsApi* | [**get_distinct_column_values**](docs/ProjectsApi.md#get_distinct_column_values) | **GET** /projects/{id}/columns/{columnHeaderId} | Get distinct column values
*ProjectsApi* | [**get_exploration**](docs/ProjectsApi.md#get_exploration) | **GET** /projects/{id}/explore | Get Explore Results
*ProjectsApi* | [**get_folder**](docs/ProjectsApi.md#get_folder) | **GET** /projects/folders/{id} | Get folder
*ProjectsApi* | [**get_folders**](docs/ProjectsApi.md#get_folders) | **GET** /projects/folders | Get folders
*ProjectsApi* | [**get_group_tonalities**](docs/ProjectsApi.md#get_group_tonalities) | **GET** /projects/{id}/explore/groups/{groupId}/tonalities | Get tonality response
*ProjectsApi* | [**get_matching_sentences_for_terms**](docs/ProjectsApi.md#get_matching_sentences_for_terms) | **GET** /projects/{id}/sentences | Get sentences
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects/{id} | Get project
*ProjectsApi* | [**get_project_document_tonalities**](docs/ProjectsApi.md#get_project_document_tonalities) | **GET** /projects/{id}/explore/projectTonalities/tonalities | Get Document Tonalities
*ProjectsApi* | [**get_project_languages**](docs/ProjectsApi.md#get_project_languages) | **GET** /projects/languages | Get all supported languages
*ProjectsApi* | [**get_project_languages1**](docs/ProjectsApi.md#get_project_languages1) | **GET** /projects/{id}/languages | Get project languages
*ProjectsApi* | [**get_project_report**](docs/ProjectsApi.md#get_project_report) | **GET** /projects/{id}/reports/{reportId} | Retrieve report
*ProjectsApi* | [**get_project_reports**](docs/ProjectsApi.md#get_project_reports) | **GET** /projects/{id}/reports | Get reports
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Get all projects
*ProjectsApi* | [**get_sample_texts**](docs/ProjectsApi.md#get_sample_texts) | **GET** /projects/{projectId}/headers/{columnHeaderId}/samples | Get sample texts
*ProjectsApi* | [**get_stories**](docs/ProjectsApi.md#get_stories) | **GET** /projects/{id}/stories | Get Stories
*ProjectsApi* | [**get_term_details**](docs/ProjectsApi.md#get_term_details) | **GET** /projects/{id}/details | Get topic details
*ProjectsApi* | [**get_topic_tonalities**](docs/ProjectsApi.md#get_topic_tonalities) | **GET** /projects/{id}/explore/groups/{groupId}/topics/{topicId}/tonalities | Get tonality response
*ProjectsApi* | [**remove_folder**](docs/ProjectsApi.md#remove_folder) | **DELETE** /projects/folders/{id} | Remove folder
*ProjectsApi* | [**remove_folder_from_folder**](docs/ProjectsApi.md#remove_folder_from_folder) | **DELETE** /projects/folders/{id}/folders/{subFolderId} | Remove sub folder from folder
*ProjectsApi* | [**remove_history**](docs/ProjectsApi.md#remove_history) | **DELETE** /projects/{id}/history/{historyId} | Remove history log
*ProjectsApi* | [**remove_model_from_project**](docs/ProjectsApi.md#remove_model_from_project) | **DELETE** /projects/{id}/model | Detach model from project
*ProjectsApi* | [**remove_project**](docs/ProjectsApi.md#remove_project) | **DELETE** /projects/{id} | Remove project
*ProjectsApi* | [**remove_project_from_folder**](docs/ProjectsApi.md#remove_project_from_folder) | **DELETE** /projects/folders/{id}/projects/{projectId} | Remove project from folder
*ProjectsApi* | [**remove_report**](docs/ProjectsApi.md#remove_report) | **DELETE** /projects/{id}/reports/{reportId} | Remove report
*ProjectsApi* | [**search_for_project_terms**](docs/ProjectsApi.md#search_for_project_terms) | **GET** /projects/{id}/result/searchTerms | Search Project Terms
*ProjectsApi* | [**start_coverage_tonalities**](docs/ProjectsApi.md#start_coverage_tonalities) | **POST** /projects/{id}/explore/coverageStatistics/tonalities | Start Coverage Tonalities Calculation
*ProjectsApi* | [**start_group_tonalities**](docs/ProjectsApi.md#start_group_tonalities) | **POST** /projects/{id}/explore/groups/{groupId}/tonalities | Start tonality calculation
*ProjectsApi* | [**start_project_document_tonalities**](docs/ProjectsApi.md#start_project_document_tonalities) | **POST** /projects/{id}/explore/projectTonalities/tonalities | Start Document Tonalities
*ProjectsApi* | [**start_topic_tonalities**](docs/ProjectsApi.md#start_topic_tonalities) | **POST** /projects/{id}/explore/groups/{groupId}/topics/{topicId}/tonalities | Start tonality calculation
*ProjectsApi* | [**update_folder**](docs/ProjectsApi.md#update_folder) | **PUT** /projects/folders/{folderId} | Update folder
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects/{id} | Update project
*ProjectsApi* | [**update_project_model**](docs/ProjectsApi.md#update_project_model) | **PUT** /projects/{id}/model | Update Project Model
*ProjectsApi* | [**upload_project**](docs/ProjectsApi.md#upload_project) | **POST** /projects | Create project
*ProjectsApi* | [**upload_project_file**](docs/ProjectsApi.md#upload_project_file) | **POST** /projects | Create project
*ProjectsApi* | [**validate_filter_date_format**](docs/ProjectsApi.md#validate_filter_date_format) | **GET** /projects/{projectId}/headers/{columnHeaderId}/validateFilterFormat | Validate your data filter format
*StatusApi* | [**ping_service**](docs/StatusApi.md#ping_service) | **GET** /status | Get System Status
*TonalityCustomizationApi* | [**create_tonality_customization**](docs/TonalityCustomizationApi.md#create_tonality_customization) | **POST** /tonality-customizations | Create Tonality Customization
*TonalityCustomizationApi* | [**delete_tonality_customization**](docs/TonalityCustomizationApi.md#delete_tonality_customization) | **DELETE** /tonality-customizations/{id} | Delete Tonality Customization
*TonalityCustomizationApi* | [**get_tonality_customization**](docs/TonalityCustomizationApi.md#get_tonality_customization) | **GET** /tonality-customizations/{id} | Get Tonality Customization
*TonalityCustomizationApi* | [**get_tonality_customizations**](docs/TonalityCustomizationApi.md#get_tonality_customizations) | **GET** /tonality-customizations | Get Tonality Customizations
*TonalityCustomizationApi* | [**get_tonality_details_for_terms**](docs/TonalityCustomizationApi.md#get_tonality_details_for_terms) | **GET** /tonality-customizations/details | Get Term Tonalitites
*TonalityCustomizationApi* | [**update_tonality_customization**](docs/TonalityCustomizationApi.md#update_tonality_customization) | **PUT** /tonality-customizations/{id} | Update Tonality Customization


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountBalance](docs/AccountBalance.md)
 - [AccountReactivationRequest](docs/AccountReactivationRequest.md)
 - [AccountReactivationResponse](docs/AccountReactivationResponse.md)
 - [AssociationsTimeseriesGraphContext](docs/AssociationsTimeseriesGraphContext.md)
 - [AssociationsTimeseriesGraphData](docs/AssociationsTimeseriesGraphData.md)
 - [AssociationsTimeseriesGraphResponse](docs/AssociationsTimeseriesGraphResponse.md)
 - [AutoAddTerm](docs/AutoAddTerm.md)
 - [AverageScoreGraphContext](docs/AverageScoreGraphContext.md)
 - [AverageScoreGraphData](docs/AverageScoreGraphData.md)
 - [AverageScoreGraphResponse](docs/AverageScoreGraphResponse.md)
 - [AverageScoreMatrixGraphContext](docs/AverageScoreMatrixGraphContext.md)
 - [AverageScoreMatrixGraphData](docs/AverageScoreMatrixGraphData.md)
 - [AverageScoreMatrixGraphResponse](docs/AverageScoreMatrixGraphResponse.md)
 - [BatchId](docs/BatchId.md)
 - [BatchRequest](docs/BatchRequest.md)
 - [BatchResponse](docs/BatchResponse.md)
 - [BatchTextRequest](docs/BatchTextRequest.md)
 - [BatchTextResponse](docs/BatchTextResponse.md)
 - [BatchTextTonality](docs/BatchTextTonality.md)
 - [BatchTopicDefinition](docs/BatchTopicDefinition.md)
 - [CellTonality](docs/CellTonality.md)
 - [CellTopicInformation](docs/CellTopicInformation.md)
 - [ColumnHeader](docs/ColumnHeader.md)
 - [ComparisonGraphContext](docs/ComparisonGraphContext.md)
 - [ComparisonLayer](docs/ComparisonLayer.md)
 - [CompiledGraphData](docs/CompiledGraphData.md)
 - [CompiledTopicGraphData](docs/CompiledTopicGraphData.md)
 - [ConceptFilter](docs/ConceptFilter.md)
 - [CoverageStatistics](docs/CoverageStatistics.md)
 - [CreateGraphRequest](docs/CreateGraphRequest.md)
 - [CreditPrice](docs/CreditPrice.md)
 - [CreditPurchase](docs/CreditPurchase.md)
 - [CreditPurchaseResponse](docs/CreditPurchaseResponse.md)
 - [CreditStatistics](docs/CreditStatistics.md)
 - [CreditsHistoryDataPoint](docs/CreditsHistoryDataPoint.md)
 - [CustomToneTerm](docs/CustomToneTerm.md)
 - [DataSegment](docs/DataSegment.md)
 - [DocumentReference](docs/DocumentReference.md)
 - [DocumentSentences](docs/DocumentSentences.md)
 - [Driver](docs/Driver.md)
 - [DriverRequest](docs/DriverRequest.md)
 - [DriverResponse](docs/DriverResponse.md)
 - [ExplorationStatus](docs/ExplorationStatus.md)
 - [FileDetails](docs/FileDetails.md)
 - [Filter](docs/Filter.md)
 - [FilterValidation](docs/FilterValidation.md)
 - [FolderInformation](docs/FolderInformation.md)
 - [FolderRequest](docs/FolderRequest.md)
 - [FolderStructure](docs/FolderStructure.md)
 - [GraphData](docs/GraphData.md)
 - [GraphDataProgress](docs/GraphDataProgress.md)
 - [GraphInfo](docs/GraphInfo.md)
 - [GraphInfoResponse](docs/GraphInfoResponse.md)
 - [GroupDefinition](docs/GroupDefinition.md)
 - [GroupedComparisonDataPoint](docs/GroupedComparisonDataPoint.md)
 - [GroupedComparisonGraphContext](docs/GroupedComparisonGraphContext.md)
 - [GroupedComparisonGraphData](docs/GroupedComparisonGraphData.md)
 - [GroupedComparisonGraphResponse](docs/GroupedComparisonGraphResponse.md)
 - [HeaderRow](docs/HeaderRow.md)
 - [HealthCheckReport](docs/HealthCheckReport.md)
 - [HealthCheckResult](docs/HealthCheckResult.md)
 - [HighImpactAssociationsGraphContext](docs/HighImpactAssociationsGraphContext.md)
 - [HighImpactAssociationsGraphData](docs/HighImpactAssociationsGraphData.md)
 - [HighImpactAssociationsGraphResponse](docs/HighImpactAssociationsGraphResponse.md)
 - [HighImpactGraphContext](docs/HighImpactGraphContext.md)
 - [HighImpactGraphData](docs/HighImpactGraphData.md)
 - [HighImpactGraphResponse](docs/HighImpactGraphResponse.md)
 - [HighImpactTopicAssociation](docs/HighImpactTopicAssociation.md)
 - [HighImpactTopicAssociationsGraphData](docs/HighImpactTopicAssociationsGraphData.md)
 - [HistoryLog](docs/HistoryLog.md)
 - [IgnoreTerm](docs/IgnoreTerm.md)
 - [IgnoreTermChangeSet](docs/IgnoreTermChangeSet.md)
 - [ManagerInvitation](docs/ManagerInvitation.md)
 - [MetadataCell](docs/MetadataCell.md)
 - [Metric](docs/Metric.md)
 - [Model](docs/Model.md)
 - [ModelAccess](docs/ModelAccess.md)
 - [ModelChangeSet](docs/ModelChangeSet.md)
 - [ModelGroup](docs/ModelGroup.md)
 - [ModelGroupInput](docs/ModelGroupInput.md)
 - [ModelInfo](docs/ModelInfo.md)
 - [ModelInput](docs/ModelInput.md)
 - [ModelInvitation](docs/ModelInvitation.md)
 - [ModelProjects](docs/ModelProjects.md)
 - [ModelUpdate](docs/ModelUpdate.md)
 - [ModelVersion](docs/ModelVersion.md)
 - [NetSentimentTimeseriesGraphContext](docs/NetSentimentTimeseriesGraphContext.md)
 - [NetSentimentTimeseriesGraphData](docs/NetSentimentTimeseriesGraphData.md)
 - [NetSentimentTimeseriesGraphResponse](docs/NetSentimentTimeseriesGraphResponse.md)
 - [NgramScore](docs/NgramScore.md)
 - [PendingPayment](docs/PendingPayment.md)
 - [Plugin](docs/Plugin.md)
 - [PluginDetails](docs/PluginDetails.md)
 - [Pole](docs/Pole.md)
 - [PolePart](docs/PolePart.md)
 - [PoleRequest](docs/PoleRequest.md)
 - [PoleSuggestion](docs/PoleSuggestion.md)
 - [PoleSuggestions](docs/PoleSuggestions.md)
 - [PolesResponse](docs/PolesResponse.md)
 - [ProductChangeResponse](docs/ProductChangeResponse.md)
 - [ProductPlan](docs/ProductPlan.md)
 - [ProductPlanUpdate](docs/ProductPlanUpdate.md)
 - [Project](docs/Project.md)
 - [ProjectDocumentTonalities](docs/ProjectDocumentTonalities.md)
 - [ProjectExplorationContext](docs/ProjectExplorationContext.md)
 - [ProjectExplorationResponse](docs/ProjectExplorationResponse.md)
 - [ProjectId](docs/ProjectId.md)
 - [ProjectInfo](docs/ProjectInfo.md)
 - [ProjectLanguage](docs/ProjectLanguage.md)
 - [ProjectReport](docs/ProjectReport.md)
 - [ProjectRequest](docs/ProjectRequest.md)
 - [ProjectSetting](docs/ProjectSetting.md)
 - [Row](docs/Row.md)
 - [RowsData](docs/RowsData.md)
 - [SelectedMetaData](docs/SelectedMetaData.md)
 - [Sentence](docs/Sentence.md)
 - [SentenceStatistics](docs/SentenceStatistics.md)
 - [Sentences](docs/Sentences.md)
 - [StoriesRequest](docs/StoriesRequest.md)
 - [StoriesResponse](docs/StoriesResponse.md)
 - [Story](docs/Story.md)
 - [Suggestion](docs/Suggestion.md)
 - [SuggestionsRequest](docs/SuggestionsRequest.md)
 - [SuggestionsResult](docs/SuggestionsResult.md)
 - [Survey](docs/Survey.md)
 - [SurveyInfo](docs/SurveyInfo.md)
 - [SynonymTerm](docs/SynonymTerm.md)
 - [TermDetails](docs/TermDetails.md)
 - [TermTonalityDetails](docs/TermTonalityDetails.md)
 - [TermsTonalityDetails](docs/TermsTonalityDetails.md)
 - [TimeseriesComparisonCurve](docs/TimeseriesComparisonCurve.md)
 - [TimeseriesComparisonCurveData](docs/TimeseriesComparisonCurveData.md)
 - [TimeseriesComparisonDataPoint](docs/TimeseriesComparisonDataPoint.md)
 - [TimeseriesComparisonGraphContext](docs/TimeseriesComparisonGraphContext.md)
 - [TimeseriesComparisonGraphData](docs/TimeseriesComparisonGraphData.md)
 - [TimeseriesComparisonGraphResponse](docs/TimeseriesComparisonGraphResponse.md)
 - [TonalitiesRequestContext](docs/TonalitiesRequestContext.md)
 - [TonalitiesResponse](docs/TonalitiesResponse.md)
 - [Tonality](docs/Tonality.md)
 - [TonalityContext](docs/TonalityContext.md)
 - [TonalityCustomization](docs/TonalityCustomization.md)
 - [TonalityCustomizationInfo](docs/TonalityCustomizationInfo.md)
 - [ToneCustomization](docs/ToneCustomization.md)
 - [ToneExcludeTerm](docs/ToneExcludeTerm.md)
 - [Topic](docs/Topic.md)
 - [TopicAssociation](docs/TopicAssociation.md)
 - [TopicAssociationWithAvgScore](docs/TopicAssociationWithAvgScore.md)
 - [TopicAssociationWithOccurrence](docs/TopicAssociationWithOccurrence.md)
 - [TopicAssociationsDataPoint](docs/TopicAssociationsDataPoint.md)
 - [TopicAssociationsGraphData](docs/TopicAssociationsGraphData.md)
 - [TopicAssociationsGraphResponse](docs/TopicAssociationsGraphResponse.md)
 - [TopicAverageScore](docs/TopicAverageScore.md)
 - [TopicAverageScoreMatrixGraphContext](docs/TopicAverageScoreMatrixGraphContext.md)
 - [TopicAverageScoreMatrixGraphData](docs/TopicAverageScoreMatrixGraphData.md)
 - [TopicAverageScoreMatrixGraphResponse](docs/TopicAverageScoreMatrixGraphResponse.md)
 - [TopicCell](docs/TopicCell.md)
 - [TopicChangeSet](docs/TopicChangeSet.md)
 - [TopicDefinition](docs/TopicDefinition.md)
 - [TopicGraphCreateRequest](docs/TopicGraphCreateRequest.md)
 - [TopicGraphData](docs/TopicGraphData.md)
 - [TopicGraphInfo](docs/TopicGraphInfo.md)
 - [TopicGraphInfoResponse](docs/TopicGraphInfoResponse.md)
 - [TopicGroupRequest](docs/TopicGroupRequest.md)
 - [TopicGroupResponse](docs/TopicGroupResponse.md)
 - [TopicHighImpact](docs/TopicHighImpact.md)
 - [TopicInformationGraphContext](docs/TopicInformationGraphContext.md)
 - [TopicInformationGraphData](docs/TopicInformationGraphData.md)
 - [TopicInformationGraphResponse](docs/TopicInformationGraphResponse.md)
 - [TopicInput](docs/TopicInput.md)
 - [TopicNetSentimentDataPoint](docs/TopicNetSentimentDataPoint.md)
 - [TopicRequest](docs/TopicRequest.md)
 - [TopicTerm](docs/TopicTerm.md)
 - [TopicTermChangeSet](docs/TopicTermChangeSet.md)
 - [TopicTextExamplesGraphContext](docs/TopicTextExamplesGraphContext.md)
 - [TopicTextExamplesGraphData](docs/TopicTextExamplesGraphData.md)
 - [TopicTextExamplesGraphResponse](docs/TopicTextExamplesGraphResponse.md)
 - [UsageDetail](docs/UsageDetail.md)
 - [UsageDetails](docs/UsageDetails.md)
 - [User](docs/User.md)
 - [UserCredits](docs/UserCredits.md)
 - [UserSetting](docs/UserSetting.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author




