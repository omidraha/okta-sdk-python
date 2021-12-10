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

class ChangePasswordRequest(object):
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
        'new_password': 'PasswordCredential',
        'old_password': 'PasswordCredential'
    }

    attribute_map = {
        'new_password': 'newPassword',
        'old_password': 'oldPassword'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, new_password=None, old_password=None):  # noqa: E501
        """ChangePasswordRequest - a model defined in Swagger"""  # noqa: E501
        self._new_password = None
        self._old_password = None
        self.discriminator = None
        if new_password is not None:
            self.new_password = new_password
        if old_password is not None:
            self.old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this ChangePasswordRequest.  # noqa: E501


        :return: The new_password of this ChangePasswordRequest.  # noqa: E501
        :rtype: PasswordCredential
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ChangePasswordRequest.


        :param new_password: The new_password of this ChangePasswordRequest.  # noqa: E501
        :type: PasswordCredential
        """

        self._new_password = new_password

    @property
    def old_password(self):
        """Gets the old_password of this ChangePasswordRequest.  # noqa: E501


        :return: The old_password of this ChangePasswordRequest.  # noqa: E501
        :rtype: PasswordCredential
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this ChangePasswordRequest.


        :param old_password: The old_password of this ChangePasswordRequest.  # noqa: E501
        :type: PasswordCredential
        """

        self._old_password = old_password

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
        if issubclass(ChangePasswordRequest, dict):
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
        if not isinstance(other, ChangePasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other