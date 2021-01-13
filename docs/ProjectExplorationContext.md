# ProjectExplorationContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language in the chosen column. Should be an iso code from the list of supported languages that can be found at developer.gavagai.se | 
**ignore_terms** | **list[str]** | The terms to be ignored. These will not be considered as candidates for topics, although they   * can still become associations. | [optional] 
**column_header_id** | **int** | The id of the columnHeader that you wish to analyze. This should be one of the columns of the project | 
**filters** | [**list[Filter]**](Filter.md) | You may filter using columns other than the one which is being analyzed. Supply filters here as specified in the Filter type | [optional] 
**concept_filter** | [**ConceptFilter**](ConceptFilter.md) |  | [optional] 
**groups** | [**list[TopicGroupRequest]**](TopicGroupRequest.md) | Specify your groups here. It is necessary to specify a group in this list if it has been modified in any way, such as if it is pinned or its title has been changed. You may send in other groups as well without adverse effects. | [optional] 
**tonality_customization_id** | **int** | Specify which tonality customization while performing tonality calculation use in the context of the exploration | [optional] 
**drivers** | [**list[DriverRequest]**](DriverRequest.md) |  | [optional] 
**filter_by_language** | **bool** | An indicator of whether the data considered for exploration should filtered by the selected language. Defaults to false. | [optional] 
**query_filter** | **bool** | If set to true, the project will be filtered to only contain queries i.e sentences that ends with a ? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


