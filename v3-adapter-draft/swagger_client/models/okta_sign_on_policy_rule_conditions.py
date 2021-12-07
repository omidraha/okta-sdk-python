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

class OktaSignOnPolicyRuleConditions(object):
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
        'auth_context': 'PolicyRuleAuthContextCondition',
        'network': 'PolicyNetworkCondition',
        'people': 'PolicyPeopleCondition'
    }

    attribute_map = {
        'auth_context': 'authContext',
        'network': 'network',
        'people': 'people'
    }

    def __init__(self, auth_context=None, network=None, people=None):  # noqa: E501
        """OktaSignOnPolicyRuleConditions - a model defined in Swagger"""  # noqa: E501
        self._auth_context = None
        self._network = None
        self._people = None
        self.discriminator = None
        if auth_context is not None:
            self.auth_context = auth_context
        if network is not None:
            self.network = network
        if people is not None:
            self.people = people

    @property
    def auth_context(self):
        """Gets the auth_context of this OktaSignOnPolicyRuleConditions.  # noqa: E501


        :return: The auth_context of this OktaSignOnPolicyRuleConditions.  # noqa: E501
        :rtype: PolicyRuleAuthContextCondition
        """
        return self._auth_context

    @auth_context.setter
    def auth_context(self, auth_context):
        """Sets the auth_context of this OktaSignOnPolicyRuleConditions.


        :param auth_context: The auth_context of this OktaSignOnPolicyRuleConditions.  # noqa: E501
        :type: PolicyRuleAuthContextCondition
        """

        self._auth_context = auth_context

    @property
    def network(self):
        """Gets the network of this OktaSignOnPolicyRuleConditions.  # noqa: E501


        :return: The network of this OktaSignOnPolicyRuleConditions.  # noqa: E501
        :rtype: PolicyNetworkCondition
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this OktaSignOnPolicyRuleConditions.


        :param network: The network of this OktaSignOnPolicyRuleConditions.  # noqa: E501
        :type: PolicyNetworkCondition
        """

        self._network = network

    @property
    def people(self):
        """Gets the people of this OktaSignOnPolicyRuleConditions.  # noqa: E501


        :return: The people of this OktaSignOnPolicyRuleConditions.  # noqa: E501
        :rtype: PolicyPeopleCondition
        """
        return self._people

    @people.setter
    def people(self, people):
        """Sets the people of this OktaSignOnPolicyRuleConditions.


        :param people: The people of this OktaSignOnPolicyRuleConditions.  # noqa: E501
        :type: PolicyPeopleCondition
        """

        self._people = people

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
        if issubclass(OktaSignOnPolicyRuleConditions, dict):
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
        if not isinstance(other, OktaSignOnPolicyRuleConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
