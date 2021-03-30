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


class Account(object):
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
        'registration_date': 'int',
        'manager': 'User',
        'managed_users': 'list[User]',
        'pending_invitations': 'list[ManagerInvitation]'
    }

    attribute_map = {
        'registration_date': 'registrationDate',
        'manager': 'manager',
        'managed_users': 'managedUsers',
        'pending_invitations': 'pendingInvitations'
    }

    def __init__(self, registration_date=None, manager=None, managed_users=None, pending_invitations=None, local_vars_configuration=None):  # noqa: E501
        """Account - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._registration_date = None
        self._manager = None
        self._managed_users = None
        self._pending_invitations = None
        self.discriminator = None

        if registration_date is not None:
            self.registration_date = registration_date
        if manager is not None:
            self.manager = manager
        if managed_users is not None:
            self.managed_users = managed_users
        if pending_invitations is not None:
            self.pending_invitations = pending_invitations

    @property
    def registration_date(self):
        """Gets the registration_date of this Account.  # noqa: E501


        :return: The registration_date of this Account.  # noqa: E501
        :rtype: int
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this Account.


        :param registration_date: The registration_date of this Account.  # noqa: E501
        :type registration_date: int
        """

        self._registration_date = registration_date

    @property
    def manager(self):
        """Gets the manager of this Account.  # noqa: E501


        :return: The manager of this Account.  # noqa: E501
        :rtype: User
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this Account.


        :param manager: The manager of this Account.  # noqa: E501
        :type manager: User
        """

        self._manager = manager

    @property
    def managed_users(self):
        """Gets the managed_users of this Account.  # noqa: E501


        :return: The managed_users of this Account.  # noqa: E501
        :rtype: list[User]
        """
        return self._managed_users

    @managed_users.setter
    def managed_users(self, managed_users):
        """Sets the managed_users of this Account.


        :param managed_users: The managed_users of this Account.  # noqa: E501
        :type managed_users: list[User]
        """

        self._managed_users = managed_users

    @property
    def pending_invitations(self):
        """Gets the pending_invitations of this Account.  # noqa: E501


        :return: The pending_invitations of this Account.  # noqa: E501
        :rtype: list[ManagerInvitation]
        """
        return self._pending_invitations

    @pending_invitations.setter
    def pending_invitations(self, pending_invitations):
        """Sets the pending_invitations of this Account.


        :param pending_invitations: The pending_invitations of this Account.  # noqa: E501
        :type pending_invitations: list[ManagerInvitation]
        """

        self._pending_invitations = pending_invitations

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
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
