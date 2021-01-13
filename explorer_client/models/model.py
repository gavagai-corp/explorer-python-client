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


class Model(object):
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
        'id': 'int',
        'title': 'str',
        'created': 'int',
        'created_by': 'User',
        'groups': 'list[ModelGroup]',
        'users_access': 'list[ModelAccess]',
        'invitations': 'list[ModelInvitation]',
        'ignore_terms': 'list[IgnoreTerm]',
        'ignore_terms_dictionary': 'dict(str, str)',
        'type': 'str',
        'outdated': 'bool',
        'language': 'str',
        'drivers': 'list[Driver]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'created': 'created',
        'created_by': 'createdBy',
        'groups': 'groups',
        'users_access': 'usersAccess',
        'invitations': 'invitations',
        'ignore_terms': 'ignoreTerms',
        'ignore_terms_dictionary': 'ignoreTermsDictionary',
        'type': 'type',
        'outdated': 'outdated',
        'language': 'language',
        'drivers': 'drivers'
    }

    def __init__(self, id=None, title=None, created=None, created_by=None, groups=None, users_access=None, invitations=None, ignore_terms=None, ignore_terms_dictionary=None, type=None, outdated=None, language=None, drivers=None, local_vars_configuration=None):  # noqa: E501
        """Model - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._created = None
        self._created_by = None
        self._groups = None
        self._users_access = None
        self._invitations = None
        self._ignore_terms = None
        self._ignore_terms_dictionary = None
        self._type = None
        self._outdated = None
        self._language = None
        self._drivers = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if groups is not None:
            self.groups = groups
        if users_access is not None:
            self.users_access = users_access
        if invitations is not None:
            self.invitations = invitations
        if ignore_terms is not None:
            self.ignore_terms = ignore_terms
        if ignore_terms_dictionary is not None:
            self.ignore_terms_dictionary = ignore_terms_dictionary
        if type is not None:
            self.type = type
        if outdated is not None:
            self.outdated = outdated
        if language is not None:
            self.language = language
        if drivers is not None:
            self.drivers = drivers

    @property
    def id(self):
        """Gets the id of this Model.  # noqa: E501


        :return: The id of this Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Model.


        :param id: The id of this Model.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Model.  # noqa: E501


        :return: The title of this Model.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Model.


        :param title: The title of this Model.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def created(self):
        """Gets the created of this Model.  # noqa: E501


        :return: The created of this Model.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Model.


        :param created: The created of this Model.  # noqa: E501
        :type created: int
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this Model.  # noqa: E501


        :return: The created_by of this Model.  # noqa: E501
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Model.


        :param created_by: The created_by of this Model.  # noqa: E501
        :type created_by: User
        """

        self._created_by = created_by

    @property
    def groups(self):
        """Gets the groups of this Model.  # noqa: E501


        :return: The groups of this Model.  # noqa: E501
        :rtype: list[ModelGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Model.


        :param groups: The groups of this Model.  # noqa: E501
        :type groups: list[ModelGroup]
        """

        self._groups = groups

    @property
    def users_access(self):
        """Gets the users_access of this Model.  # noqa: E501


        :return: The users_access of this Model.  # noqa: E501
        :rtype: list[ModelAccess]
        """
        return self._users_access

    @users_access.setter
    def users_access(self, users_access):
        """Sets the users_access of this Model.


        :param users_access: The users_access of this Model.  # noqa: E501
        :type users_access: list[ModelAccess]
        """

        self._users_access = users_access

    @property
    def invitations(self):
        """Gets the invitations of this Model.  # noqa: E501


        :return: The invitations of this Model.  # noqa: E501
        :rtype: list[ModelInvitation]
        """
        return self._invitations

    @invitations.setter
    def invitations(self, invitations):
        """Sets the invitations of this Model.


        :param invitations: The invitations of this Model.  # noqa: E501
        :type invitations: list[ModelInvitation]
        """

        self._invitations = invitations

    @property
    def ignore_terms(self):
        """Gets the ignore_terms of this Model.  # noqa: E501


        :return: The ignore_terms of this Model.  # noqa: E501
        :rtype: list[IgnoreTerm]
        """
        return self._ignore_terms

    @ignore_terms.setter
    def ignore_terms(self, ignore_terms):
        """Sets the ignore_terms of this Model.


        :param ignore_terms: The ignore_terms of this Model.  # noqa: E501
        :type ignore_terms: list[IgnoreTerm]
        """

        self._ignore_terms = ignore_terms

    @property
    def ignore_terms_dictionary(self):
        """Gets the ignore_terms_dictionary of this Model.  # noqa: E501


        :return: The ignore_terms_dictionary of this Model.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._ignore_terms_dictionary

    @ignore_terms_dictionary.setter
    def ignore_terms_dictionary(self, ignore_terms_dictionary):
        """Sets the ignore_terms_dictionary of this Model.


        :param ignore_terms_dictionary: The ignore_terms_dictionary of this Model.  # noqa: E501
        :type ignore_terms_dictionary: dict(str, str)
        """

        self._ignore_terms_dictionary = ignore_terms_dictionary

    @property
    def type(self):
        """Gets the type of this Model.  # noqa: E501


        :return: The type of this Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Model.


        :param type: The type of this Model.  # noqa: E501
        :type type: str
        """
        allowed_values = ["STANDARD", "DYNAMIC", "MANAGED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def outdated(self):
        """Gets the outdated of this Model.  # noqa: E501


        :return: The outdated of this Model.  # noqa: E501
        :rtype: bool
        """
        return self._outdated

    @outdated.setter
    def outdated(self, outdated):
        """Sets the outdated of this Model.


        :param outdated: The outdated of this Model.  # noqa: E501
        :type outdated: bool
        """

        self._outdated = outdated

    @property
    def language(self):
        """Gets the language of this Model.  # noqa: E501


        :return: The language of this Model.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Model.


        :param language: The language of this Model.  # noqa: E501
        :type language: str
        """

        self._language = language

    @property
    def drivers(self):
        """Gets the drivers of this Model.  # noqa: E501


        :return: The drivers of this Model.  # noqa: E501
        :rtype: list[Driver]
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this Model.


        :param drivers: The drivers of this Model.  # noqa: E501
        :type drivers: list[Driver]
        """

        self._drivers = drivers

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
        if not isinstance(other, Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Model):
            return True

        return self.to_dict() != other.to_dict()