# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.10.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class CapabilitiesUpdateObject(object):
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
    swagger_types = {}
    swagger_types['lifecycle_deactivate'] = 'LifecycleDeactivateSettingObject'
    swagger_types['password'] = 'PasswordSettingObject'
    swagger_types['profile'] = 'ProfileSettingObject'

    attribute_map = {
        'lifecycle_deactivate': 'lifecycleDeactivate',
        'password': 'password',
        'profile': 'profile'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, lifecycle_deactivate=None, password=None, profile=None, **kwargs):  # noqa: E501
        """CapabilitiesUpdateObject - a model defined in Swagger"""  # noqa: E501
        self._lifecycle_deactivate = None
        self._password = None
        self._profile = None
        self.discriminator = None
        if lifecycle_deactivate is not None:
            if hasattr(models, self.swagger_types['lifecycle_deactivate']):
                nested_class = getattr(models, self.swagger_types['lifecycle_deactivate'])
                if isinstance(lifecycle_deactivate, nested_class):
                    self.lifecycle_deactivate = lifecycle_deactivate
                elif isinstance(lifecycle_deactivate, dict):
                    self.lifecycle_deactivate = nested_class.from_kwargs(**lifecycle_deactivate)
                else:
                    self.lifecycle_deactivate = lifecycle_deactivate
            else:
                self.lifecycle_deactivate = lifecycle_deactivate
        if password is not None:
            if hasattr(models, self.swagger_types['password']):
                nested_class = getattr(models, self.swagger_types['password'])
                if isinstance(password, nested_class):
                    self.password = password
                elif isinstance(password, dict):
                    self.password = nested_class.from_kwargs(**password)
                else:
                    self.password = password
            else:
                self.password = password
        if profile is not None:
            if hasattr(models, self.swagger_types['profile']):
                nested_class = getattr(models, self.swagger_types['profile'])
                if isinstance(profile, nested_class):
                    self.profile = profile
                elif isinstance(profile, dict):
                    self.profile = nested_class.from_kwargs(**profile)
                else:
                    self.profile = profile
            else:
                self.profile = profile

    @property
    def lifecycle_deactivate(self):
        """Gets the lifecycle_deactivate of this CapabilitiesUpdateObject.  # noqa: E501


        :return: The lifecycle_deactivate of this CapabilitiesUpdateObject.  # noqa: E501
        :rtype: LifecycleDeactivateSettingObject
        """
        return self._lifecycle_deactivate

    @lifecycle_deactivate.setter
    def lifecycle_deactivate(self, lifecycle_deactivate):
        """Sets the lifecycle_deactivate of this CapabilitiesUpdateObject.


        :param lifecycle_deactivate: The lifecycle_deactivate of this CapabilitiesUpdateObject.  # noqa: E501
        :type: LifecycleDeactivateSettingObject
        """

        self._lifecycle_deactivate = lifecycle_deactivate

    @property
    def password(self):
        """Gets the password of this CapabilitiesUpdateObject.  # noqa: E501


        :return: The password of this CapabilitiesUpdateObject.  # noqa: E501
        :rtype: PasswordSettingObject
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CapabilitiesUpdateObject.


        :param password: The password of this CapabilitiesUpdateObject.  # noqa: E501
        :type: PasswordSettingObject
        """

        self._password = password

    @property
    def profile(self):
        """Gets the profile of this CapabilitiesUpdateObject.  # noqa: E501


        :return: The profile of this CapabilitiesUpdateObject.  # noqa: E501
        :rtype: ProfileSettingObject
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this CapabilitiesUpdateObject.


        :param profile: The profile of this CapabilitiesUpdateObject.  # noqa: E501
        :type: ProfileSettingObject
        """

        self._profile = profile

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
        if issubclass(CapabilitiesUpdateObject, dict):
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
        if not isinstance(other, CapabilitiesUpdateObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other