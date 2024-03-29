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


class DocumentSentences(object):
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
        'document_text': 'str',
        'general_document_tonalities': 'list[Tonality]',
        'tonalities': 'list[Tonality]',
        'relevant_sentences': 'list[Sentence]',
        'selected_meta_data_list': 'list[SelectedMetaData]'
    }

    attribute_map = {
        'document_text': 'documentText',
        'general_document_tonalities': 'generalDocumentTonalities',
        'tonalities': 'tonalities',
        'relevant_sentences': 'relevantSentences',
        'selected_meta_data_list': 'selectedMetaDataList'
    }

    def __init__(self, document_text=None, general_document_tonalities=None, tonalities=None, relevant_sentences=None, selected_meta_data_list=None, local_vars_configuration=None):  # noqa: E501
        """DocumentSentences - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document_text = None
        self._general_document_tonalities = None
        self._tonalities = None
        self._relevant_sentences = None
        self._selected_meta_data_list = None
        self.discriminator = None

        if document_text is not None:
            self.document_text = document_text
        if general_document_tonalities is not None:
            self.general_document_tonalities = general_document_tonalities
        if tonalities is not None:
            self.tonalities = tonalities
        if relevant_sentences is not None:
            self.relevant_sentences = relevant_sentences
        if selected_meta_data_list is not None:
            self.selected_meta_data_list = selected_meta_data_list

    @property
    def document_text(self):
        """Gets the document_text of this DocumentSentences.  # noqa: E501


        :return: The document_text of this DocumentSentences.  # noqa: E501
        :rtype: str
        """
        return self._document_text

    @document_text.setter
    def document_text(self, document_text):
        """Sets the document_text of this DocumentSentences.


        :param document_text: The document_text of this DocumentSentences.  # noqa: E501
        :type document_text: str
        """

        self._document_text = document_text

    @property
    def general_document_tonalities(self):
        """Gets the general_document_tonalities of this DocumentSentences.  # noqa: E501


        :return: The general_document_tonalities of this DocumentSentences.  # noqa: E501
        :rtype: list[Tonality]
        """
        return self._general_document_tonalities

    @general_document_tonalities.setter
    def general_document_tonalities(self, general_document_tonalities):
        """Sets the general_document_tonalities of this DocumentSentences.


        :param general_document_tonalities: The general_document_tonalities of this DocumentSentences.  # noqa: E501
        :type general_document_tonalities: list[Tonality]
        """

        self._general_document_tonalities = general_document_tonalities

    @property
    def tonalities(self):
        """Gets the tonalities of this DocumentSentences.  # noqa: E501


        :return: The tonalities of this DocumentSentences.  # noqa: E501
        :rtype: list[Tonality]
        """
        return self._tonalities

    @tonalities.setter
    def tonalities(self, tonalities):
        """Sets the tonalities of this DocumentSentences.


        :param tonalities: The tonalities of this DocumentSentences.  # noqa: E501
        :type tonalities: list[Tonality]
        """

        self._tonalities = tonalities

    @property
    def relevant_sentences(self):
        """Gets the relevant_sentences of this DocumentSentences.  # noqa: E501


        :return: The relevant_sentences of this DocumentSentences.  # noqa: E501
        :rtype: list[Sentence]
        """
        return self._relevant_sentences

    @relevant_sentences.setter
    def relevant_sentences(self, relevant_sentences):
        """Sets the relevant_sentences of this DocumentSentences.


        :param relevant_sentences: The relevant_sentences of this DocumentSentences.  # noqa: E501
        :type relevant_sentences: list[Sentence]
        """

        self._relevant_sentences = relevant_sentences

    @property
    def selected_meta_data_list(self):
        """Gets the selected_meta_data_list of this DocumentSentences.  # noqa: E501


        :return: The selected_meta_data_list of this DocumentSentences.  # noqa: E501
        :rtype: list[SelectedMetaData]
        """
        return self._selected_meta_data_list

    @selected_meta_data_list.setter
    def selected_meta_data_list(self, selected_meta_data_list):
        """Sets the selected_meta_data_list of this DocumentSentences.


        :param selected_meta_data_list: The selected_meta_data_list of this DocumentSentences.  # noqa: E501
        :type selected_meta_data_list: list[SelectedMetaData]
        """

        self._selected_meta_data_list = selected_meta_data_list

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
        if not isinstance(other, DocumentSentences):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentSentences):
            return True

        return self.to_dict() != other.to_dict()
