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


class CreditsHistoryDataPoint(object):
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
        'credits_used': 'int',
        'credits_purchased': 'int',
        'credits_refilled': 'int',
        'credits_granted': 'int',
        'credits_unique_texts': 'int',
        'start_date': 'int',
        'end_date': 'int'
    }

    attribute_map = {
        'credits_used': 'creditsUsed',
        'credits_purchased': 'creditsPurchased',
        'credits_refilled': 'creditsRefilled',
        'credits_granted': 'creditsGranted',
        'credits_unique_texts': 'creditsUniqueTexts',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, credits_used=None, credits_purchased=None, credits_refilled=None, credits_granted=None, credits_unique_texts=None, start_date=None, end_date=None, local_vars_configuration=None):  # noqa: E501
        """CreditsHistoryDataPoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._credits_used = None
        self._credits_purchased = None
        self._credits_refilled = None
        self._credits_granted = None
        self._credits_unique_texts = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if credits_used is not None:
            self.credits_used = credits_used
        if credits_purchased is not None:
            self.credits_purchased = credits_purchased
        if credits_refilled is not None:
            self.credits_refilled = credits_refilled
        if credits_granted is not None:
            self.credits_granted = credits_granted
        if credits_unique_texts is not None:
            self.credits_unique_texts = credits_unique_texts
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def credits_used(self):
        """Gets the credits_used of this CreditsHistoryDataPoint.  # noqa: E501


        :return: The credits_used of this CreditsHistoryDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._credits_used

    @credits_used.setter
    def credits_used(self, credits_used):
        """Sets the credits_used of this CreditsHistoryDataPoint.


        :param credits_used: The credits_used of this CreditsHistoryDataPoint.  # noqa: E501
        :type credits_used: int
        """

        self._credits_used = credits_used

    @property
    def credits_purchased(self):
        """Gets the credits_purchased of this CreditsHistoryDataPoint.  # noqa: E501


        :return: The credits_purchased of this CreditsHistoryDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._credits_purchased

    @credits_purchased.setter
    def credits_purchased(self, credits_purchased):
        """Sets the credits_purchased of this CreditsHistoryDataPoint.


        :param credits_purchased: The credits_purchased of this CreditsHistoryDataPoint.  # noqa: E501
        :type credits_purchased: int
        """

        self._credits_purchased = credits_purchased

    @property
    def credits_refilled(self):
        """Gets the credits_refilled of this CreditsHistoryDataPoint.  # noqa: E501


        :return: The credits_refilled of this CreditsHistoryDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._credits_refilled

    @credits_refilled.setter
    def credits_refilled(self, credits_refilled):
        """Sets the credits_refilled of this CreditsHistoryDataPoint.


        :param credits_refilled: The credits_refilled of this CreditsHistoryDataPoint.  # noqa: E501
        :type credits_refilled: int
        """

        self._credits_refilled = credits_refilled

    @property
    def credits_granted(self):
        """Gets the credits_granted of this CreditsHistoryDataPoint.  # noqa: E501


        :return: The credits_granted of this CreditsHistoryDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._credits_granted

    @credits_granted.setter
    def credits_granted(self, credits_granted):
        """Sets the credits_granted of this CreditsHistoryDataPoint.


        :param credits_granted: The credits_granted of this CreditsHistoryDataPoint.  # noqa: E501
        :type credits_granted: int
        """

        self._credits_granted = credits_granted

    @property
    def credits_unique_texts(self):
        """Gets the credits_unique_texts of this CreditsHistoryDataPoint.  # noqa: E501


        :return: The credits_unique_texts of this CreditsHistoryDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._credits_unique_texts

    @credits_unique_texts.setter
    def credits_unique_texts(self, credits_unique_texts):
        """Sets the credits_unique_texts of this CreditsHistoryDataPoint.


        :param credits_unique_texts: The credits_unique_texts of this CreditsHistoryDataPoint.  # noqa: E501
        :type credits_unique_texts: int
        """

        self._credits_unique_texts = credits_unique_texts

    @property
    def start_date(self):
        """Gets the start_date of this CreditsHistoryDataPoint.  # noqa: E501


        :return: The start_date of this CreditsHistoryDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreditsHistoryDataPoint.


        :param start_date: The start_date of this CreditsHistoryDataPoint.  # noqa: E501
        :type start_date: int
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CreditsHistoryDataPoint.  # noqa: E501


        :return: The end_date of this CreditsHistoryDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreditsHistoryDataPoint.


        :param end_date: The end_date of this CreditsHistoryDataPoint.  # noqa: E501
        :type end_date: int
        """

        self._end_date = end_date

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
        if not isinstance(other, CreditsHistoryDataPoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditsHistoryDataPoint):
            return True

        return self.to_dict() != other.to_dict()
