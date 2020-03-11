# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from ...properties import Property
import pprint
import re

import six


class FileSystemReplicaLink(object):


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
        'lag': 'int',
        'members': 'list[ResourceWithLocation]',
        'paused': 'bool',
        'recovery_point': 'int',
        'status_details': 'str',
        'sources': 'list[ResourceWithLocation]',
        'targets': 'list[ResourceWithLocation]',
        'status': 'str'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'lag': 'lag',
        'members': 'members',
        'paused': 'paused',
        'recovery_point': 'recovery_point',
        'status_details': 'status_details',
        'sources': 'sources',
        'targets': 'targets',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(self, **kwargs):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            lag (int): Duration, in milliseconds, which represents how far behind the replication `target` is from the `source`.
            members (list[ResourceWithLocation]): The union of source and target resources in the replica link.
            paused (bool): Returns `true` if the replica link is paused.
            recovery_point (int): Time when the last replicated snapshot was created, in milliseconds since UNIX epoch. I.e. the recovery point if the file system is promoted.
            status_details (str): Detailed information about the status of the replica link when it is `unhealthy`.
            sources (list[ResourceWithLocation]): The source resources in the replica link.
            targets (list[ResourceWithLocation]): The target resources in the replica link.
            status (str): Status of the replica link. Values include `replicating`, `idle`, and `unhealthy`.
        """
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
        for arg in self.required_args:
            if arg not in kwargs:
                raise Exception("Required argument {} is missing".format(arg))

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileSystemReplicaLink`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
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
        if issubclass(FileSystemReplicaLink, dict):
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
        if not isinstance(other, FileSystemReplicaLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
