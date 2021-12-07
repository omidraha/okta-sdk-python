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

class DevicePolicyRuleCondition(object):
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
        'migrated': 'bool',
        'platform': 'DevicePolicyRuleConditionPlatform',
        'rooted': 'bool',
        'trust_level': 'str'
    }

    attribute_map = {
        'migrated': 'migrated',
        'platform': 'platform',
        'rooted': 'rooted',
        'trust_level': 'trustLevel'
    }

    def __init__(self, migrated=None, platform=None, rooted=None, trust_level=None):  # noqa: E501
        """DevicePolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._migrated = None
        self._platform = None
        self._rooted = None
        self._trust_level = None
        self.discriminator = None
        if migrated is not None:
            self.migrated = migrated
        if platform is not None:
            self.platform = platform
        if rooted is not None:
            self.rooted = rooted
        if trust_level is not None:
            self.trust_level = trust_level

    @property
    def migrated(self):
        """Gets the migrated of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The migrated of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: bool
        """
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        """Sets the migrated of this DevicePolicyRuleCondition.


        :param migrated: The migrated of this DevicePolicyRuleCondition.  # noqa: E501
        :type: bool
        """

        self._migrated = migrated

    @property
    def platform(self):
        """Gets the platform of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The platform of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: DevicePolicyRuleConditionPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DevicePolicyRuleCondition.


        :param platform: The platform of this DevicePolicyRuleCondition.  # noqa: E501
        :type: DevicePolicyRuleConditionPlatform
        """

        self._platform = platform

    @property
    def rooted(self):
        """Gets the rooted of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The rooted of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: bool
        """
        return self._rooted

    @rooted.setter
    def rooted(self, rooted):
        """Sets the rooted of this DevicePolicyRuleCondition.


        :param rooted: The rooted of this DevicePolicyRuleCondition.  # noqa: E501
        :type: bool
        """

        self._rooted = rooted

    @property
    def trust_level(self):
        """Gets the trust_level of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The trust_level of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._trust_level

    @trust_level.setter
    def trust_level(self, trust_level):
        """Sets the trust_level of this DevicePolicyRuleCondition.


        :param trust_level: The trust_level of this DevicePolicyRuleCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["ANY", "TRUSTED"]  # noqa: E501
        if trust_level not in allowed_values:
            raise ValueError(
                "Invalid value for `trust_level` ({0}), must be one of {1}"  # noqa: E501
                .format(trust_level, allowed_values)
            )

        self._trust_level = trust_level

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
        if issubclass(DevicePolicyRuleCondition, dict):
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
        if not isinstance(other, DevicePolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
