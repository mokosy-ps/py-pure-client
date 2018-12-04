# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](http://www.purestorage.com/)  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pypureclient.pure1.models.time_aware import TimeAware  # noqa: F401,E501


class BuiltInAsOf(object):
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
        'as_of': 'int',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, as_of=None, id=None, name=None):  # noqa: E501
        """BuiltInAsOf - a model defined in Swagger"""  # noqa: E501

        self._as_of = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.as_of = as_of
        self.id = id
        self.name = name

    @property
    def as_of(self):
        """Gets the as_of of this BuiltInAsOf.  # noqa: E501

        The freshness of the data (timestamp in millis since epoch)  # noqa: E501

        :return: The as_of of this BuiltInAsOf.  # noqa: E501
        :rtype: int
        """
        return self._as_of

    @as_of.setter
    def as_of(self, as_of):
        """Sets the as_of of this BuiltInAsOf.

        The freshness of the data (timestamp in millis since epoch)  # noqa: E501

        :param as_of: The as_of of this BuiltInAsOf.  # noqa: E501
        :type: int
        """
        if as_of is None:
            raise ValueError("Invalid value for `as_of`, must not be `None`")  # noqa: E501

        self._as_of = as_of

    @property
    def id(self):
        """Gets the id of this BuiltInAsOf.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this BuiltInAsOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BuiltInAsOf.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this BuiltInAsOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BuiltInAsOf.  # noqa: E501

        A non-modifiable, locally unique name chosen by the system.  # noqa: E501

        :return: The name of this BuiltInAsOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuiltInAsOf.

        A non-modifiable, locally unique name chosen by the system.  # noqa: E501

        :param name: The name of this BuiltInAsOf.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(BuiltInAsOf, dict):
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
        if not isinstance(other, BuiltInAsOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
