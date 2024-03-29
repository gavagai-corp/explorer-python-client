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


class TopicCell(object):
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
        'row_number': 'int',
        'text': 'str',
        'matching_topic_ids': 'list[int]',
        'metadata': 'list[MetadataCell]',
        'tonalities': 'list[CellTonality]'
    }

    attribute_map = {
        'row_number': 'rowNumber',
        'text': 'text',
        'matching_topic_ids': 'matchingTopicIds',
        'metadata': 'metadata',
        'tonalities': 'tonalities'
    }

    def __init__(self, row_number=None, text=None, matching_topic_ids=None, metadata=None, tonalities=None, local_vars_configuration=None):  # noqa: E501
        """TopicCell - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._row_number = None
        self._text = None
        self._matching_topic_ids = None
        self._metadata = None
        self._tonalities = None
        self.discriminator = None

        if row_number is not None:
            self.row_number = row_number
        if text is not None:
            self.text = text
        if matching_topic_ids is not None:
            self.matching_topic_ids = matching_topic_ids
        if metadata is not None:
            self.metadata = metadata
        if tonalities is not None:
            self.tonalities = tonalities

    @property
    def row_number(self):
        """Gets the row_number of this TopicCell.  # noqa: E501


        :return: The row_number of this TopicCell.  # noqa: E501
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """Sets the row_number of this TopicCell.


        :param row_number: The row_number of this TopicCell.  # noqa: E501
        :type row_number: int
        """

        self._row_number = row_number

    @property
    def text(self):
        """Gets the text of this TopicCell.  # noqa: E501


        :return: The text of this TopicCell.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TopicCell.


        :param text: The text of this TopicCell.  # noqa: E501
        :type text: str
        """

        self._text = text

    @property
    def matching_topic_ids(self):
        """Gets the matching_topic_ids of this TopicCell.  # noqa: E501


        :return: The matching_topic_ids of this TopicCell.  # noqa: E501
        :rtype: list[int]
        """
        return self._matching_topic_ids

    @matching_topic_ids.setter
    def matching_topic_ids(self, matching_topic_ids):
        """Sets the matching_topic_ids of this TopicCell.


        :param matching_topic_ids: The matching_topic_ids of this TopicCell.  # noqa: E501
        :type matching_topic_ids: list[int]
        """

        self._matching_topic_ids = matching_topic_ids

    @property
    def metadata(self):
        """Gets the metadata of this TopicCell.  # noqa: E501


        :return: The metadata of this TopicCell.  # noqa: E501
        :rtype: list[MetadataCell]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TopicCell.


        :param metadata: The metadata of this TopicCell.  # noqa: E501
        :type metadata: list[MetadataCell]
        """

        self._metadata = metadata

    @property
    def tonalities(self):
        """Gets the tonalities of this TopicCell.  # noqa: E501


        :return: The tonalities of this TopicCell.  # noqa: E501
        :rtype: list[CellTonality]
        """
        return self._tonalities

    @tonalities.setter
    def tonalities(self, tonalities):
        """Sets the tonalities of this TopicCell.


        :param tonalities: The tonalities of this TopicCell.  # noqa: E501
        :type tonalities: list[CellTonality]
        """

        self._tonalities = tonalities

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
        if not isinstance(other, TopicCell):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopicCell):
            return True

        return self.to_dict() != other.to_dict()
