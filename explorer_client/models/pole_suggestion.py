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


class PoleSuggestion(object):
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
        'term': 'str',
        'sum_cosine': 'float',
        'cosine': 'float',
        'frequency': 'int',
        'neighbour_counter': 'int',
        'for_word': 'str',
        'string_similarity': 'bool',
        'reciprocal': 'bool'
    }

    attribute_map = {
        'term': 'term',
        'sum_cosine': 'sumCosine',
        'cosine': 'cosine',
        'frequency': 'frequency',
        'neighbour_counter': 'neighbourCounter',
        'for_word': 'forWord',
        'string_similarity': 'stringSimilarity',
        'reciprocal': 'reciprocal'
    }

    def __init__(self, term=None, sum_cosine=None, cosine=None, frequency=None, neighbour_counter=None, for_word=None, string_similarity=None, reciprocal=None, local_vars_configuration=None):  # noqa: E501
        """PoleSuggestion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._term = None
        self._sum_cosine = None
        self._cosine = None
        self._frequency = None
        self._neighbour_counter = None
        self._for_word = None
        self._string_similarity = None
        self._reciprocal = None
        self.discriminator = None

        if term is not None:
            self.term = term
        if sum_cosine is not None:
            self.sum_cosine = sum_cosine
        if cosine is not None:
            self.cosine = cosine
        if frequency is not None:
            self.frequency = frequency
        if neighbour_counter is not None:
            self.neighbour_counter = neighbour_counter
        if for_word is not None:
            self.for_word = for_word
        if string_similarity is not None:
            self.string_similarity = string_similarity
        if reciprocal is not None:
            self.reciprocal = reciprocal

    @property
    def term(self):
        """Gets the term of this PoleSuggestion.  # noqa: E501


        :return: The term of this PoleSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this PoleSuggestion.


        :param term: The term of this PoleSuggestion.  # noqa: E501
        :type term: str
        """

        self._term = term

    @property
    def sum_cosine(self):
        """Gets the sum_cosine of this PoleSuggestion.  # noqa: E501


        :return: The sum_cosine of this PoleSuggestion.  # noqa: E501
        :rtype: float
        """
        return self._sum_cosine

    @sum_cosine.setter
    def sum_cosine(self, sum_cosine):
        """Sets the sum_cosine of this PoleSuggestion.


        :param sum_cosine: The sum_cosine of this PoleSuggestion.  # noqa: E501
        :type sum_cosine: float
        """

        self._sum_cosine = sum_cosine

    @property
    def cosine(self):
        """Gets the cosine of this PoleSuggestion.  # noqa: E501


        :return: The cosine of this PoleSuggestion.  # noqa: E501
        :rtype: float
        """
        return self._cosine

    @cosine.setter
    def cosine(self, cosine):
        """Sets the cosine of this PoleSuggestion.


        :param cosine: The cosine of this PoleSuggestion.  # noqa: E501
        :type cosine: float
        """

        self._cosine = cosine

    @property
    def frequency(self):
        """Gets the frequency of this PoleSuggestion.  # noqa: E501


        :return: The frequency of this PoleSuggestion.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PoleSuggestion.


        :param frequency: The frequency of this PoleSuggestion.  # noqa: E501
        :type frequency: int
        """

        self._frequency = frequency

    @property
    def neighbour_counter(self):
        """Gets the neighbour_counter of this PoleSuggestion.  # noqa: E501


        :return: The neighbour_counter of this PoleSuggestion.  # noqa: E501
        :rtype: int
        """
        return self._neighbour_counter

    @neighbour_counter.setter
    def neighbour_counter(self, neighbour_counter):
        """Sets the neighbour_counter of this PoleSuggestion.


        :param neighbour_counter: The neighbour_counter of this PoleSuggestion.  # noqa: E501
        :type neighbour_counter: int
        """

        self._neighbour_counter = neighbour_counter

    @property
    def for_word(self):
        """Gets the for_word of this PoleSuggestion.  # noqa: E501


        :return: The for_word of this PoleSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._for_word

    @for_word.setter
    def for_word(self, for_word):
        """Sets the for_word of this PoleSuggestion.


        :param for_word: The for_word of this PoleSuggestion.  # noqa: E501
        :type for_word: str
        """

        self._for_word = for_word

    @property
    def string_similarity(self):
        """Gets the string_similarity of this PoleSuggestion.  # noqa: E501


        :return: The string_similarity of this PoleSuggestion.  # noqa: E501
        :rtype: bool
        """
        return self._string_similarity

    @string_similarity.setter
    def string_similarity(self, string_similarity):
        """Sets the string_similarity of this PoleSuggestion.


        :param string_similarity: The string_similarity of this PoleSuggestion.  # noqa: E501
        :type string_similarity: bool
        """

        self._string_similarity = string_similarity

    @property
    def reciprocal(self):
        """Gets the reciprocal of this PoleSuggestion.  # noqa: E501


        :return: The reciprocal of this PoleSuggestion.  # noqa: E501
        :rtype: bool
        """
        return self._reciprocal

    @reciprocal.setter
    def reciprocal(self, reciprocal):
        """Sets the reciprocal of this PoleSuggestion.


        :param reciprocal: The reciprocal of this PoleSuggestion.  # noqa: E501
        :type reciprocal: bool
        """

        self._reciprocal = reciprocal

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
        if not isinstance(other, PoleSuggestion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PoleSuggestion):
            return True

        return self.to_dict() != other.to_dict()
