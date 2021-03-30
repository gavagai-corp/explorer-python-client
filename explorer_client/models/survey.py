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


class Survey(object):
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
        'id': 'str',
        'title': 'str',
        'nickname': 'str',
        'language': 'str',
        'question_count': 'int',
        'page_count': 'int',
        'response_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'nickname': 'nickname',
        'language': 'language',
        'question_count': 'questionCount',
        'page_count': 'pageCount',
        'response_count': 'responseCount'
    }

    def __init__(self, id=None, title=None, nickname=None, language=None, question_count=None, page_count=None, response_count=None, local_vars_configuration=None):  # noqa: E501
        """Survey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._nickname = None
        self._language = None
        self._question_count = None
        self._page_count = None
        self._response_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if nickname is not None:
            self.nickname = nickname
        if language is not None:
            self.language = language
        if question_count is not None:
            self.question_count = question_count
        if page_count is not None:
            self.page_count = page_count
        if response_count is not None:
            self.response_count = response_count

    @property
    def id(self):
        """Gets the id of this Survey.  # noqa: E501


        :return: The id of this Survey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Survey.


        :param id: The id of this Survey.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Survey.  # noqa: E501


        :return: The title of this Survey.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Survey.


        :param title: The title of this Survey.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def nickname(self):
        """Gets the nickname of this Survey.  # noqa: E501


        :return: The nickname of this Survey.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this Survey.


        :param nickname: The nickname of this Survey.  # noqa: E501
        :type nickname: str
        """

        self._nickname = nickname

    @property
    def language(self):
        """Gets the language of this Survey.  # noqa: E501


        :return: The language of this Survey.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Survey.


        :param language: The language of this Survey.  # noqa: E501
        :type language: str
        """

        self._language = language

    @property
    def question_count(self):
        """Gets the question_count of this Survey.  # noqa: E501


        :return: The question_count of this Survey.  # noqa: E501
        :rtype: int
        """
        return self._question_count

    @question_count.setter
    def question_count(self, question_count):
        """Sets the question_count of this Survey.


        :param question_count: The question_count of this Survey.  # noqa: E501
        :type question_count: int
        """

        self._question_count = question_count

    @property
    def page_count(self):
        """Gets the page_count of this Survey.  # noqa: E501


        :return: The page_count of this Survey.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this Survey.


        :param page_count: The page_count of this Survey.  # noqa: E501
        :type page_count: int
        """

        self._page_count = page_count

    @property
    def response_count(self):
        """Gets the response_count of this Survey.  # noqa: E501


        :return: The response_count of this Survey.  # noqa: E501
        :rtype: int
        """
        return self._response_count

    @response_count.setter
    def response_count(self, response_count):
        """Sets the response_count of this Survey.


        :param response_count: The response_count of this Survey.  # noqa: E501
        :type response_count: int
        """

        self._response_count = response_count

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
        if not isinstance(other, Survey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Survey):
            return True

        return self.to_dict() != other.to_dict()
