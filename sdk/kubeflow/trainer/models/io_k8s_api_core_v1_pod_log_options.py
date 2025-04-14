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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1PodLogOptions(BaseModel):
    """
    PodLogOptions is the query options for a Pod's logs REST call.
    """ # noqa: E501
    api_version: Optional[StrictStr] = Field(default=None, description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", alias="apiVersion")
    container: Optional[StrictStr] = Field(default=None, description="The container for which to stream logs. Defaults to only container if there is one container in the pod.")
    follow: Optional[StrictBool] = Field(default=None, description="Follow the log stream of the pod. Defaults to false.")
    insecure_skip_tls_verify_backend: Optional[StrictBool] = Field(default=None, description="insecureSkipTLSVerifyBackend indicates that the apiserver should not confirm the validity of the serving certificate of the backend it is connecting to.  This will make the HTTPS connection between the apiserver and the backend insecure. This means the apiserver cannot verify the log data it is receiving came from the real kubelet.  If the kubelet is configured to verify the apiserver's TLS credentials, it does not mean the connection to the real kubelet is vulnerable to a man in the middle attack (e.g. an attacker could not intercept the actual log data coming from the real kubelet).", alias="insecureSkipTLSVerifyBackend")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    limit_bytes: Optional[StrictInt] = Field(default=None, description="If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit.", alias="limitBytes")
    previous: Optional[StrictBool] = Field(default=None, description="Return previous terminated container logs. Defaults to false.")
    since_seconds: Optional[StrictInt] = Field(default=None, description="A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified.", alias="sinceSeconds")
    since_time: Optional[datetime] = Field(default=None, description="An RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified.", alias="sinceTime")
    stream: Optional[StrictStr] = Field(default=None, description="Specify which container log stream to return to the client. Acceptable values are \"All\", \"Stdout\" and \"Stderr\". If not specified, \"All\" is used, and both stdout and stderr are returned interleaved. Note that when \"TailLines\" is specified, \"Stream\" can only be set to nil or \"All\".")
    tail_lines: Optional[StrictInt] = Field(default=None, description="If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime. Note that when \"TailLines\" is specified, \"Stream\" can only be set to nil or \"All\".", alias="tailLines")
    timestamps: Optional[StrictBool] = Field(default=None, description="If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false.")
    __properties: ClassVar[List[str]] = ["apiVersion", "container", "follow", "insecureSkipTLSVerifyBackend", "kind", "limitBytes", "previous", "sinceSeconds", "sinceTime", "stream", "tailLines", "timestamps"]

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
        """Create an instance of IoK8sApiCoreV1PodLogOptions from a JSON string"""
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
        """Create an instance of IoK8sApiCoreV1PodLogOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiVersion": obj.get("apiVersion"),
            "container": obj.get("container"),
            "follow": obj.get("follow"),
            "insecureSkipTLSVerifyBackend": obj.get("insecureSkipTLSVerifyBackend"),
            "kind": obj.get("kind"),
            "limitBytes": obj.get("limitBytes"),
            "previous": obj.get("previous"),
            "sinceSeconds": obj.get("sinceSeconds"),
            "sinceTime": obj.get("sinceTime"),
            "stream": obj.get("stream"),
            "tailLines": obj.get("tailLines"),
            "timestamps": obj.get("timestamps")
        })
        return _obj


