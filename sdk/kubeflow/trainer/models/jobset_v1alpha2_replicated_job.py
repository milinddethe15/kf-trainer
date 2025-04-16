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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_api_batch_v1_job_template_spec import IoK8sApiBatchV1JobTemplateSpec
from kubeflow.trainer.models.jobset_v1alpha2_depends_on import JobsetV1alpha2DependsOn
from typing import Optional, Set
from typing_extensions import Self

class JobsetV1alpha2ReplicatedJob(BaseModel):
    """
    JobsetV1alpha2ReplicatedJob
    """ # noqa: E501
    depends_on: Optional[List[JobsetV1alpha2DependsOn]] = Field(default=None, description="DependsOn is an optional list that specifies the preceding ReplicatedJobs upon which the current ReplicatedJob depends. If specified, the ReplicatedJob will be created only after the referenced ReplicatedJobs reach their desired state. The Order of ReplicatedJobs is defined by their enumeration in the slice. Note, that the first ReplicatedJob in the slice cannot use the DependsOn API. Currently, only a single item is supported in the DependsOn list. If JobSet is suspended the all active ReplicatedJobs will be suspended. When JobSet is resumed the Job sequence starts again. This API is mutually exclusive with the StartupPolicy API.", alias="dependsOn")
    name: StrictStr = Field(description="Name is the name of the entry and will be used as a suffix for the Job name.")
    replicas: Optional[StrictInt] = Field(default=None, description="Replicas is the number of jobs that will be created from this ReplicatedJob's template. Jobs names will be in the format: <jobSet.name>-<spec.replicatedJob.name>-<job-index>")
    template: IoK8sApiBatchV1JobTemplateSpec = Field(description="Template defines the template of the Job that will be created.")
    __properties: ClassVar[List[str]] = ["dependsOn", "name", "replicas", "template"]

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
        """Create an instance of JobsetV1alpha2ReplicatedJob from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in depends_on (list)
        _items = []
        if self.depends_on:
            for _item_depends_on in self.depends_on:
                if _item_depends_on:
                    _items.append(_item_depends_on.to_dict())
            _dict['dependsOn'] = _items
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobsetV1alpha2ReplicatedJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dependsOn": [JobsetV1alpha2DependsOn.from_dict(_item) for _item in obj["dependsOn"]] if obj.get("dependsOn") is not None else None,
            "name": obj.get("name") if obj.get("name") is not None else '',
            "replicas": obj.get("replicas"),
            "template": IoK8sApiBatchV1JobTemplateSpec.from_dict(obj["template"]) if obj.get("template") is not None else None
        })
        return _obj


