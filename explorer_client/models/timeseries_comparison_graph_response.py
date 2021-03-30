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


class TimeseriesComparisonGraphResponse(object):
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
        'graph_id': 'str',
        'context': 'TimeseriesComparisonGraphContext',
        'data': 'TimeseriesComparisonGraphData',
        'progress': 'GraphDataProgress'
    }

    attribute_map = {
        'graph_id': 'graphId',
        'context': 'context',
        'data': 'data',
        'progress': 'progress'
    }

    def __init__(self, graph_id=None, context=None, data=None, progress=None, local_vars_configuration=None):  # noqa: E501
        """TimeseriesComparisonGraphResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._graph_id = None
        self._context = None
        self._data = None
        self._progress = None
        self.discriminator = None

        if graph_id is not None:
            self.graph_id = graph_id
        if context is not None:
            self.context = context
        if data is not None:
            self.data = data
        if progress is not None:
            self.progress = progress

    @property
    def graph_id(self):
        """Gets the graph_id of this TimeseriesComparisonGraphResponse.  # noqa: E501


        :return: The graph_id of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        """Sets the graph_id of this TimeseriesComparisonGraphResponse.


        :param graph_id: The graph_id of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :type graph_id: str
        """

        self._graph_id = graph_id

    @property
    def context(self):
        """Gets the context of this TimeseriesComparisonGraphResponse.  # noqa: E501


        :return: The context of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :rtype: TimeseriesComparisonGraphContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this TimeseriesComparisonGraphResponse.


        :param context: The context of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :type context: TimeseriesComparisonGraphContext
        """

        self._context = context

    @property
    def data(self):
        """Gets the data of this TimeseriesComparisonGraphResponse.  # noqa: E501


        :return: The data of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :rtype: TimeseriesComparisonGraphData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TimeseriesComparisonGraphResponse.


        :param data: The data of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :type data: TimeseriesComparisonGraphData
        """

        self._data = data

    @property
    def progress(self):
        """Gets the progress of this TimeseriesComparisonGraphResponse.  # noqa: E501


        :return: The progress of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :rtype: GraphDataProgress
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this TimeseriesComparisonGraphResponse.


        :param progress: The progress of this TimeseriesComparisonGraphResponse.  # noqa: E501
        :type progress: GraphDataProgress
        """

        self._progress = progress

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
        if not isinstance(other, TimeseriesComparisonGraphResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeseriesComparisonGraphResponse):
            return True

        return self.to_dict() != other.to_dict()
