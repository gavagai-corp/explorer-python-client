# coding: utf-8

"""
    Gavagai Explorer API

    <p>This is the technical documentation for the Gavagai Explorer API.</p><p>We recommend that you get familiar with using <a href=\"https://explorer.gavagai.se/\">Gavagai Explorer</a> before you start developing with the API. The Explorer has its own <a href=\"https://gavagai-corp.github.io/explorer/\"> general documentation</a>.</p><p>Make sure that you understand the basic procedures, such as creating projects and uploading texts, exploring and refining your project, or creating reports and applying models. All functionality in Gavagai Explorer is built on this API, so you will have a much easier time understanding the different steps if you have already seen them in the Explorer web interface.</p> <p>The <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/99319872/Gavagai+Explorer+API+Tutorial\">Getting Started</a> tutorial and the <a href=\"https://gavagai.atlassian.net/wiki/spaces/PUB/pages/322797577/Explorer+API+Common+Use+Cases\"> Common Use Cases </a>section provide more guidance in understanding how the different API calls can be fitted together to create a workflow. The documentation below then provides full technical specifics for each endpoint.</p><p>Use <code>https://api.gavagai.se/explorer/v1/</code> as the Base URL for each of these API endpoints</p>  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from explorer_client.configuration import Configuration


class TopicAssociationsDataPoint(object):
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
        'date': 'int',
        'total_document_count': 'int',
        'associations': 'list[TopicAssociationWithAvgScore]'
    }

    attribute_map = {
        'date': 'date',
        'total_document_count': 'totalDocumentCount',
        'associations': 'associations'
    }

    def __init__(self, date=None, total_document_count=None, associations=None, local_vars_configuration=None):  # noqa: E501
        """TopicAssociationsDataPoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._total_document_count = None
        self._associations = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if total_document_count is not None:
            self.total_document_count = total_document_count
        if associations is not None:
            self.associations = associations

    @property
    def date(self):
        """Gets the date of this TopicAssociationsDataPoint.  # noqa: E501


        :return: The date of this TopicAssociationsDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TopicAssociationsDataPoint.


        :param date: The date of this TopicAssociationsDataPoint.  # noqa: E501
        :type date: int
        """

        self._date = date

    @property
    def total_document_count(self):
        """Gets the total_document_count of this TopicAssociationsDataPoint.  # noqa: E501


        :return: The total_document_count of this TopicAssociationsDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._total_document_count

    @total_document_count.setter
    def total_document_count(self, total_document_count):
        """Sets the total_document_count of this TopicAssociationsDataPoint.


        :param total_document_count: The total_document_count of this TopicAssociationsDataPoint.  # noqa: E501
        :type total_document_count: int
        """

        self._total_document_count = total_document_count

    @property
    def associations(self):
        """Gets the associations of this TopicAssociationsDataPoint.  # noqa: E501


        :return: The associations of this TopicAssociationsDataPoint.  # noqa: E501
        :rtype: list[TopicAssociationWithAvgScore]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this TopicAssociationsDataPoint.


        :param associations: The associations of this TopicAssociationsDataPoint.  # noqa: E501
        :type associations: list[TopicAssociationWithAvgScore]
        """

        self._associations = associations

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
        if not isinstance(other, TopicAssociationsDataPoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopicAssociationsDataPoint):
            return True

        return self.to_dict() != other.to_dict()
