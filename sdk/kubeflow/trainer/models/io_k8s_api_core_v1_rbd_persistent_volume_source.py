# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_api_core_v1_secret_reference import IoK8sApiCoreV1SecretReference
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1RBDPersistentVolumeSource(BaseModel):
    """
    Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.
    """ # noqa: E501
    fs_type: Optional[StrictStr] = Field(default=None, description="fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd", alias="fsType")
    image: StrictStr = Field(description="image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    keyring: Optional[StrictStr] = Field(default='/etc/ceph/keyring', description="keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    monitors: List[StrictStr] = Field(description="monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    pool: Optional[StrictStr] = Field(default='rbd', description="pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    read_only: Optional[StrictBool] = Field(default=None, description="readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it", alias="readOnly")
    secret_ref: Optional[IoK8sApiCoreV1SecretReference] = Field(default=None, description="secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it", alias="secretRef")
    user: Optional[StrictStr] = Field(default='admin', description="user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    __properties: ClassVar[List[str]] = ["fsType", "image", "keyring", "monitors", "pool", "readOnly", "secretRef", "user"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1RBDPersistentVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of secret_ref
        if self.secret_ref:
            _dict['secretRef'] = self.secret_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1RBDPersistentVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fsType": obj.get("fsType"),
            "image": obj.get("image") if obj.get("image") is not None else '',
            "keyring": obj.get("keyring") if obj.get("keyring") is not None else '/etc/ceph/keyring',
            "monitors": obj.get("monitors"),
            "pool": obj.get("pool") if obj.get("pool") is not None else 'rbd',
            "readOnly": obj.get("readOnly"),
            "secretRef": IoK8sApiCoreV1SecretReference.from_dict(obj["secretRef"]) if obj.get("secretRef") is not None else None,
            "user": obj.get("user") if obj.get("user") is not None else 'admin'
        })
        return _obj


