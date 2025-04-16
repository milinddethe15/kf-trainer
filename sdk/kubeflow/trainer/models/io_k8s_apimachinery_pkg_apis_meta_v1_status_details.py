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
from kubeflow.trainer.models.io_k8s_apimachinery_pkg_apis_meta_v1_status_cause import IoK8sApimachineryPkgApisMetaV1StatusCause
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApimachineryPkgApisMetaV1StatusDetails(BaseModel):
    """
    StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined.
    """ # noqa: E501
    causes: Optional[List[IoK8sApimachineryPkgApisMetaV1StatusCause]] = Field(default=None, description="The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.")
    group: Optional[StrictStr] = Field(default=None, description="The group attribute of the resource associated with the status StatusReason.")
    kind: Optional[StrictStr] = Field(default=None, description="The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    name: Optional[StrictStr] = Field(default=None, description="The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).")
    retry_after_seconds: Optional[StrictInt] = Field(default=None, description="If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.", alias="retryAfterSeconds")
    uid: Optional[StrictStr] = Field(default=None, description="UID of the resource. (when there is a single resource which can be described). More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids")
    __properties: ClassVar[List[str]] = ["causes", "group", "kind", "name", "retryAfterSeconds", "uid"]

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
        """Create an instance of IoK8sApimachineryPkgApisMetaV1StatusDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in causes (list)
        _items = []
        if self.causes:
            for _item_causes in self.causes:
                if _item_causes:
                    _items.append(_item_causes.to_dict())
            _dict['causes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApimachineryPkgApisMetaV1StatusDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "causes": [IoK8sApimachineryPkgApisMetaV1StatusCause.from_dict(_item) for _item in obj["causes"]] if obj.get("causes") is not None else None,
            "group": obj.get("group"),
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "retryAfterSeconds": obj.get("retryAfterSeconds"),
            "uid": obj.get("uid")
        })
        return _obj


