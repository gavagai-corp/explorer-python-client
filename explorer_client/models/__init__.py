# coding: utf-8

# flake8: noqa
"""
    Gavagai Explorer API

    <p>This is the technical documentation for the Gavagai Explorer API.</p><p>We recommend that you get familiar with using <a href=\"https://explorer.gavagai.se/\">Gavagai Explorer</a> before you start developing with the API. The Explorer has its own <a href=\"https://gavagai-corp.github.io/explorer/\"> general documentation</a>.</p><p>Make sure that you understand the basic procedures, such as creating projects and uploading texts, exploring and refining your project, or creating reports and applying models. All functionality in Gavagai Explorer is built on this API, so you will have a much easier time understanding the different steps if you have already seen them in the Explorer web interface.</p> <p>The <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/99319872/Gavagai+Explorer+API+Tutorial\">Getting Started</a> tutorial and the <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/322797577/Explorer+API+Common+Use+Cases\"> Common Use Cases </a>section provide more guidance in understanding how the different API calls can be fitted together to create a workflow. The documentation below then provides full technical specifics for each endpoint.</p><p>Use <code>https://api.gavagai.se/explorer/v1/</code> as the Base URL for each of these API endpoints</p>  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from explorer_client.models.account import Account
from explorer_client.models.account_balance import AccountBalance
from explorer_client.models.account_reactivation_request import AccountReactivationRequest
from explorer_client.models.account_reactivation_response import AccountReactivationResponse
from explorer_client.models.apply_model_request import ApplyModelRequest
from explorer_client.models.associations_timeseries_graph_context import AssociationsTimeseriesGraphContext
from explorer_client.models.associations_timeseries_graph_data import AssociationsTimeseriesGraphData
from explorer_client.models.associations_timeseries_graph_response import AssociationsTimeseriesGraphResponse
from explorer_client.models.auto_add_term import AutoAddTerm
from explorer_client.models.average_score_graph_context import AverageScoreGraphContext
from explorer_client.models.average_score_graph_data import AverageScoreGraphData
from explorer_client.models.average_score_graph_response import AverageScoreGraphResponse
from explorer_client.models.average_score_matrix_graph_context import AverageScoreMatrixGraphContext
from explorer_client.models.average_score_matrix_graph_data import AverageScoreMatrixGraphData
from explorer_client.models.average_score_matrix_graph_response import AverageScoreMatrixGraphResponse
from explorer_client.models.batch_id import BatchId
from explorer_client.models.batch_request import BatchRequest
from explorer_client.models.batch_response import BatchResponse
from explorer_client.models.batch_text_request import BatchTextRequest
from explorer_client.models.batch_text_response import BatchTextResponse
from explorer_client.models.batch_text_tonality import BatchTextTonality
from explorer_client.models.batch_topic_definition import BatchTopicDefinition
from explorer_client.models.cell_tonality import CellTonality
from explorer_client.models.cell_topic_information import CellTopicInformation
from explorer_client.models.column_header import ColumnHeader
from explorer_client.models.column_header_update import ColumnHeaderUpdate
from explorer_client.models.comparison_graph_context import ComparisonGraphContext
from explorer_client.models.comparison_layer import ComparisonLayer
from explorer_client.models.compiled_graph_data import CompiledGraphData
from explorer_client.models.compiled_topic_graph_data import CompiledTopicGraphData
from explorer_client.models.concept_filter import ConceptFilter
from explorer_client.models.coverage_statistics import CoverageStatistics
from explorer_client.models.create_graph_request import CreateGraphRequest
from explorer_client.models.credit_price import CreditPrice
from explorer_client.models.credit_purchase import CreditPurchase
from explorer_client.models.credit_purchase_response import CreditPurchaseResponse
from explorer_client.models.credit_statistics import CreditStatistics
from explorer_client.models.credits_history_data_point import CreditsHistoryDataPoint
from explorer_client.models.custom_tone_term import CustomToneTerm
from explorer_client.models.data_segment import DataSegment
from explorer_client.models.document_reference import DocumentReference
from explorer_client.models.document_sentences import DocumentSentences
from explorer_client.models.driver import Driver
from explorer_client.models.driver_change_set import DriverChangeSet
from explorer_client.models.driver_definition import DriverDefinition
from explorer_client.models.driver_request import DriverRequest
from explorer_client.models.driver_response import DriverResponse
from explorer_client.models.exploration_status import ExplorationStatus
from explorer_client.models.file_details import FileDetails
from explorer_client.models.filter import Filter
from explorer_client.models.filter_validation import FilterValidation
from explorer_client.models.folder_information import FolderInformation
from explorer_client.models.folder_request import FolderRequest
from explorer_client.models.folder_structure import FolderStructure
from explorer_client.models.graph_data import GraphData
from explorer_client.models.graph_data_progress import GraphDataProgress
from explorer_client.models.graph_info import GraphInfo
from explorer_client.models.graph_info_response import GraphInfoResponse
from explorer_client.models.group_change_set import GroupChangeSet
from explorer_client.models.group_definition import GroupDefinition
from explorer_client.models.grouped_comparison_data_point import GroupedComparisonDataPoint
from explorer_client.models.grouped_comparison_graph_context import GroupedComparisonGraphContext
from explorer_client.models.grouped_comparison_graph_data import GroupedComparisonGraphData
from explorer_client.models.grouped_comparison_graph_response import GroupedComparisonGraphResponse
from explorer_client.models.header_row import HeaderRow
from explorer_client.models.health_check_report import HealthCheckReport
from explorer_client.models.health_check_result import HealthCheckResult
from explorer_client.models.high_impact_associations_graph_context import HighImpactAssociationsGraphContext
from explorer_client.models.high_impact_associations_graph_data import HighImpactAssociationsGraphData
from explorer_client.models.high_impact_associations_graph_response import HighImpactAssociationsGraphResponse
from explorer_client.models.high_impact_graph_context import HighImpactGraphContext
from explorer_client.models.high_impact_graph_data import HighImpactGraphData
from explorer_client.models.high_impact_graph_response import HighImpactGraphResponse
from explorer_client.models.high_impact_topic_association import HighImpactTopicAssociation
from explorer_client.models.high_impact_topic_associations_graph_data import HighImpactTopicAssociationsGraphData
from explorer_client.models.history_log import HistoryLog
from explorer_client.models.ignore_term import IgnoreTerm
from explorer_client.models.ignore_term_change_set import IgnoreTermChangeSet
from explorer_client.models.manager_invitation import ManagerInvitation
from explorer_client.models.metadata_cell import MetadataCell
from explorer_client.models.metric import Metric
from explorer_client.models.model import Model
from explorer_client.models.model_access import ModelAccess
from explorer_client.models.model_change_set import ModelChangeSet
from explorer_client.models.model_group import ModelGroup
from explorer_client.models.model_info import ModelInfo
from explorer_client.models.model_input import ModelInput
from explorer_client.models.model_translation_candidates import ModelTranslationCandidates
from explorer_client.models.model_update import ModelUpdate
from explorer_client.models.model_version import ModelVersion
from explorer_client.models.model_version_update import ModelVersionUpdate
from explorer_client.models.model_versions_change_set import ModelVersionsChangeSet
from explorer_client.models.net_sentiment_timeseries_graph_context import NetSentimentTimeseriesGraphContext
from explorer_client.models.net_sentiment_timeseries_graph_data import NetSentimentTimeseriesGraphData
from explorer_client.models.net_sentiment_timeseries_graph_response import NetSentimentTimeseriesGraphResponse
from explorer_client.models.ngram_score import NgramScore
from explorer_client.models.pending_payment import PendingPayment
from explorer_client.models.plugin import Plugin
from explorer_client.models.plugin_details import PluginDetails
from explorer_client.models.pole import Pole
from explorer_client.models.pole_part import PolePart
from explorer_client.models.pole_request import PoleRequest
from explorer_client.models.pole_suggestion import PoleSuggestion
from explorer_client.models.pole_suggestions import PoleSuggestions
from explorer_client.models.poles_response import PolesResponse
from explorer_client.models.product_change_response import ProductChangeResponse
from explorer_client.models.product_plan import ProductPlan
from explorer_client.models.product_plan_update import ProductPlanUpdate
from explorer_client.models.project import Project
from explorer_client.models.project_details import ProjectDetails
from explorer_client.models.project_document_tonalities import ProjectDocumentTonalities
from explorer_client.models.project_exploration_context import ProjectExplorationContext
from explorer_client.models.project_exploration_response import ProjectExplorationResponse
from explorer_client.models.project_id import ProjectId
from explorer_client.models.project_info import ProjectInfo
from explorer_client.models.project_language import ProjectLanguage
from explorer_client.models.project_report import ProjectReport
from explorer_client.models.project_request import ProjectRequest
from explorer_client.models.project_setting import ProjectSetting
from explorer_client.models.project_version import ProjectVersion
from explorer_client.models.project_version_update import ProjectVersionUpdate
from explorer_client.models.project_versions_change_set import ProjectVersionsChangeSet
from explorer_client.models.row import Row
from explorer_client.models.rows_data import RowsData
from explorer_client.models.selected_meta_data import SelectedMetaData
from explorer_client.models.sentence import Sentence
from explorer_client.models.sentence_statistics import SentenceStatistics
from explorer_client.models.sentences import Sentences
from explorer_client.models.stories_request import StoriesRequest
from explorer_client.models.stories_response import StoriesResponse
from explorer_client.models.story import Story
from explorer_client.models.subscribed_model import SubscribedModel
from explorer_client.models.suggestion import Suggestion
from explorer_client.models.suggestions_request import SuggestionsRequest
from explorer_client.models.suggestions_result import SuggestionsResult
from explorer_client.models.survey import Survey
from explorer_client.models.survey_info import SurveyInfo
from explorer_client.models.synonym_term import SynonymTerm
from explorer_client.models.term_details import TermDetails
from explorer_client.models.term_tonality_details import TermTonalityDetails
from explorer_client.models.terms_tonality_details import TermsTonalityDetails
from explorer_client.models.timeseries_comparison_curve import TimeseriesComparisonCurve
from explorer_client.models.timeseries_comparison_curve_data import TimeseriesComparisonCurveData
from explorer_client.models.timeseries_comparison_data_point import TimeseriesComparisonDataPoint
from explorer_client.models.timeseries_comparison_graph_context import TimeseriesComparisonGraphContext
from explorer_client.models.timeseries_comparison_graph_data import TimeseriesComparisonGraphData
from explorer_client.models.timeseries_comparison_graph_response import TimeseriesComparisonGraphResponse
from explorer_client.models.tonalities_request_context import TonalitiesRequestContext
from explorer_client.models.tonalities_response import TonalitiesResponse
from explorer_client.models.tonality import Tonality
from explorer_client.models.tonality_context import TonalityContext
from explorer_client.models.tonality_customization import TonalityCustomization
from explorer_client.models.tonality_customization_info import TonalityCustomizationInfo
from explorer_client.models.tonality_customization_request import TonalityCustomizationRequest
from explorer_client.models.tone_customization import ToneCustomization
from explorer_client.models.tone_exclude_term import ToneExcludeTerm
from explorer_client.models.topic import Topic
from explorer_client.models.topic_association import TopicAssociation
from explorer_client.models.topic_association_with_avg_score import TopicAssociationWithAvgScore
from explorer_client.models.topic_association_with_occurrence import TopicAssociationWithOccurrence
from explorer_client.models.topic_associations_data_point import TopicAssociationsDataPoint
from explorer_client.models.topic_associations_graph_data import TopicAssociationsGraphData
from explorer_client.models.topic_associations_graph_response import TopicAssociationsGraphResponse
from explorer_client.models.topic_average_score import TopicAverageScore
from explorer_client.models.topic_average_score_matrix_graph_context import TopicAverageScoreMatrixGraphContext
from explorer_client.models.topic_average_score_matrix_graph_data import TopicAverageScoreMatrixGraphData
from explorer_client.models.topic_average_score_matrix_graph_response import TopicAverageScoreMatrixGraphResponse
from explorer_client.models.topic_cell import TopicCell
from explorer_client.models.topic_change_set import TopicChangeSet
from explorer_client.models.topic_definition import TopicDefinition
from explorer_client.models.topic_graph_create_request import TopicGraphCreateRequest
from explorer_client.models.topic_graph_data import TopicGraphData
from explorer_client.models.topic_graph_info import TopicGraphInfo
from explorer_client.models.topic_graph_info_response import TopicGraphInfoResponse
from explorer_client.models.topic_group_request import TopicGroupRequest
from explorer_client.models.topic_group_response import TopicGroupResponse
from explorer_client.models.topic_high_impact import TopicHighImpact
from explorer_client.models.topic_information_graph_context import TopicInformationGraphContext
from explorer_client.models.topic_information_graph_data import TopicInformationGraphData
from explorer_client.models.topic_information_graph_response import TopicInformationGraphResponse
from explorer_client.models.topic_net_sentiment_data_point import TopicNetSentimentDataPoint
from explorer_client.models.topic_request import TopicRequest
from explorer_client.models.topic_term import TopicTerm
from explorer_client.models.topic_term_change_set import TopicTermChangeSet
from explorer_client.models.topic_text_examples_graph_context import TopicTextExamplesGraphContext
from explorer_client.models.topic_text_examples_graph_data import TopicTextExamplesGraphData
from explorer_client.models.topic_text_examples_graph_response import TopicTextExamplesGraphResponse
from explorer_client.models.usage_detail import UsageDetail
from explorer_client.models.usage_details import UsageDetails
from explorer_client.models.user import User
from explorer_client.models.user_credits import UserCredits
from explorer_client.models.user_setting import UserSetting
