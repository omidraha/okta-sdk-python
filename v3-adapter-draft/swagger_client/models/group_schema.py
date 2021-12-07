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

class GroupSchema(object):
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
        'schema': 'str',
        'links': 'dict(str, object)',
        'created': 'str',
        'definitions': 'GroupSchemaDefinitions',
        'description': 'str',
        'id': 'str',
        'last_updated': 'str',
        'name': 'str',
        'properties': 'UserSchemaProperties',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'schema': '$schema',
        'links': '_links',
        'created': 'created',
        'definitions': 'definitions',
        'description': 'description',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'properties': 'properties',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, schema=None, links=None, created=None, definitions=None, description=None, id=None, last_updated=None, name=None, properties=None, title=None, type=None):  # noqa: E501
        """GroupSchema - a model defined in Swagger"""  # noqa: E501
        self._schema = None
        self._links = None
        self._created = None
        self._definitions = None
        self._description = None
        self._id = None
        self._last_updated = None
        self._name = None
        self._properties = None
        self._title = None
        self._type = None
        self.discriminator = None
        if schema is not None:
            self.schema = schema
        if links is not None:
            self.links = links
        if created is not None:
            self.created = created
        if definitions is not None:
            self.definitions = definitions
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def schema(self):
        """Gets the schema of this GroupSchema.  # noqa: E501


        :return: The schema of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this GroupSchema.


        :param schema: The schema of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def links(self):
        """Gets the links of this GroupSchema.  # noqa: E501


        :return: The links of this GroupSchema.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GroupSchema.


        :param links: The links of this GroupSchema.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this GroupSchema.  # noqa: E501


        :return: The created of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GroupSchema.


        :param created: The created of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def definitions(self):
        """Gets the definitions of this GroupSchema.  # noqa: E501


        :return: The definitions of this GroupSchema.  # noqa: E501
        :rtype: GroupSchemaDefinitions
        """
        return self._definitions

    @definitions.setter
    def definitions(self, definitions):
        """Sets the definitions of this GroupSchema.


        :param definitions: The definitions of this GroupSchema.  # noqa: E501
        :type: GroupSchemaDefinitions
        """

        self._definitions = definitions

    @property
    def description(self):
        """Gets the description of this GroupSchema.  # noqa: E501


        :return: The description of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupSchema.


        :param description: The description of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this GroupSchema.  # noqa: E501


        :return: The id of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupSchema.


        :param id: The id of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this GroupSchema.  # noqa: E501


        :return: The last_updated of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this GroupSchema.


        :param last_updated: The last_updated of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this GroupSchema.  # noqa: E501


        :return: The name of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupSchema.


        :param name: The name of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this GroupSchema.  # noqa: E501


        :return: The properties of this GroupSchema.  # noqa: E501
        :rtype: UserSchemaProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GroupSchema.


        :param properties: The properties of this GroupSchema.  # noqa: E501
        :type: UserSchemaProperties
        """

        self._properties = properties

    @property
    def title(self):
        """Gets the title of this GroupSchema.  # noqa: E501


        :return: The title of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GroupSchema.


        :param title: The title of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this GroupSchema.  # noqa: E501


        :return: The type of this GroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupSchema.


        :param type: The type of this GroupSchema.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(GroupSchema, dict):
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
        if not isinstance(other, GroupSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
