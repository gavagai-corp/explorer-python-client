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


class TopicChangeSet(object):
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
        'change_type': 'str',
        'renamed_from': 'str',
        'added_terms': 'list[TopicTermChangeSet]',
        'removed_terms': 'list[TopicTermChangeSet]'
    }

    attribute_map = {
        'title': 'title',
        'change_type': 'changeType',
        'renamed_from': 'renamedFrom',
        'added_terms': 'addedTerms',
        'removed_terms': 'removedTerms'
    }

    def __init__(self, title=None, change_type=None, renamed_from=None, added_terms=None, removed_terms=None, local_vars_configuration=None):  # noqa: E501
        """TopicChangeSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._change_type = None
        self._renamed_from = None
        self._added_terms = None
        self._removed_terms = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if change_type is not None:
            self.change_type = change_type
        if renamed_from is not None:
            self.renamed_from = renamed_from
        if added_terms is not None:
            self.added_terms = added_terms
        if removed_terms is not None:
            self.removed_terms = removed_terms

    @property
    def title(self):
        """Gets the title of this TopicChangeSet.  # noqa: E501


        :return: The title of this TopicChangeSet.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TopicChangeSet.


        :param title: The title of this TopicChangeSet.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def change_type(self):
        """Gets the change_type of this TopicChangeSet.  # noqa: E501


        :return: The change_type of this TopicChangeSet.  # noqa: E501
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this TopicChangeSet.


        :param change_type: The change_type of this TopicChangeSet.  # noqa: E501
        :type change_type: str
        """
        allowed_values = ["ADDED", "REMOVED", "MODIFIED", "RENAMED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and change_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `change_type` ({0}), must be one of {1}"  # noqa: E501
                .format(change_type, allowed_values)
            )

        self._change_type = change_type

    @property
    def renamed_from(self):
        """Gets the renamed_from of this TopicChangeSet.  # noqa: E501


        :return: The renamed_from of this TopicChangeSet.  # noqa: E501
        :rtype: str
        """
        return self._renamed_from

    @renamed_from.setter
    def renamed_from(self, renamed_from):
        """Sets the renamed_from of this TopicChangeSet.


        :param renamed_from: The renamed_from of this TopicChangeSet.  # noqa: E501
        :type renamed_from: str
        """

        self._renamed_from = renamed_from

    @property
    def added_terms(self):
        """Gets the added_terms of this TopicChangeSet.  # noqa: E501


        :return: The added_terms of this TopicChangeSet.  # noqa: E501
        :rtype: list[TopicTermChangeSet]
        """
        return self._added_terms

    @added_terms.setter
    def added_terms(self, added_terms):
        """Sets the added_terms of this TopicChangeSet.


        :param added_terms: The added_terms of this TopicChangeSet.  # noqa: E501
        :type added_terms: list[TopicTermChangeSet]
        """

        self._added_terms = added_terms

    @property
    def removed_terms(self):
        """Gets the removed_terms of this TopicChangeSet.  # noqa: E501


        :return: The removed_terms of this TopicChangeSet.  # noqa: E501
        :rtype: list[TopicTermChangeSet]
        """
        return self._removed_terms

    @removed_terms.setter
    def removed_terms(self, removed_terms):
        """Sets the removed_terms of this TopicChangeSet.


        :param removed_terms: The removed_terms of this TopicChangeSet.  # noqa: E501
        :type removed_terms: list[TopicTermChangeSet]
        """

        self._removed_terms = removed_terms

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
        if not isinstance(other, TopicChangeSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopicChangeSet):
            return True

        return self.to_dict() != other.to_dict()
