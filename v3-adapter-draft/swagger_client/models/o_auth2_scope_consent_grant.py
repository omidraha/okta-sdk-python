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

class OAuth2ScopeConsentGrant(object):
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
        'client_id': 'str',
        'user_id': 'str',
        'created': 'datetime',
        'created_by': 'OAuth2Actor',
        'id': 'str',
        'issuer': 'str',
        'last_updated': 'datetime',
        'scope_id': 'str',
        'source': 'OAuth2ScopeConsentGrantSource',
        'status': 'OAuth2ScopeConsentGrantStatus'
    }

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'client_id': 'clientId',
        'user_id': 'userId',
        'created': 'created',
        'created_by': 'createdBy',
        'id': 'id',
        'issuer': 'issuer',
        'last_updated': 'lastUpdated',
        'scope_id': 'scopeId',
        'source': 'source',
        'status': 'status'
    }

    def __init__(self, embedded=None, links=None, client_id=None, user_id=None, created=None, created_by=None, id=None, issuer=None, last_updated=None, scope_id=None, source=None, status=None):  # noqa: E501
        """OAuth2ScopeConsentGrant - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._client_id = None
        self._user_id = None
        self._created = None
        self._created_by = None
        self._id = None
        self._issuer = None
        self._last_updated = None
        self._scope_id = None
        self._source = None
        self._status = None
        self.discriminator = None
        if embedded is not None:
            self.embedded = embedded
        if links is not None:
            self.links = links
        if client_id is not None:
            self.client_id = client_id
        if user_id is not None:
            self.user_id = user_id
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if id is not None:
            self.id = id
        if issuer is not None:
            self.issuer = issuer
        if last_updated is not None:
            self.last_updated = last_updated
        if scope_id is not None:
            self.scope_id = scope_id
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status

    @property
    def embedded(self):
        """Gets the embedded of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The embedded of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this OAuth2ScopeConsentGrant.


        :param embedded: The embedded of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The links of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OAuth2ScopeConsentGrant.


        :param links: The links of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def client_id(self):
        """Gets the client_id of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The client_id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OAuth2ScopeConsentGrant.


        :param client_id: The client_id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def user_id(self):
        """Gets the user_id of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The user_id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OAuth2ScopeConsentGrant.


        :param user_id: The user_id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def created(self):
        """Gets the created of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The created of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OAuth2ScopeConsentGrant.


        :param created: The created of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The created_by of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: OAuth2Actor
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OAuth2ScopeConsentGrant.


        :param created_by: The created_by of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: OAuth2Actor
        """

        self._created_by = created_by

    @property
    def id(self):
        """Gets the id of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2ScopeConsentGrant.


        :param id: The id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issuer(self):
        """Gets the issuer of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The issuer of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this OAuth2ScopeConsentGrant.


        :param issuer: The issuer of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def last_updated(self):
        """Gets the last_updated of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The last_updated of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this OAuth2ScopeConsentGrant.


        :param last_updated: The last_updated of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def scope_id(self):
        """Gets the scope_id of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The scope_id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this OAuth2ScopeConsentGrant.


        :param scope_id: The scope_id of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def source(self):
        """Gets the source of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The source of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: OAuth2ScopeConsentGrantSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this OAuth2ScopeConsentGrant.


        :param source: The source of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: OAuth2ScopeConsentGrantSource
        """

        self._source = source

    @property
    def status(self):
        """Gets the status of this OAuth2ScopeConsentGrant.  # noqa: E501


        :return: The status of this OAuth2ScopeConsentGrant.  # noqa: E501
        :rtype: OAuth2ScopeConsentGrantStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OAuth2ScopeConsentGrant.


        :param status: The status of this OAuth2ScopeConsentGrant.  # noqa: E501
        :type: OAuth2ScopeConsentGrantStatus
        """

        self._status = status

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
        if issubclass(OAuth2ScopeConsentGrant, dict):
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
        if not isinstance(other, OAuth2ScopeConsentGrant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
