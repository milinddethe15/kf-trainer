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
from kubeflow.trainer.models.io_k8s_apimachinery_pkg_util_intstr_int_or_string import IoK8sApimachineryPkgUtilIntstrIntOrString
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1ServicePort(BaseModel):
    """
    ServicePort contains information on service's port.
    """ # noqa: E501
    app_protocol: Optional[StrictStr] = Field(default=None, description="The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-   * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.", alias="appProtocol")
    name: Optional[StrictStr] = Field(default=None, description="The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service.")
    node_port: Optional[StrictInt] = Field(default=None, description="The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport", alias="nodePort")
    port: StrictInt = Field(description="The port that will be exposed by this service.")
    protocol: Optional[StrictStr] = Field(default='TCP', description="The IP protocol for this port. Supports \"TCP\", \"UDP\", and \"SCTP\". Default is TCP.  Possible enum values:  - `\"SCTP\"` is the SCTP protocol.  - `\"TCP\"` is the TCP protocol.  - `\"UDP\"` is the UDP protocol.")
    target_port: Optional[IoK8sApimachineryPkgUtilIntstrIntOrString] = Field(default=None, description="Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service", alias="targetPort")
    __properties: ClassVar[List[str]] = ["appProtocol", "name", "nodePort", "port", "protocol", "targetPort"]

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SCTP', 'TCP', 'UDP']):
            raise ValueError("must be one of enum values ('SCTP', 'TCP', 'UDP')")
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
        """Create an instance of IoK8sApiCoreV1ServicePort from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target_port
        if self.target_port:
            _dict['targetPort'] = self.target_port.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1ServicePort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appProtocol": obj.get("appProtocol"),
            "name": obj.get("name"),
            "nodePort": obj.get("nodePort"),
            "port": obj.get("port") if obj.get("port") is not None else 0,
            "protocol": obj.get("protocol") if obj.get("protocol") is not None else 'TCP',
            "targetPort": IoK8sApimachineryPkgUtilIntstrIntOrString.from_dict(obj["targetPort"]) if obj.get("targetPort") is not None else None
        })
        return _obj


