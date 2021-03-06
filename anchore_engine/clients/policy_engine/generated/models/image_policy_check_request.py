# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ImagePolicyCheckRequest(object):
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
        'image_id': 'str',
        'tag': 'str',
        'user_id': 'str',
        'bundle': 'object'
    }

    attribute_map = {
        'image_id': 'image_id',
        'tag': 'tag',
        'user_id': 'user_id',
        'bundle': 'bundle'
    }

    def __init__(self, image_id=None, tag=None, user_id=None, bundle=None):  # noqa: E501
        """ImagePolicyCheckRequest - a model defined in Swagger"""  # noqa: E501

        self._image_id = None
        self._tag = None
        self._user_id = None
        self._bundle = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if tag is not None:
            self.tag = tag
        if user_id is not None:
            self.user_id = user_id
        if bundle is not None:
            self.bundle = bundle

    @property
    def image_id(self):
        """Gets the image_id of this ImagePolicyCheckRequest.  # noqa: E501


        :return: The image_id of this ImagePolicyCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImagePolicyCheckRequest.


        :param image_id: The image_id of this ImagePolicyCheckRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def tag(self):
        """Gets the tag of this ImagePolicyCheckRequest.  # noqa: E501


        :return: The tag of this ImagePolicyCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ImagePolicyCheckRequest.


        :param tag: The tag of this ImagePolicyCheckRequest.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def user_id(self):
        """Gets the user_id of this ImagePolicyCheckRequest.  # noqa: E501


        :return: The user_id of this ImagePolicyCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ImagePolicyCheckRequest.


        :param user_id: The user_id of this ImagePolicyCheckRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def bundle(self):
        """Gets the bundle of this ImagePolicyCheckRequest.  # noqa: E501


        :return: The bundle of this ImagePolicyCheckRequest.  # noqa: E501
        :rtype: object
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this ImagePolicyCheckRequest.


        :param bundle: The bundle of this ImagePolicyCheckRequest.  # noqa: E501
        :type: object
        """

        self._bundle = bundle

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImagePolicyCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
