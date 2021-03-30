# Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**created** | **int** |  | [optional] 
**created_by** | [**User**](User.md) |  | [optional] 
**groups** | [**list[ModelGroup]**](ModelGroup.md) |  | [optional] 
**users_access** | [**list[ModelAccess]**](ModelAccess.md) |  | [optional] 
**ignore_terms** | [**list[IgnoreTerm]**](IgnoreTerm.md) |  | [optional] 
**ignore_terms_dictionary** | **dict(str, str)** |  | [optional] 
**type** | **str** |  | [optional] 
**outdated** | **bool** |  | [optional] 
**language** | **str** |  | [optional] 
**project** | [**ProjectDetails**](ProjectDetails.md) |  | [optional] 
**drivers** | [**list[Driver]**](Driver.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


