# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: unversioned
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_api_core_v1_object_field_selector import IoK8sApiCoreV1ObjectFieldSelector
from kubeflow.trainer.models.io_k8s_api_core_v1_resource_field_selector import IoK8sApiCoreV1ResourceFieldSelector
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1DownwardAPIVolumeFile(BaseModel):
    """
    DownwardAPIVolumeFile represents information to create the file containing the pod field
    """ # noqa: E501
    field_ref: Optional[IoK8sApiCoreV1ObjectFieldSelector] = Field(default=None, description="Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.", alias="fieldRef")
    mode: Optional[StrictInt] = Field(default=None, description="Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.")
    path: StrictStr = Field(description="Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'")
    resource_field_ref: Optional[IoK8sApiCoreV1ResourceFieldSelector] = Field(default=None, description="Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.", alias="resourceFieldRef")
    __properties: ClassVar[List[str]] = ["fieldRef", "mode", "path", "resourceFieldRef"]

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
        """Create an instance of IoK8sApiCoreV1DownwardAPIVolumeFile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of field_ref
        if self.field_ref:
            _dict['fieldRef'] = self.field_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_field_ref
        if self.resource_field_ref:
            _dict['resourceFieldRef'] = self.resource_field_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1DownwardAPIVolumeFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fieldRef": IoK8sApiCoreV1ObjectFieldSelector.from_dict(obj["fieldRef"]) if obj.get("fieldRef") is not None else None,
            "mode": obj.get("mode"),
            "path": obj.get("path") if obj.get("path") is not None else '',
            "resourceFieldRef": IoK8sApiCoreV1ResourceFieldSelector.from_dict(obj["resourceFieldRef"]) if obj.get("resourceFieldRef") is not None else None
        })
        return _obj


