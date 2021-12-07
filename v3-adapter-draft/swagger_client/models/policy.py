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

class Policy(object):
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
        'embedded': 'dict(str, object)',
        'links': 'dict(str, object)',
        'conditions': 'PolicyRuleConditions',
        'created': 'datetime',
        'description': 'str',
        'id': 'str',
        'last_updated': 'datetime',
        'name': 'str',
        'priority': 'int',
        'status': 'str',
        'system': 'bool',
        'type': 'PolicyType'
    }

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'conditions': 'conditions',
        'created': 'created',
        'description': 'description',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'priority': 'priority',
        'status': 'status',
        'system': 'system',
        'type': 'type'
    }

    discriminator_value_class_map = {
            'IDP_DISCOVERY'.lower(): '#/components/schemas/IdentityProviderPolicy',
            'OAUTH_AUTHORIZATION_POLICY'.lower(): '#/components/schemas/OAuthAuthorizationPolicy',
            'OKTA_SIGN_ON'.lower(): '#/components/schemas/OktaSignOnPolicy',
            'PASSWORD'.lower(): '#/components/schemas/PasswordPolicy',
    }

    def __init__(self, embedded=None, links=None, conditions=None, created=None, description=None, id=None, last_updated=None, name=None, priority=None, status=None, system=None, type=None):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._conditions = None
        self._created = None
        self._description = None
        self._id = None
        self._last_updated = None
        self._name = None
        self._priority = None
        self._status = None
        self._system = None
        self._type = None
        self.discriminator = 'type'
        if embedded is not None:
            self.embedded = embedded
        if links is not None:
            self.links = links
        if conditions is not None:
            self.conditions = conditions
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if status is not None:
            self.status = status
        if system is not None:
            self.system = system
        if type is not None:
            self.type = type

    @property
    def embedded(self):
        """Gets the embedded of this Policy.  # noqa: E501


        :return: The embedded of this Policy.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Policy.


        :param embedded: The embedded of this Policy.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this Policy.  # noqa: E501


        :return: The links of this Policy.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Policy.


        :param links: The links of this Policy.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def conditions(self):
        """Gets the conditions of this Policy.  # noqa: E501


        :return: The conditions of this Policy.  # noqa: E501
        :rtype: PolicyRuleConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Policy.


        :param conditions: The conditions of this Policy.  # noqa: E501
        :type: PolicyRuleConditions
        """

        self._conditions = conditions

    @property
    def created(self):
        """Gets the created of this Policy.  # noqa: E501


        :return: The created of this Policy.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Policy.


        :param created: The created of this Policy.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this Policy.  # noqa: E501


        :return: The description of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Policy.


        :param description: The description of this Policy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Policy.  # noqa: E501


        :return: The id of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Policy.


        :param id: The id of this Policy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this Policy.  # noqa: E501


        :return: The last_updated of this Policy.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Policy.


        :param last_updated: The last_updated of this Policy.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this Policy.  # noqa: E501


        :return: The name of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.


        :param name: The name of this Policy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this Policy.  # noqa: E501


        :return: The priority of this Policy.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Policy.


        :param priority: The priority of this Policy.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def status(self):
        """Gets the status of this Policy.  # noqa: E501


        :return: The status of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Policy.


        :param status: The status of this Policy.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def system(self):
        """Gets the system of this Policy.  # noqa: E501


        :return: The system of this Policy.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Policy.


        :param system: The system of this Policy.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def type(self):
        """Gets the type of this Policy.  # noqa: E501


        :return: The type of this Policy.  # noqa: E501
        :rtype: PolicyType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Policy.


        :param type: The type of this Policy.  # noqa: E501
        :type: PolicyType
        """

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(Policy, dict):
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
