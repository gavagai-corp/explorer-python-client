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


class ProjectReport(object):
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
        'created': 'int',
        'type': 'str',
        'status': 'str',
        'progress_percentage': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'type': 'type',
        'status': 'status',
        'progress_percentage': 'progressPercentage'
    }

    def __init__(self, id=None, created=None, type=None, status=None, progress_percentage=None, local_vars_configuration=None):  # noqa: E501
        """ProjectReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._type = None
        self._status = None
        self._progress_percentage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if progress_percentage is not None:
            self.progress_percentage = progress_percentage

    @property
    def id(self):
        """Gets the id of this ProjectReport.  # noqa: E501


        :return: The id of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectReport.


        :param id: The id of this ProjectReport.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this ProjectReport.  # noqa: E501


        :return: The created of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ProjectReport.


        :param created: The created of this ProjectReport.  # noqa: E501
        :type created: int
        """

        self._created = created

    @property
    def type(self):
        """Gets the type of this ProjectReport.  # noqa: E501


        :return: The type of this ProjectReport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProjectReport.


        :param type: The type of this ProjectReport.  # noqa: E501
        :type type: str
        """
        allowed_values = ["EXCEL", "PDF", "EXCEL_FULL", "CSV_FULL", "EXCEL_DRIVERS", "PDF_DRIVERS", "PDF_TOPIC_DRIVERS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this ProjectReport.  # noqa: E501


        :return: The status of this ProjectReport.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectReport.


        :param status: The status of this ProjectReport.  # noqa: E501
        :type status: str
        """
        allowed_values = ["IN_PROGRESS", "FINISHED", "ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def progress_percentage(self):
        """Gets the progress_percentage of this ProjectReport.  # noqa: E501


        :return: The progress_percentage of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, progress_percentage):
        """Sets the progress_percentage of this ProjectReport.


        :param progress_percentage: The progress_percentage of this ProjectReport.  # noqa: E501
        :type progress_percentage: int
        """

        self._progress_percentage = progress_percentage

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
        if not isinstance(other, ProjectReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectReport):
            return True

        return self.to_dict() != other.to_dict()
