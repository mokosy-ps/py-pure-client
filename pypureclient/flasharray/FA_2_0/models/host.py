# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_0 import models

class Host(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'chap': 'Chap',
        'connection_count': 'int',
        'host_group': 'ReferenceNoId',
        'iqns': 'list[str]',
        'nqns': 'list[str]',
        'personality': 'str',
        'port_connectivity': 'HostPortConnectivity',
        'preferred_arrays': 'list[Reference]',
        'space': 'Space',
        'wwns': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'chap': 'chap',
        'connection_count': 'connection_count',
        'host_group': 'host_group',
        'iqns': 'iqns',
        'nqns': 'nqns',
        'personality': 'personality',
        'port_connectivity': 'port_connectivity',
        'preferred_arrays': 'preferred_arrays',
        'space': 'space',
        'wwns': 'wwns'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        chap=None,  # type: models.Chap
        connection_count=None,  # type: int
        host_group=None,  # type: models.ReferenceNoId
        iqns=None,  # type: List[str]
        nqns=None,  # type: List[str]
        personality=None,  # type: str
        port_connectivity=None,  # type: models.HostPortConnectivity
        preferred_arrays=None,  # type: List[models.Reference]
        space=None,  # type: models.Space
        wwns=None,  # type: List[str]
    ):
        """
        Keyword args:
            name (str): A user-specified name. The name must be locally unique and can be changed.
            chap (Chap)
            connection_count (int): The number of volumes connected to the specified host.
            host_group (ReferenceNoId): The host group to which the host should be associated.
            iqns (list[str]): The iSCSI qualified name (IQN) associated with the host.
            nqns (list[str]): The NVMe Qualified Name (NQN) associated with the host.
            personality (str): Determines how the system tunes the array to ensure that it works optimally with the host. Set `personality` to the name of the host operating system or virtual memory system. Valid values are `aix`, `esxi`, `hitachi-vsp`, `hpux`, `oracle-vm-server`, `solaris`, and `vms`. If your system is not listed as one of the valid host personalities, do not set the option. By default, the personality is not set.
            port_connectivity (HostPortConnectivity)
            preferred_arrays (list[Reference]): For synchronous replication configurations, sets a host's preferred array to specify which array exposes active/optimized paths to that host. Enter multiple preferred arrays in comma-separated format. If a preferred array is set for a host, then the other arrays in the same pod will expose active/non-optimized paths to that host. If the host is in a host group, `preferred_arrays` cannot be set because host groups have their own preferred arrays. On a preferred array of a certain host, all the paths on all the ports (for both the primary and secondary controllers) are set up as A/O (active/optimized) paths, while on a non-preferred array, all the paths are A/N (Active/Non-optimized) paths.
            space (Space): Displays provisioned size and physical storage consumption information for the sum of all volumes connected to the specified host.
            wwns (list[str]): The Fibre Channel World Wide Name (WWN) associated with the host.
        """
        if name is not None:
            self.name = name
        if chap is not None:
            self.chap = chap
        if connection_count is not None:
            self.connection_count = connection_count
        if host_group is not None:
            self.host_group = host_group
        if iqns is not None:
            self.iqns = iqns
        if nqns is not None:
            self.nqns = nqns
        if personality is not None:
            self.personality = personality
        if port_connectivity is not None:
            self.port_connectivity = port_connectivity
        if preferred_arrays is not None:
            self.preferred_arrays = preferred_arrays
        if space is not None:
            self.space = space
        if wwns is not None:
            self.wwns = wwns

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Host`".format(key))
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
        if issubclass(Host, dict):
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
        if not isinstance(other, Host):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
