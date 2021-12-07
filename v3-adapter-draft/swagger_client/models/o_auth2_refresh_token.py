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

class OAuth2RefreshToken(object):
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
        'created': 'datetime',
        'created_by': 'OAuth2Actor',
        'expires_at': 'datetime',
        'id': 'str',
        'issuer': 'str',
        'last_updated': 'datetime',
        'scopes': 'list[str]',
        'status': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'client_id': 'clientId',
        'created': 'created',
        'created_by': 'createdBy',
        'expires_at': 'expiresAt',
        'id': 'id',
        'issuer': 'issuer',
        'last_updated': 'lastUpdated',
        'scopes': 'scopes',
        'status': 'status',
        'user_id': 'userId'
    }

    def __init__(self, embedded=None, links=None, client_id=None, created=None, created_by=None, expires_at=None, id=None, issuer=None, last_updated=None, scopes=None, status=None, user_id=None):  # noqa: E501
        """OAuth2RefreshToken - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._client_id = None
        self._created = None
        self._created_by = None
        self._expires_at = None
        self._id = None
        self._issuer = None
        self._last_updated = None
        self._scopes = None
        self._status = None
        self._user_id = None
        self.discriminator = None
        if embedded is not None:
            self.embedded = embedded
        if links is not None:
            self.links = links
        if client_id is not None:
            self.client_id = client_id
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if expires_at is not None:
            self.expires_at = expires_at
        if id is not None:
            self.id = id
        if issuer is not None:
            self.issuer = issuer
        if last_updated is not None:
            self.last_updated = last_updated
        if scopes is not None:
            self.scopes = scopes
        if status is not None:
            self.status = status
        if user_id is not None:
            self.user_id = user_id

    @property
    def embedded(self):
        """Gets the embedded of this OAuth2RefreshToken.  # noqa: E501


        :return: The embedded of this OAuth2RefreshToken.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this OAuth2RefreshToken.


        :param embedded: The embedded of this OAuth2RefreshToken.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this OAuth2RefreshToken.  # noqa: E501


        :return: The links of this OAuth2RefreshToken.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OAuth2RefreshToken.


        :param links: The links of this OAuth2RefreshToken.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def client_id(self):
        """Gets the client_id of this OAuth2RefreshToken.  # noqa: E501


        :return: The client_id of this OAuth2RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OAuth2RefreshToken.


        :param client_id: The client_id of this OAuth2RefreshToken.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def created(self):
        """Gets the created of this OAuth2RefreshToken.  # noqa: E501


        :return: The created of this OAuth2RefreshToken.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OAuth2RefreshToken.


        :param created: The created of this OAuth2RefreshToken.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this OAuth2RefreshToken.  # noqa: E501


        :return: The created_by of this OAuth2RefreshToken.  # noqa: E501
        :rtype: OAuth2Actor
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OAuth2RefreshToken.


        :param created_by: The created_by of this OAuth2RefreshToken.  # noqa: E501
        :type: OAuth2Actor
        """

        self._created_by = created_by

    @property
    def expires_at(self):
        """Gets the expires_at of this OAuth2RefreshToken.  # noqa: E501


        :return: The expires_at of this OAuth2RefreshToken.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this OAuth2RefreshToken.


        :param expires_at: The expires_at of this OAuth2RefreshToken.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def id(self):
        """Gets the id of this OAuth2RefreshToken.  # noqa: E501


        :return: The id of this OAuth2RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2RefreshToken.


        :param id: The id of this OAuth2RefreshToken.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issuer(self):
        """Gets the issuer of this OAuth2RefreshToken.  # noqa: E501


        :return: The issuer of this OAuth2RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this OAuth2RefreshToken.


        :param issuer: The issuer of this OAuth2RefreshToken.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def last_updated(self):
        """Gets the last_updated of this OAuth2RefreshToken.  # noqa: E501


        :return: The last_updated of this OAuth2RefreshToken.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this OAuth2RefreshToken.


        :param last_updated: The last_updated of this OAuth2RefreshToken.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def scopes(self):
        """Gets the scopes of this OAuth2RefreshToken.  # noqa: E501


        :return: The scopes of this OAuth2RefreshToken.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this OAuth2RefreshToken.


        :param scopes: The scopes of this OAuth2RefreshToken.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def status(self):
        """Gets the status of this OAuth2RefreshToken.  # noqa: E501


        :return: The status of this OAuth2RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OAuth2RefreshToken.


        :param status: The status of this OAuth2RefreshToken.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "REVOKED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this OAuth2RefreshToken.  # noqa: E501


        :return: The user_id of this OAuth2RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OAuth2RefreshToken.


        :param user_id: The user_id of this OAuth2RefreshToken.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(OAuth2RefreshToken, dict):
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
        if not isinstance(other, OAuth2RefreshToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
