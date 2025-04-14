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
from kubeflow.trainer.models.io_k8s_apimachinery_pkg_api_resource_quantity import IoK8sApimachineryPkgApiResourceQuantity
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiAutoscalingV2MetricTarget(BaseModel):
    """
    MetricTarget defines the target value, average value, or average utilization of a specific metric
    """ # noqa: E501
    average_utilization: Optional[StrictInt] = Field(default=None, description="averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type", alias="averageUtilization")
    average_value: Optional[IoK8sApimachineryPkgApiResourceQuantity] = Field(default=None, description="averageValue is the target value of the average of the metric across all relevant pods (as a quantity)", alias="averageValue")
    type: StrictStr = Field(description="type represents whether the metric type is Utilization, Value, or AverageValue")
    value: Optional[IoK8sApimachineryPkgApiResourceQuantity] = Field(default=None, description="value is the target value of the metric (as a quantity).")
    __properties: ClassVar[List[str]] = ["averageUtilization", "averageValue", "type", "value"]

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
        """Create an instance of IoK8sApiAutoscalingV2MetricTarget from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of average_value
        if self.average_value:
            _dict['averageValue'] = self.average_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiAutoscalingV2MetricTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "averageUtilization": obj.get("averageUtilization"),
            "averageValue": IoK8sApimachineryPkgApiResourceQuantity.from_dict(obj["averageValue"]) if obj.get("averageValue") is not None else None,
            "type": obj.get("type") if obj.get("type") is not None else '',
            "value": IoK8sApimachineryPkgApiResourceQuantity.from_dict(obj["value"]) if obj.get("value") is not None else None
        })
        return _obj


