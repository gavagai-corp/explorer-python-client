# coding: utf-8

"""
    Gavagai Explorer API

    <p>This is the technical documentation for the Gavagai Explorer API.</p><p>We recommend that you get familiar with using <a href=\"https://explorer.gavagai.se/\">Gavagai Explorer</a> before you start developing with the API. The Explorer has its own <a href=\"https://gavagai-corp.github.io/explorer/\"> general documentation</a>.</p><p>Make sure that you understand the basic procedures, such as creating projects and uploading texts, exploring and refining your project, or creating reports and applying models. All functionality in Gavagai Explorer is built on this API, so you will have a much easier time understanding the different steps if you have already seen them in the Explorer web interface.</p> <p>The <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/99319872/Gavagai+Explorer+API+Tutorial\">Getting Started</a> tutorial and the <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/322797577/Explorer+API+Common+Use+Cases\"> Common Use Cases </a>section provide more guidance in understanding how the different API calls can be fitted together to create a workflow. The documentation below then provides full technical specifics for each endpoint.</p>  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from explorer_client.configuration import Configuration


class ColumnHeader(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'header': 'str',
        'filterable': 'bool',
        'suggested_language': 'str',
        'column_data_size': 'int',
        'number_of_empty_cells': 'int',
        'time_series_candidate': 'bool',
        'suggested_for_analysis': 'bool',
        'npscandidate': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'header': 'header',
        'filterable': 'filterable',
        'suggested_language': 'suggestedLanguage',
        'column_data_size': 'columnDataSize',
        'number_of_empty_cells': 'numberOfEmptyCells',
        'time_series_candidate': 'timeSeriesCandidate',
        'suggested_for_analysis': 'suggestedForAnalysis',
        'npscandidate': 'npscandidate'
    }

    def __init__(self, id=None, header=None, filterable=None, suggested_language=None, column_data_size=None, number_of_empty_cells=None, time_series_candidate=None, suggested_for_analysis=None, npscandidate=None, local_vars_configuration=None):  # noqa: E501
        """ColumnHeader - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._header = None
        self._filterable = None
        self._suggested_language = None
        self._column_data_size = None
        self._number_of_empty_cells = None
        self._time_series_candidate = None
        self._suggested_for_analysis = None
        self._npscandidate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if header is not None:
            self.header = header
        if filterable is not None:
            self.filterable = filterable
        if suggested_language is not None:
            self.suggested_language = suggested_language
        if column_data_size is not None:
            self.column_data_size = column_data_size
        if number_of_empty_cells is not None:
            self.number_of_empty_cells = number_of_empty_cells
        if time_series_candidate is not None:
            self.time_series_candidate = time_series_candidate
        if suggested_for_analysis is not None:
            self.suggested_for_analysis = suggested_for_analysis
        if npscandidate is not None:
            self.npscandidate = npscandidate

    @property
    def id(self):
        """Gets the id of this ColumnHeader.  # noqa: E501


        :return: The id of this ColumnHeader.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ColumnHeader.


        :param id: The id of this ColumnHeader.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def header(self):
        """Gets the header of this ColumnHeader.  # noqa: E501


        :return: The header of this ColumnHeader.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this ColumnHeader.


        :param header: The header of this ColumnHeader.  # noqa: E501
        :type header: str
        """

        self._header = header

    @property
    def filterable(self):
        """Gets the filterable of this ColumnHeader.  # noqa: E501


        :return: The filterable of this ColumnHeader.  # noqa: E501
        :rtype: bool
        """
        return self._filterable

    @filterable.setter
    def filterable(self, filterable):
        """Sets the filterable of this ColumnHeader.


        :param filterable: The filterable of this ColumnHeader.  # noqa: E501
        :type filterable: bool
        """

        self._filterable = filterable

    @property
    def suggested_language(self):
        """Gets the suggested_language of this ColumnHeader.  # noqa: E501


        :return: The suggested_language of this ColumnHeader.  # noqa: E501
        :rtype: str
        """
        return self._suggested_language

    @suggested_language.setter
    def suggested_language(self, suggested_language):
        """Sets the suggested_language of this ColumnHeader.


        :param suggested_language: The suggested_language of this ColumnHeader.  # noqa: E501
        :type suggested_language: str
        """
        allowed_values = ["AA", "AB", "AE", "AF", "AK", "AM", "AN", "AR", "AS", "AV", "AY", "AZ", "BA", "BE", "BG", "BH", "BI", "BM", "BN", "BO", "BR", "BS", "CA", "CE", "CH", "CO", "CR", "CS", "CU", "CV", "CY", "DA", "DE", "DV", "DZ", "EE", "EL", "EN", "EO", "ES", "ET", "EU", "FA", "FF", "FI", "FJ", "FO", "FR", "FY", "GA", "GD", "GL", "GN", "GU", "GV", "HA", "HE", "HI", "HO", "HR", "HT", "HU", "HY", "HZ", "IA", "ID", "IE", "IG", "II", "IK", "IO", "IS", "IT", "IU", "JA", "JV", "KA", "KG", "KI", "KJ", "KK", "KL", "KM", "KN", "KO", "KR", "KS", "KU", "KV", "KW", "KY", "LA", "LB", "LG", "LI", "LN", "LO", "LT", "LU", "LV", "MG", "MH", "MI", "MK", "ML", "MN", "MR", "MS", "MT", "MY", "NA", "NB", "ND", "NE", "NG", "NL", "NN", "NO", "NR", "NV", "NY", "OC", "OJ", "OM", "OR", "OS", "PA", "PI", "PL", "PS", "PT", "QU", "RM", "RN", "RO", "RU", "RW", "SA", "SC", "SD", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SO", "SQ", "SR", "SS", "ST", "SU", "SV", "SW", "TA", "TE", "TG", "TH", "TI", "TK", "TL", "TN", "TO", "TR", "TS", "TT", "TW", "TY", "UG", "UK", "UR", "UZ", "VE", "VI", "VO", "WA", "WO", "XH", "YI", "YO", "ZA", "ZH", "ZH_CN", "ZH_TW", "ZU", "UNASSIGNED", "UNHANDLED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and suggested_language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `suggested_language` ({0}), must be one of {1}"  # noqa: E501
                .format(suggested_language, allowed_values)
            )

        self._suggested_language = suggested_language

    @property
    def column_data_size(self):
        """Gets the column_data_size of this ColumnHeader.  # noqa: E501


        :return: The column_data_size of this ColumnHeader.  # noqa: E501
        :rtype: int
        """
        return self._column_data_size

    @column_data_size.setter
    def column_data_size(self, column_data_size):
        """Sets the column_data_size of this ColumnHeader.


        :param column_data_size: The column_data_size of this ColumnHeader.  # noqa: E501
        :type column_data_size: int
        """

        self._column_data_size = column_data_size

    @property
    def number_of_empty_cells(self):
        """Gets the number_of_empty_cells of this ColumnHeader.  # noqa: E501


        :return: The number_of_empty_cells of this ColumnHeader.  # noqa: E501
        :rtype: int
        """
        return self._number_of_empty_cells

    @number_of_empty_cells.setter
    def number_of_empty_cells(self, number_of_empty_cells):
        """Sets the number_of_empty_cells of this ColumnHeader.


        :param number_of_empty_cells: The number_of_empty_cells of this ColumnHeader.  # noqa: E501
        :type number_of_empty_cells: int
        """

        self._number_of_empty_cells = number_of_empty_cells

    @property
    def time_series_candidate(self):
        """Gets the time_series_candidate of this ColumnHeader.  # noqa: E501


        :return: The time_series_candidate of this ColumnHeader.  # noqa: E501
        :rtype: bool
        """
        return self._time_series_candidate

    @time_series_candidate.setter
    def time_series_candidate(self, time_series_candidate):
        """Sets the time_series_candidate of this ColumnHeader.


        :param time_series_candidate: The time_series_candidate of this ColumnHeader.  # noqa: E501
        :type time_series_candidate: bool
        """

        self._time_series_candidate = time_series_candidate

    @property
    def suggested_for_analysis(self):
        """Gets the suggested_for_analysis of this ColumnHeader.  # noqa: E501


        :return: The suggested_for_analysis of this ColumnHeader.  # noqa: E501
        :rtype: bool
        """
        return self._suggested_for_analysis

    @suggested_for_analysis.setter
    def suggested_for_analysis(self, suggested_for_analysis):
        """Sets the suggested_for_analysis of this ColumnHeader.


        :param suggested_for_analysis: The suggested_for_analysis of this ColumnHeader.  # noqa: E501
        :type suggested_for_analysis: bool
        """

        self._suggested_for_analysis = suggested_for_analysis

    @property
    def npscandidate(self):
        """Gets the npscandidate of this ColumnHeader.  # noqa: E501


        :return: The npscandidate of this ColumnHeader.  # noqa: E501
        :rtype: bool
        """
        return self._npscandidate

    @npscandidate.setter
    def npscandidate(self, npscandidate):
        """Sets the npscandidate of this ColumnHeader.


        :param npscandidate: The npscandidate of this ColumnHeader.  # noqa: E501
        :type npscandidate: bool
        """

        self._npscandidate = npscandidate

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ColumnHeader):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ColumnHeader):
            return True

        return self.to_dict() != other.to_dict()