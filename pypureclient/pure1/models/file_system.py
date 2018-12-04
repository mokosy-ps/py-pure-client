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

from pypureclient.pure1.models.arrays_built_in import ArraysBuiltIn  # noqa: F401,E501
from pypureclient.pure1.models.fixed_reference import FixedReference  # noqa: F401,E501
from pypureclient.pure1.models.http import Http  # noqa: F401,E501
from pypureclient.pure1.models.nfs import Nfs  # noqa: F401,E501
from pypureclient.pure1.models.smb import Smb  # noqa: F401,E501


class FileSystem(object):
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
        'name': 'str',
        'arrays': 'list[FixedReference]',
        'created': 'int',
        'destroyed': 'bool',
        'fast_remove_directory_enabled': 'bool',
        'hard_limit_enabled': 'bool',
        'http': 'Http',
        'nfs': 'Nfs',
        'provisioned': 'int',
        'smb': 'Smb',
        'snapshot_directory_enabled': 'bool'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'created': 'created',
        'destroyed': 'destroyed',
        'fast_remove_directory_enabled': 'fast_remove_directory_enabled',
        'hard_limit_enabled': 'hard_limit_enabled',
        'http': 'http',
        'nfs': 'nfs',
        'provisioned': 'provisioned',
        'smb': 'smb',
        'snapshot_directory_enabled': 'snapshot_directory_enabled'
    }

    def __init__(self, as_of=None, id=None, name=None, arrays=None, created=None, destroyed=None, fast_remove_directory_enabled=None, hard_limit_enabled=None, http=None, nfs=None, provisioned=None, smb=None, snapshot_directory_enabled=None):  # noqa: E501
        """FileSystem - a model defined in Swagger"""  # noqa: E501

        self._as_of = None
        self._id = None
        self._name = None
        self._arrays = None
        self._created = None
        self._destroyed = None
        self._fast_remove_directory_enabled = None
        self._hard_limit_enabled = None
        self._http = None
        self._nfs = None
        self._provisioned = None
        self._smb = None
        self._snapshot_directory_enabled = None
        self.discriminator = None

        self.as_of = as_of
        self.id = id
        self.name = name
        self.arrays = arrays
        self.created = created
        self.destroyed = destroyed
        self.fast_remove_directory_enabled = fast_remove_directory_enabled
        self.hard_limit_enabled = hard_limit_enabled
        self.http = http
        self.nfs = nfs
        self.provisioned = provisioned
        self.smb = smb
        self.snapshot_directory_enabled = snapshot_directory_enabled

    @property
    def as_of(self):
        """Gets the as_of of this FileSystem.  # noqa: E501

        The freshness of the data (timestamp in millis since epoch)  # noqa: E501

        :return: The as_of of this FileSystem.  # noqa: E501
        :rtype: int
        """
        return self._as_of

    @as_of.setter
    def as_of(self, as_of):
        """Sets the as_of of this FileSystem.

        The freshness of the data (timestamp in millis since epoch)  # noqa: E501

        :param as_of: The as_of of this FileSystem.  # noqa: E501
        :type: int
        """
        if as_of is None:
            raise ValueError("Invalid value for `as_of`, must not be `None`")  # noqa: E501

        self._as_of = as_of

    @property
    def id(self):
        """Gets the id of this FileSystem.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this FileSystem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileSystem.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this FileSystem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FileSystem.  # noqa: E501

        A non-modifiable, locally unique name chosen by the system.  # noqa: E501

        :return: The name of this FileSystem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSystem.

        A non-modifiable, locally unique name chosen by the system.  # noqa: E501

        :param name: The name of this FileSystem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def arrays(self):
        """Gets the arrays of this FileSystem.  # noqa: E501

        The list of arrays where this resource exists. Many resources are on a single array, but some resources - for example pods - can be stretched across multiple arrays.  # noqa: E501

        :return: The arrays of this FileSystem.  # noqa: E501
        :rtype: list[FixedReference]
        """
        return self._arrays

    @arrays.setter
    def arrays(self, arrays):
        """Sets the arrays of this FileSystem.

        The list of arrays where this resource exists. Many resources are on a single array, but some resources - for example pods - can be stretched across multiple arrays.  # noqa: E501

        :param arrays: The arrays of this FileSystem.  # noqa: E501
        :type: list[FixedReference]
        """

        self._arrays = arrays

    @property
    def created(self):
        """Gets the created of this FileSystem.  # noqa: E501

        Creation time in milliseconds since UNIX epoch.  # noqa: E501

        :return: The created of this FileSystem.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileSystem.

        Creation time in milliseconds since UNIX epoch.  # noqa: E501

        :param created: The created of this FileSystem.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def destroyed(self):
        """Gets the destroyed of this FileSystem.  # noqa: E501

        Is the file system destroyed? Default is false. Modifiable.  # noqa: E501

        :return: The destroyed of this FileSystem.  # noqa: E501
        :rtype: bool
        """
        return self._destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        """Sets the destroyed of this FileSystem.

        Is the file system destroyed? Default is false. Modifiable.  # noqa: E501

        :param destroyed: The destroyed of this FileSystem.  # noqa: E501
        :type: bool
        """

        self._destroyed = destroyed

    @property
    def fast_remove_directory_enabled(self):
        """Gets the fast_remove_directory_enabled of this FileSystem.  # noqa: E501

        Is fast remove directory enabled? Default is false. Modifiable.  # noqa: E501

        :return: The fast_remove_directory_enabled of this FileSystem.  # noqa: E501
        :rtype: bool
        """
        return self._fast_remove_directory_enabled

    @fast_remove_directory_enabled.setter
    def fast_remove_directory_enabled(self, fast_remove_directory_enabled):
        """Sets the fast_remove_directory_enabled of this FileSystem.

        Is fast remove directory enabled? Default is false. Modifiable.  # noqa: E501

        :param fast_remove_directory_enabled: The fast_remove_directory_enabled of this FileSystem.  # noqa: E501
        :type: bool
        """

        self._fast_remove_directory_enabled = fast_remove_directory_enabled

    @property
    def hard_limit_enabled(self):
        """Gets the hard_limit_enabled of this FileSystem.  # noqa: E501

        Is the file system's size a hard limit quota? Default is false.  # noqa: E501

        :return: The hard_limit_enabled of this FileSystem.  # noqa: E501
        :rtype: bool
        """
        return self._hard_limit_enabled

    @hard_limit_enabled.setter
    def hard_limit_enabled(self, hard_limit_enabled):
        """Sets the hard_limit_enabled of this FileSystem.

        Is the file system's size a hard limit quota? Default is false.  # noqa: E501

        :param hard_limit_enabled: The hard_limit_enabled of this FileSystem.  # noqa: E501
        :type: bool
        """

        self._hard_limit_enabled = hard_limit_enabled

    @property
    def http(self):
        """Gets the http of this FileSystem.  # noqa: E501

        HTTP configuration. Modifiable.  # noqa: E501

        :return: The http of this FileSystem.  # noqa: E501
        :rtype: Http
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this FileSystem.

        HTTP configuration. Modifiable.  # noqa: E501

        :param http: The http of this FileSystem.  # noqa: E501
        :type: Http
        """

        self._http = http

    @property
    def nfs(self):
        """Gets the nfs of this FileSystem.  # noqa: E501

        NFS configuration. Modifiable.  # noqa: E501

        :return: The nfs of this FileSystem.  # noqa: E501
        :rtype: Nfs
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """Sets the nfs of this FileSystem.

        NFS configuration. Modifiable.  # noqa: E501

        :param nfs: The nfs of this FileSystem.  # noqa: E501
        :type: Nfs
        """

        self._nfs = nfs

    @property
    def provisioned(self):
        """Gets the provisioned of this FileSystem.  # noqa: E501

        The provisioned size of the file system in bytes. Modifiable. Default is 0, meaning unlimited.  # noqa: E501

        :return: The provisioned of this FileSystem.  # noqa: E501
        :rtype: int
        """
        return self._provisioned

    @provisioned.setter
    def provisioned(self, provisioned):
        """Sets the provisioned of this FileSystem.

        The provisioned size of the file system in bytes. Modifiable. Default is 0, meaning unlimited.  # noqa: E501

        :param provisioned: The provisioned of this FileSystem.  # noqa: E501
        :type: int
        """

        self._provisioned = provisioned

    @property
    def smb(self):
        """Gets the smb of this FileSystem.  # noqa: E501

        SMB configuration. Modifiable.  # noqa: E501

        :return: The smb of this FileSystem.  # noqa: E501
        :rtype: Smb
        """
        return self._smb

    @smb.setter
    def smb(self, smb):
        """Sets the smb of this FileSystem.

        SMB configuration. Modifiable.  # noqa: E501

        :param smb: The smb of this FileSystem.  # noqa: E501
        :type: Smb
        """

        self._smb = smb

    @property
    def snapshot_directory_enabled(self):
        """Gets the snapshot_directory_enabled of this FileSystem.  # noqa: E501

        Is snapshot directory enabled? Default is false. Modifiable.  # noqa: E501

        :return: The snapshot_directory_enabled of this FileSystem.  # noqa: E501
        :rtype: bool
        """
        return self._snapshot_directory_enabled

    @snapshot_directory_enabled.setter
    def snapshot_directory_enabled(self, snapshot_directory_enabled):
        """Sets the snapshot_directory_enabled of this FileSystem.

        Is snapshot directory enabled? Default is false. Modifiable.  # noqa: E501

        :param snapshot_directory_enabled: The snapshot_directory_enabled of this FileSystem.  # noqa: E501
        :type: bool
        """

        self._snapshot_directory_enabled = snapshot_directory_enabled

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
        if issubclass(FileSystem, dict):
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
        if not isinstance(other, FileSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
