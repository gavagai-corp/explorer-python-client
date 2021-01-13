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


class ConceptFilter(object):
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
        'inclusive': 'bool',
        'filtered': 'bool',
        'concept_id': 'int'
    }

    attribute_map = {
        'inclusive': 'inclusive',
        'filtered': 'filtered',
        'concept_id': 'conceptId'
    }

    def __init__(self, inclusive=None, filtered=None, concept_id=None, local_vars_configuration=None):  # noqa: E501
        """ConceptFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._inclusive = None
        self._filtered = None
        self._concept_id = None
        self.discriminator = None

        if inclusive is not None:
            self.inclusive = inclusive
        if filtered is not None:
            self.filtered = filtered
        if concept_id is not None:
            self.concept_id = concept_id

    @property
    def inclusive(self):
        """Gets the inclusive of this ConceptFilter.  # noqa: E501


        :return: The inclusive of this ConceptFilter.  # noqa: E501
        :rtype: bool
        """
        return self._inclusive

    @inclusive.setter
    def inclusive(self, inclusive):
        """Sets the inclusive of this ConceptFilter.


        :param inclusive: The inclusive of this ConceptFilter.  # noqa: E501
        :type inclusive: bool
        """

        self._inclusive = inclusive

    @property
    def filtered(self):
        """Gets the filtered of this ConceptFilter.  # noqa: E501


        :return: The filtered of this ConceptFilter.  # noqa: E501
        :rtype: bool
        """
        return self._filtered

    @filtered.setter
    def filtered(self, filtered):
        """Sets the filtered of this ConceptFilter.


        :param filtered: The filtered of this ConceptFilter.  # noqa: E501
        :type filtered: bool
        """

        self._filtered = filtered

    @property
    def concept_id(self):
        """Gets the concept_id of this ConceptFilter.  # noqa: E501


        :return: The concept_id of this ConceptFilter.  # noqa: E501
        :rtype: int
        """
        return self._concept_id

    @concept_id.setter
    def concept_id(self, concept_id):
        """Sets the concept_id of this ConceptFilter.


        :param concept_id: The concept_id of this ConceptFilter.  # noqa: E501
        :type concept_id: int
        """

        self._concept_id = concept_id

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
        if not isinstance(other, ConceptFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConceptFilter):
            return True

        return self.to_dict() != other.to_dict()