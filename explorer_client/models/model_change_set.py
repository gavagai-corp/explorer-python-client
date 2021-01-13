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


class ModelChangeSet(object):
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
        'topic_change_sets': 'list[TopicChangeSet]',
        'removed_ignore_terms': 'list[IgnoreTermChangeSet]',
        'added_ignore_terms': 'list[IgnoreTermChangeSet]'
    }

    attribute_map = {
        'topic_change_sets': 'topicChangeSets',
        'removed_ignore_terms': 'removedIgnoreTerms',
        'added_ignore_terms': 'addedIgnoreTerms'
    }

    def __init__(self, topic_change_sets=None, removed_ignore_terms=None, added_ignore_terms=None, local_vars_configuration=None):  # noqa: E501
        """ModelChangeSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._topic_change_sets = None
        self._removed_ignore_terms = None
        self._added_ignore_terms = None
        self.discriminator = None

        if topic_change_sets is not None:
            self.topic_change_sets = topic_change_sets
        if removed_ignore_terms is not None:
            self.removed_ignore_terms = removed_ignore_terms
        if added_ignore_terms is not None:
            self.added_ignore_terms = added_ignore_terms

    @property
    def topic_change_sets(self):
        """Gets the topic_change_sets of this ModelChangeSet.  # noqa: E501


        :return: The topic_change_sets of this ModelChangeSet.  # noqa: E501
        :rtype: list[TopicChangeSet]
        """
        return self._topic_change_sets

    @topic_change_sets.setter
    def topic_change_sets(self, topic_change_sets):
        """Sets the topic_change_sets of this ModelChangeSet.


        :param topic_change_sets: The topic_change_sets of this ModelChangeSet.  # noqa: E501
        :type topic_change_sets: list[TopicChangeSet]
        """

        self._topic_change_sets = topic_change_sets

    @property
    def removed_ignore_terms(self):
        """Gets the removed_ignore_terms of this ModelChangeSet.  # noqa: E501


        :return: The removed_ignore_terms of this ModelChangeSet.  # noqa: E501
        :rtype: list[IgnoreTermChangeSet]
        """
        return self._removed_ignore_terms

    @removed_ignore_terms.setter
    def removed_ignore_terms(self, removed_ignore_terms):
        """Sets the removed_ignore_terms of this ModelChangeSet.


        :param removed_ignore_terms: The removed_ignore_terms of this ModelChangeSet.  # noqa: E501
        :type removed_ignore_terms: list[IgnoreTermChangeSet]
        """

        self._removed_ignore_terms = removed_ignore_terms

    @property
    def added_ignore_terms(self):
        """Gets the added_ignore_terms of this ModelChangeSet.  # noqa: E501


        :return: The added_ignore_terms of this ModelChangeSet.  # noqa: E501
        :rtype: list[IgnoreTermChangeSet]
        """
        return self._added_ignore_terms

    @added_ignore_terms.setter
    def added_ignore_terms(self, added_ignore_terms):
        """Sets the added_ignore_terms of this ModelChangeSet.


        :param added_ignore_terms: The added_ignore_terms of this ModelChangeSet.  # noqa: E501
        :type added_ignore_terms: list[IgnoreTermChangeSet]
        """

        self._added_ignore_terms = added_ignore_terms

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
        if not isinstance(other, ModelChangeSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelChangeSet):
            return True

        return self.to_dict() != other.to_dict()