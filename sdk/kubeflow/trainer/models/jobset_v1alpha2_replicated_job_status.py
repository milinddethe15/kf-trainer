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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class JobsetV1alpha2ReplicatedJobStatus(BaseModel):
    """
    ReplicatedJobStatus defines the observed ReplicatedJobs Readiness.
    """ # noqa: E501
    active: StrictInt = Field(description="Active is the number of child Jobs with at least 1 pod in a running or pending state which are not marked for deletion.")
    failed: StrictInt = Field(description="Failed is the number of failed child Jobs.")
    name: StrictStr = Field(description="Name of the ReplicatedJob.")
    ready: StrictInt = Field(description="Ready is the number of child Jobs where the number of ready pods and completed pods is greater than or equal to the total expected pod count for the Job (i.e., the minimum of job.spec.parallelism and job.spec.completions).")
    succeeded: StrictInt = Field(description="Succeeded is the number of successfully completed child Jobs.")
    suspended: StrictInt = Field(description="Suspended is the number of child Jobs which are in a suspended state.")
    __properties: ClassVar[List[str]] = ["active", "failed", "name", "ready", "succeeded", "suspended"]

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
        """Create an instance of JobsetV1alpha2ReplicatedJobStatus from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobsetV1alpha2ReplicatedJobStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active") if obj.get("active") is not None else 0,
            "failed": obj.get("failed") if obj.get("failed") is not None else 0,
            "name": obj.get("name") if obj.get("name") is not None else '',
            "ready": obj.get("ready") if obj.get("ready") is not None else 0,
            "succeeded": obj.get("succeeded") if obj.get("succeeded") is not None else 0,
            "suspended": obj.get("suspended") if obj.get("suspended") is not None else 0
        })
        return _obj


