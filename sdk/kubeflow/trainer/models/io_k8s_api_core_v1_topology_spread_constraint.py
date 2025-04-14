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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_apimachinery_pkg_apis_meta_v1_label_selector import IoK8sApimachineryPkgApisMetaV1LabelSelector
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1TopologySpreadConstraint(BaseModel):
    """
    TopologySpreadConstraint specifies how to spread matching pods among the given topology.
    """ # noqa: E501
    label_selector: Optional[IoK8sApimachineryPkgApisMetaV1LabelSelector] = Field(default=None, description="LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.", alias="labelSelector")
    match_label_keys: Optional[List[StrictStr]] = Field(default=None, description="MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).", alias="matchLabelKeys")
    max_skew: StrictInt = Field(description="MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.", alias="maxSkew")
    min_domains: Optional[StrictInt] = Field(default=None, description="MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats \"global minimum\" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so \"global minimum\" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.", alias="minDomains")
    node_affinity_policy: Optional[StrictStr] = Field(default=None, description="NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  Possible enum values:  - `\"Honor\"` means use this scheduling directive when calculating pod topology spread skew.  - `\"Ignore\"` means ignore this scheduling directive when calculating pod topology spread skew.", alias="nodeAffinityPolicy")
    node_taints_policy: Optional[StrictStr] = Field(default=None, description="NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  Possible enum values:  - `\"Honor\"` means use this scheduling directive when calculating pod topology spread skew.  - `\"Ignore\"` means ignore this scheduling directive when calculating pod topology spread skew.", alias="nodeTaintsPolicy")
    topology_key: StrictStr = Field(description="TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a \"bucket\", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is \"kubernetes.io/hostname\", each Node is a domain of that topology. And, if TopologyKey is \"topology.kubernetes.io/zone\", each zone is a domain of that topology. It's a required field.", alias="topologyKey")
    when_unsatisfiable: StrictStr = Field(description="WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,   but giving higher precedence to topologies that would help reduce the   skew. A constraint is considered \"Unsatisfiable\" for an incoming pod if and only if every possible node assignment for that pod would violate \"MaxSkew\" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.  Possible enum values:  - `\"DoNotSchedule\"` instructs the scheduler not to schedule the pod when constraints are not satisfied.  - `\"ScheduleAnyway\"` instructs the scheduler to schedule the pod even if constraints are not satisfied.", alias="whenUnsatisfiable")
    __properties: ClassVar[List[str]] = ["labelSelector", "matchLabelKeys", "maxSkew", "minDomains", "nodeAffinityPolicy", "nodeTaintsPolicy", "topologyKey", "whenUnsatisfiable"]

    @field_validator('node_affinity_policy')
    def node_affinity_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Honor', 'Ignore']):
            raise ValueError("must be one of enum values ('Honor', 'Ignore')")
        return value

    @field_validator('node_taints_policy')
    def node_taints_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Honor', 'Ignore']):
            raise ValueError("must be one of enum values ('Honor', 'Ignore')")
        return value

    @field_validator('when_unsatisfiable')
    def when_unsatisfiable_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DoNotSchedule', 'ScheduleAnyway']):
            raise ValueError("must be one of enum values ('DoNotSchedule', 'ScheduleAnyway')")
        return value

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
        """Create an instance of IoK8sApiCoreV1TopologySpreadConstraint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of label_selector
        if self.label_selector:
            _dict['labelSelector'] = self.label_selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1TopologySpreadConstraint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "labelSelector": IoK8sApimachineryPkgApisMetaV1LabelSelector.from_dict(obj["labelSelector"]) if obj.get("labelSelector") is not None else None,
            "matchLabelKeys": obj.get("matchLabelKeys"),
            "maxSkew": obj.get("maxSkew") if obj.get("maxSkew") is not None else 0,
            "minDomains": obj.get("minDomains"),
            "nodeAffinityPolicy": obj.get("nodeAffinityPolicy"),
            "nodeTaintsPolicy": obj.get("nodeTaintsPolicy"),
            "topologyKey": obj.get("topologyKey") if obj.get("topologyKey") is not None else '',
            "whenUnsatisfiable": obj.get("whenUnsatisfiable")
        })
        return _obj


