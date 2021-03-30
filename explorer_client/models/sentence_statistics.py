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


class SentenceStatistics(object):
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
        'text': 'str',
        'score': 'float',
        'ngrams': 'list[NgramScore]',
        'terms': 'list[str]'
    }

    attribute_map = {
        'text': 'text',
        'score': 'score',
        'ngrams': 'ngrams',
        'terms': 'terms'
    }

    def __init__(self, text=None, score=None, ngrams=None, terms=None, local_vars_configuration=None):  # noqa: E501
        """SentenceStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text = None
        self._score = None
        self._ngrams = None
        self._terms = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if score is not None:
            self.score = score
        if ngrams is not None:
            self.ngrams = ngrams
        if terms is not None:
            self.terms = terms

    @property
    def text(self):
        """Gets the text of this SentenceStatistics.  # noqa: E501


        :return: The text of this SentenceStatistics.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SentenceStatistics.


        :param text: The text of this SentenceStatistics.  # noqa: E501
        :type text: str
        """

        self._text = text

    @property
    def score(self):
        """Gets the score of this SentenceStatistics.  # noqa: E501


        :return: The score of this SentenceStatistics.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this SentenceStatistics.


        :param score: The score of this SentenceStatistics.  # noqa: E501
        :type score: float
        """

        self._score = score

    @property
    def ngrams(self):
        """Gets the ngrams of this SentenceStatistics.  # noqa: E501


        :return: The ngrams of this SentenceStatistics.  # noqa: E501
        :rtype: list[NgramScore]
        """
        return self._ngrams

    @ngrams.setter
    def ngrams(self, ngrams):
        """Sets the ngrams of this SentenceStatistics.


        :param ngrams: The ngrams of this SentenceStatistics.  # noqa: E501
        :type ngrams: list[NgramScore]
        """

        self._ngrams = ngrams

    @property
    def terms(self):
        """Gets the terms of this SentenceStatistics.  # noqa: E501


        :return: The terms of this SentenceStatistics.  # noqa: E501
        :rtype: list[str]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this SentenceStatistics.


        :param terms: The terms of this SentenceStatistics.  # noqa: E501
        :type terms: list[str]
        """

        self._terms = terms

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
        if not isinstance(other, SentenceStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SentenceStatistics):
            return True

        return self.to_dict() != other.to_dict()
