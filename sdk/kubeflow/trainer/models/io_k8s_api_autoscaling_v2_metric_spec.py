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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_api_autoscaling_v2_container_resource_metric_source import IoK8sApiAutoscalingV2ContainerResourceMetricSource
from kubeflow.trainer.models.io_k8s_api_autoscaling_v2_external_metric_source import IoK8sApiAutoscalingV2ExternalMetricSource
from kubeflow.trainer.models.io_k8s_api_autoscaling_v2_object_metric_source import IoK8sApiAutoscalingV2ObjectMetricSource
from kubeflow.trainer.models.io_k8s_api_autoscaling_v2_pods_metric_source import IoK8sApiAutoscalingV2PodsMetricSource
from kubeflow.trainer.models.io_k8s_api_autoscaling_v2_resource_metric_source import IoK8sApiAutoscalingV2ResourceMetricSource
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiAutoscalingV2MetricSpec(BaseModel):
    """
    MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).
    """ # noqa: E501
    container_resource: Optional[IoK8sApiAutoscalingV2ContainerResourceMetricSource] = Field(default=None, description="containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.", alias="containerResource")
    external: Optional[IoK8sApiAutoscalingV2ExternalMetricSource] = Field(default=None, description="external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).")
    object: Optional[IoK8sApiAutoscalingV2ObjectMetricSource] = Field(default=None, description="object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).")
    pods: Optional[IoK8sApiAutoscalingV2PodsMetricSource] = Field(default=None, description="pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.")
    resource: Optional[IoK8sApiAutoscalingV2ResourceMetricSource] = Field(default=None, description="resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.")
    type: StrictStr = Field(description="type is the type of metric source.  It should be one of \"ContainerResource\", \"External\", \"Object\", \"Pods\" or \"Resource\", each mapping to a matching field in the object.")
    __properties: ClassVar[List[str]] = ["containerResource", "external", "object", "pods", "resource", "type"]

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
        """Create an instance of IoK8sApiAutoscalingV2MetricSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of container_resource
        if self.container_resource:
            _dict['containerResource'] = self.container_resource.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external
        if self.external:
            _dict['external'] = self.external.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pods
        if self.pods:
            _dict['pods'] = self.pods.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiAutoscalingV2MetricSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "containerResource": IoK8sApiAutoscalingV2ContainerResourceMetricSource.from_dict(obj["containerResource"]) if obj.get("containerResource") is not None else None,
            "external": IoK8sApiAutoscalingV2ExternalMetricSource.from_dict(obj["external"]) if obj.get("external") is not None else None,
            "object": IoK8sApiAutoscalingV2ObjectMetricSource.from_dict(obj["object"]) if obj.get("object") is not None else None,
            "pods": IoK8sApiAutoscalingV2PodsMetricSource.from_dict(obj["pods"]) if obj.get("pods") is not None else None,
            "resource": IoK8sApiAutoscalingV2ResourceMetricSource.from_dict(obj["resource"]) if obj.get("resource") is not None else None,
            "type": obj.get("type") if obj.get("type") is not None else ''
        })
        return _obj


