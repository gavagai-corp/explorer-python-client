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


class TimeseriesComparisonCurve(object):
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
        'selected_topic_id': 'int',
        'selected_layers': 'list[ComparisonLayer]',
        'title': 'str'
    }

    attribute_map = {
        'selected_topic_id': 'selectedTopicId',
        'selected_layers': 'selectedLayers',
        'title': 'title'
    }

    def __init__(self, selected_topic_id=None, selected_layers=None, title=None, local_vars_configuration=None):  # noqa: E501
        """TimeseriesComparisonCurve - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._selected_topic_id = None
        self._selected_layers = None
        self._title = None
        self.discriminator = None

        if selected_topic_id is not None:
            self.selected_topic_id = selected_topic_id
        if selected_layers is not None:
            self.selected_layers = selected_layers
        if title is not None:
            self.title = title

    @property
    def selected_topic_id(self):
        """Gets the selected_topic_id of this TimeseriesComparisonCurve.  # noqa: E501


        :return: The selected_topic_id of this TimeseriesComparisonCurve.  # noqa: E501
        :rtype: int
        """
        return self._selected_topic_id

    @selected_topic_id.setter
    def selected_topic_id(self, selected_topic_id):
        """Sets the selected_topic_id of this TimeseriesComparisonCurve.


        :param selected_topic_id: The selected_topic_id of this TimeseriesComparisonCurve.  # noqa: E501
        :type selected_topic_id: int
        """

        self._selected_topic_id = selected_topic_id

    @property
    def selected_layers(self):
        """Gets the selected_layers of this TimeseriesComparisonCurve.  # noqa: E501


        :return: The selected_layers of this TimeseriesComparisonCurve.  # noqa: E501
        :rtype: list[ComparisonLayer]
        """
        return self._selected_layers

    @selected_layers.setter
    def selected_layers(self, selected_layers):
        """Sets the selected_layers of this TimeseriesComparisonCurve.


        :param selected_layers: The selected_layers of this TimeseriesComparisonCurve.  # noqa: E501
        :type selected_layers: list[ComparisonLayer]
        """

        self._selected_layers = selected_layers

    @property
    def title(self):
        """Gets the title of this TimeseriesComparisonCurve.  # noqa: E501


        :return: The title of this TimeseriesComparisonCurve.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TimeseriesComparisonCurve.


        :param title: The title of this TimeseriesComparisonCurve.  # noqa: E501
        :type title: str
        """

        self._title = title

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
        if not isinstance(other, TimeseriesComparisonCurve):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeseriesComparisonCurve):
            return True

        return self.to_dict() != other.to_dict()