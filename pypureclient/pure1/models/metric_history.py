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

from pypureclient.pure1.models.built_in_as_of import BuiltInAsOf  # noqa: F401,E501
from pypureclient.pure1.models.fixed_reference import FixedReference  # noqa: F401,E501


class MetricHistory(object):
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
        'aggregation': 'str',
        'data': 'list[list[float]]',
        'resolution': 'int',
        'resources': 'list[FixedReference]',
        'unit': 'str'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'aggregation': 'aggregation',
        'data': 'data',
        'resolution': 'resolution',
        'resources': 'resources',
        'unit': 'unit'
    }

    def __init__(self, as_of=None, id=None, name=None, aggregation=None, data=None, resolution=None, resources=None, unit=None):  # noqa: E501
        """MetricHistory - a model defined in Swagger"""  # noqa: E501

        self._as_of = None
        self._id = None
        self._name = None
        self._aggregation = None
        self._data = None
        self._resolution = None
        self._resources = None
        self._unit = None
        self.discriminator = None

        self.as_of = as_of
        self.id = id
        self.name = name
        self.aggregation = aggregation
        self.data = data
        self.resolution = resolution
        self.resources = resources
        self.unit = unit

    @property
    def as_of(self):
        """Gets the as_of of this MetricHistory.  # noqa: E501

        The freshness of the data (timestamp in millis since epoch)  # noqa: E501

        :return: The as_of of this MetricHistory.  # noqa: E501
        :rtype: int
        """
        return self._as_of

    @as_of.setter
    def as_of(self, as_of):
        """Sets the as_of of this MetricHistory.

        The freshness of the data (timestamp in millis since epoch)  # noqa: E501

        :param as_of: The as_of of this MetricHistory.  # noqa: E501
        :type: int
        """
        if as_of is None:
            raise ValueError("Invalid value for `as_of`, must not be `None`")  # noqa: E501

        self._as_of = as_of

    @property
    def id(self):
        """Gets the id of this MetricHistory.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this MetricHistory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricHistory.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this MetricHistory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MetricHistory.  # noqa: E501

        A non-modifiable, locally unique name chosen by the system.  # noqa: E501

        :return: The name of this MetricHistory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricHistory.

        A non-modifiable, locally unique name chosen by the system.  # noqa: E501

        :param name: The name of this MetricHistory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def aggregation(self):
        """Gets the aggregation of this MetricHistory.  # noqa: E501

        The aggregation of the metric data  # noqa: E501

        :return: The aggregation of this MetricHistory.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this MetricHistory.

        The aggregation of the metric data  # noqa: E501

        :param aggregation: The aggregation of this MetricHistory.  # noqa: E501
        :type: str
        """

        self._aggregation = aggregation

    @property
    def data(self):
        """Gets the data of this MetricHistory.  # noqa: E501

        The data points of the metric corresponding to the time window, resolution and aggregation. The points are returned in a nested array of 2-element arrays. For each of the 2-element array, the 1st element is the UTC millisecond epoch, and the 2nd element is the value, e.g. [[1519362000000, 11], [1519362030000, 21], ...]  # noqa: E501

        :return: The data of this MetricHistory.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MetricHistory.

        The data points of the metric corresponding to the time window, resolution and aggregation. The points are returned in a nested array of 2-element arrays. For each of the 2-element array, the 1st element is the UTC millisecond epoch, and the 2nd element is the value, e.g. [[1519362000000, 11], [1519362030000, 21], ...]  # noqa: E501

        :param data: The data of this MetricHistory.  # noqa: E501
        :type: list[list[float]]
        """

        self._data = data

    @property
    def resolution(self):
        """Gets the resolution of this MetricHistory.  # noqa: E501

        The resolution of the metric data in milliseconds  # noqa: E501

        :return: The resolution of this MetricHistory.  # noqa: E501
        :rtype: int
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this MetricHistory.

        The resolution of the metric data in milliseconds  # noqa: E501

        :param resolution: The resolution of this MetricHistory.  # noqa: E501
        :type: int
        """

        self._resolution = resolution

    @property
    def resources(self):
        """Gets the resources of this MetricHistory.  # noqa: E501

        The references to the resources that the metric data is for. For example, write-iops metric for an array will have one element in this list referencing the array entity. the write-iops from an array to a pod will contain two elements in this list - first element pointing to the array, and second element pointing to the pod.  # noqa: E501

        :return: The resources of this MetricHistory.  # noqa: E501
        :rtype: list[FixedReference]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this MetricHistory.

        The references to the resources that the metric data is for. For example, write-iops metric for an array will have one element in this list referencing the array entity. the write-iops from an array to a pod will contain two elements in this list - first element pointing to the array, and second element pointing to the pod.  # noqa: E501

        :param resources: The resources of this MetricHistory.  # noqa: E501
        :type: list[FixedReference]
        """

        self._resources = resources

    @property
    def unit(self):
        """Gets the unit of this MetricHistory.  # noqa: E501

        The unit of the metric data  # noqa: E501

        :return: The unit of this MetricHistory.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricHistory.

        The unit of the metric data  # noqa: E501

        :param unit: The unit of this MetricHistory.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if issubclass(MetricHistory, dict):
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
        if not isinstance(other, MetricHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
