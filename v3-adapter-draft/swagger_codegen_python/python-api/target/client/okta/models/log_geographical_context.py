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

class LogGeographicalContext(object):
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
        'city': 'str',
        'country': 'str',
        'geolocation': 'LogGeolocation',
        'postal_code': 'str',
        'state': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country': 'country',
        'geolocation': 'geolocation',
        'postal_code': 'postalCode',
        'state': 'state'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, city=None, country=None, geolocation=None, postal_code=None, state=None):  # noqa: E501
        """LogGeographicalContext - a model defined in Swagger"""  # noqa: E501
        self._city = None
        self._country = None
        self._geolocation = None
        self._postal_code = None
        self._state = None
        self.discriminator = None
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if geolocation is not None:
            self.geolocation = geolocation
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state

    @property
    def city(self):
        """Gets the city of this LogGeographicalContext.  # noqa: E501


        :return: The city of this LogGeographicalContext.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this LogGeographicalContext.


        :param city: The city of this LogGeographicalContext.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this LogGeographicalContext.  # noqa: E501


        :return: The country of this LogGeographicalContext.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this LogGeographicalContext.


        :param country: The country of this LogGeographicalContext.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def geolocation(self):
        """Gets the geolocation of this LogGeographicalContext.  # noqa: E501


        :return: The geolocation of this LogGeographicalContext.  # noqa: E501
        :rtype: LogGeolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this LogGeographicalContext.


        :param geolocation: The geolocation of this LogGeographicalContext.  # noqa: E501
        :type: LogGeolocation
        """

        self._geolocation = geolocation

    @property
    def postal_code(self):
        """Gets the postal_code of this LogGeographicalContext.  # noqa: E501


        :return: The postal_code of this LogGeographicalContext.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this LogGeographicalContext.


        :param postal_code: The postal_code of this LogGeographicalContext.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this LogGeographicalContext.  # noqa: E501


        :return: The state of this LogGeographicalContext.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this LogGeographicalContext.


        :param state: The state of this LogGeographicalContext.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(LogGeographicalContext, dict):
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
        if not isinstance(other, LogGeographicalContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other