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


class AverageScoreMatrixGraphData(object):
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
        'topics': 'list[TopicAverageScore]',
        'average_score_across_topics': 'float',
        'average_occurrence': 'float'
    }

    attribute_map = {
        'topics': 'topics',
        'average_score_across_topics': 'averageScoreAcrossTopics',
        'average_occurrence': 'averageOccurrence'
    }

    def __init__(self, topics=None, average_score_across_topics=None, average_occurrence=None, local_vars_configuration=None):  # noqa: E501
        """AverageScoreMatrixGraphData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._topics = None
        self._average_score_across_topics = None
        self._average_occurrence = None
        self.discriminator = None

        if topics is not None:
            self.topics = topics
        if average_score_across_topics is not None:
            self.average_score_across_topics = average_score_across_topics
        if average_occurrence is not None:
            self.average_occurrence = average_occurrence

    @property
    def topics(self):
        """Gets the topics of this AverageScoreMatrixGraphData.  # noqa: E501


        :return: The topics of this AverageScoreMatrixGraphData.  # noqa: E501
        :rtype: list[TopicAverageScore]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this AverageScoreMatrixGraphData.


        :param topics: The topics of this AverageScoreMatrixGraphData.  # noqa: E501
        :type topics: list[TopicAverageScore]
        """

        self._topics = topics

    @property
    def average_score_across_topics(self):
        """Gets the average_score_across_topics of this AverageScoreMatrixGraphData.  # noqa: E501


        :return: The average_score_across_topics of this AverageScoreMatrixGraphData.  # noqa: E501
        :rtype: float
        """
        return self._average_score_across_topics

    @average_score_across_topics.setter
    def average_score_across_topics(self, average_score_across_topics):
        """Sets the average_score_across_topics of this AverageScoreMatrixGraphData.


        :param average_score_across_topics: The average_score_across_topics of this AverageScoreMatrixGraphData.  # noqa: E501
        :type average_score_across_topics: float
        """

        self._average_score_across_topics = average_score_across_topics

    @property
    def average_occurrence(self):
        """Gets the average_occurrence of this AverageScoreMatrixGraphData.  # noqa: E501


        :return: The average_occurrence of this AverageScoreMatrixGraphData.  # noqa: E501
        :rtype: float
        """
        return self._average_occurrence

    @average_occurrence.setter
    def average_occurrence(self, average_occurrence):
        """Sets the average_occurrence of this AverageScoreMatrixGraphData.


        :param average_occurrence: The average_occurrence of this AverageScoreMatrixGraphData.  # noqa: E501
        :type average_occurrence: float
        """

        self._average_occurrence = average_occurrence

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
        if not isinstance(other, AverageScoreMatrixGraphData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AverageScoreMatrixGraphData):
            return True

        return self.to_dict() != other.to_dict()
