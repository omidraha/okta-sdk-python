# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrgOktaCommunicationSetting(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'dict(str, object)',
        'opt_out_email_users': 'bool'
    }

    attribute_map = {
        'links': '_links',
        'opt_out_email_users': 'optOutEmailUsers'
    }

    def __init__(self, links=None, opt_out_email_users=None):  # noqa: E501
        """OrgOktaCommunicationSetting - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._opt_out_email_users = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if opt_out_email_users is not None:
            self.opt_out_email_users = opt_out_email_users

    @property
    def links(self):
        """Gets the links of this OrgOktaCommunicationSetting.  # noqa: E501


        :return: The links of this OrgOktaCommunicationSetting.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrgOktaCommunicationSetting.


        :param links: The links of this OrgOktaCommunicationSetting.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def opt_out_email_users(self):
        """Gets the opt_out_email_users of this OrgOktaCommunicationSetting.  # noqa: E501


        :return: The opt_out_email_users of this OrgOktaCommunicationSetting.  # noqa: E501
        :rtype: bool
        """
        return self._opt_out_email_users

    @opt_out_email_users.setter
    def opt_out_email_users(self, opt_out_email_users):
        """Sets the opt_out_email_users of this OrgOktaCommunicationSetting.


        :param opt_out_email_users: The opt_out_email_users of this OrgOktaCommunicationSetting.  # noqa: E501
        :type: bool
        """

        self._opt_out_email_users = opt_out_email_users

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrgOktaCommunicationSetting, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrgOktaCommunicationSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
