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


class ProjectRequest(object):
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
        'title': 'str',
        'encoding': 'str',
        'settings': 'list[ProjectSetting]',
        'model_id': 'int'
    }

    attribute_map = {
        'title': 'title',
        'encoding': 'encoding',
        'settings': 'settings',
        'model_id': 'modelId'
    }

    def __init__(self, title=None, encoding=None, settings=None, model_id=None, local_vars_configuration=None):  # noqa: E501
        """ProjectRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._encoding = None
        self._settings = None
        self._model_id = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if encoding is not None:
            self.encoding = encoding
        if settings is not None:
            self.settings = settings
        if model_id is not None:
            self.model_id = model_id

    @property
    def title(self):
        """Gets the title of this ProjectRequest.  # noqa: E501


        :return: The title of this ProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectRequest.


        :param title: The title of this ProjectRequest.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def encoding(self):
        """Gets the encoding of this ProjectRequest.  # noqa: E501


        :return: The encoding of this ProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this ProjectRequest.


        :param encoding: The encoding of this ProjectRequest.  # noqa: E501
        :type encoding: str
        """

        self._encoding = encoding

    @property
    def settings(self):
        """Gets the settings of this ProjectRequest.  # noqa: E501


        :return: The settings of this ProjectRequest.  # noqa: E501
        :rtype: list[ProjectSetting]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ProjectRequest.


        :param settings: The settings of this ProjectRequest.  # noqa: E501
        :type settings: list[ProjectSetting]
        """

        self._settings = settings

    @property
    def model_id(self):
        """Gets the model_id of this ProjectRequest.  # noqa: E501


        :return: The model_id of this ProjectRequest.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ProjectRequest.


        :param model_id: The model_id of this ProjectRequest.  # noqa: E501
        :type model_id: int
        """

        self._model_id = model_id

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
        if not isinstance(other, ProjectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectRequest):
            return True

        return self.to_dict() != other.to_dict()
