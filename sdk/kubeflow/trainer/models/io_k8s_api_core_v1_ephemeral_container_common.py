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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_api_core_v1_container_port import IoK8sApiCoreV1ContainerPort
from kubeflow.trainer.models.io_k8s_api_core_v1_container_resize_policy import IoK8sApiCoreV1ContainerResizePolicy
from kubeflow.trainer.models.io_k8s_api_core_v1_env_from_source import IoK8sApiCoreV1EnvFromSource
from kubeflow.trainer.models.io_k8s_api_core_v1_env_var import IoK8sApiCoreV1EnvVar
from kubeflow.trainer.models.io_k8s_api_core_v1_lifecycle import IoK8sApiCoreV1Lifecycle
from kubeflow.trainer.models.io_k8s_api_core_v1_probe import IoK8sApiCoreV1Probe
from kubeflow.trainer.models.io_k8s_api_core_v1_resource_requirements import IoK8sApiCoreV1ResourceRequirements
from kubeflow.trainer.models.io_k8s_api_core_v1_security_context import IoK8sApiCoreV1SecurityContext
from kubeflow.trainer.models.io_k8s_api_core_v1_volume_device import IoK8sApiCoreV1VolumeDevice
from kubeflow.trainer.models.io_k8s_api_core_v1_volume_mount import IoK8sApiCoreV1VolumeMount
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1EphemeralContainerCommon(BaseModel):
    """
    EphemeralContainerCommon is a copy of all fields in Container to be inlined in EphemeralContainer. This separate type allows easy conversion from EphemeralContainer to Container and allows separate documentation for the fields of EphemeralContainer. When a new field is added to Container it must be added here as well.
    """ # noqa: E501
    args: Optional[List[StrictStr]] = Field(default=None, description="Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    command: Optional[List[StrictStr]] = Field(default=None, description="Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    env: Optional[List[IoK8sApiCoreV1EnvVar]] = Field(default=None, description="List of environment variables to set in the container. Cannot be updated.")
    env_from: Optional[List[IoK8sApiCoreV1EnvFromSource]] = Field(default=None, description="List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.", alias="envFrom")
    image: Optional[StrictStr] = Field(default=None, description="Container image name. More info: https://kubernetes.io/docs/concepts/containers/images")
    image_pull_policy: Optional[StrictStr] = Field(default=None, description="Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images  Possible enum values:  - `\"Always\"` means that kubelet always attempts to pull the latest image. Container will fail If the pull fails.  - `\"IfNotPresent\"` means that kubelet pulls if the image isn't present on disk. Container will fail if the image isn't present and the pull fails.  - `\"Never\"` means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn't present", alias="imagePullPolicy")
    lifecycle: Optional[IoK8sApiCoreV1Lifecycle] = Field(default=None, description="Lifecycle is not allowed for ephemeral containers.")
    liveness_probe: Optional[IoK8sApiCoreV1Probe] = Field(default=None, description="Probes are not allowed for ephemeral containers.", alias="livenessProbe")
    name: StrictStr = Field(description="Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.")
    ports: Optional[List[IoK8sApiCoreV1ContainerPort]] = Field(default=None, description="Ports are not allowed for ephemeral containers.")
    readiness_probe: Optional[IoK8sApiCoreV1Probe] = Field(default=None, description="Probes are not allowed for ephemeral containers.", alias="readinessProbe")
    resize_policy: Optional[List[IoK8sApiCoreV1ContainerResizePolicy]] = Field(default=None, description="Resources resize policy for the container.", alias="resizePolicy")
    resources: Optional[IoK8sApiCoreV1ResourceRequirements] = Field(default=None, description="Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.")
    restart_policy: Optional[StrictStr] = Field(default=None, description="Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers.", alias="restartPolicy")
    security_context: Optional[IoK8sApiCoreV1SecurityContext] = Field(default=None, description="Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.", alias="securityContext")
    startup_probe: Optional[IoK8sApiCoreV1Probe] = Field(default=None, description="Probes are not allowed for ephemeral containers.", alias="startupProbe")
    stdin: Optional[StrictBool] = Field(default=None, description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.")
    stdin_once: Optional[StrictBool] = Field(default=None, description="Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false", alias="stdinOnce")
    termination_message_path: Optional[StrictStr] = Field(default=None, description="Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.", alias="terminationMessagePath")
    termination_message_policy: Optional[StrictStr] = Field(default=None, description="Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.  Possible enum values:  - `\"FallbackToLogsOnError\"` will read the most recent contents of the container logs for the container status message when the container exits with an error and the terminationMessagePath has no contents.  - `\"File\"` is the default behavior and will set the container status message to the contents of the container's terminationMessagePath when the container exits.", alias="terminationMessagePolicy")
    tty: Optional[StrictBool] = Field(default=None, description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.")
    volume_devices: Optional[List[IoK8sApiCoreV1VolumeDevice]] = Field(default=None, description="volumeDevices is the list of block devices to be used by the container.", alias="volumeDevices")
    volume_mounts: Optional[List[IoK8sApiCoreV1VolumeMount]] = Field(default=None, description="Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.", alias="volumeMounts")
    working_dir: Optional[StrictStr] = Field(default=None, description="Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.", alias="workingDir")
    __properties: ClassVar[List[str]] = ["args", "command", "env", "envFrom", "image", "imagePullPolicy", "lifecycle", "livenessProbe", "name", "ports", "readinessProbe", "resizePolicy", "resources", "restartPolicy", "securityContext", "startupProbe", "stdin", "stdinOnce", "terminationMessagePath", "terminationMessagePolicy", "tty", "volumeDevices", "volumeMounts", "workingDir"]

    @field_validator('image_pull_policy')
    def image_pull_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Always', 'IfNotPresent', 'Never']):
            raise ValueError("must be one of enum values ('Always', 'IfNotPresent', 'Never')")
        return value

    @field_validator('termination_message_policy')
    def termination_message_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['FallbackToLogsOnError', 'File']):
            raise ValueError("must be one of enum values ('FallbackToLogsOnError', 'File')")
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
        """Create an instance of IoK8sApiCoreV1EphemeralContainerCommon from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in env (list)
        _items = []
        if self.env:
            for _item_env in self.env:
                if _item_env:
                    _items.append(_item_env.to_dict())
            _dict['env'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in env_from (list)
        _items = []
        if self.env_from:
            for _item_env_from in self.env_from:
                if _item_env_from:
                    _items.append(_item_env_from.to_dict())
            _dict['envFrom'] = _items
        # override the default output from pydantic by calling `to_dict()` of lifecycle
        if self.lifecycle:
            _dict['lifecycle'] = self.lifecycle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of liveness_probe
        if self.liveness_probe:
            _dict['livenessProbe'] = self.liveness_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item_ports in self.ports:
                if _item_ports:
                    _items.append(_item_ports.to_dict())
            _dict['ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of readiness_probe
        if self.readiness_probe:
            _dict['readinessProbe'] = self.readiness_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resize_policy (list)
        _items = []
        if self.resize_policy:
            for _item_resize_policy in self.resize_policy:
                if _item_resize_policy:
                    _items.append(_item_resize_policy.to_dict())
            _dict['resizePolicy'] = _items
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_context
        if self.security_context:
            _dict['securityContext'] = self.security_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of startup_probe
        if self.startup_probe:
            _dict['startupProbe'] = self.startup_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volume_devices (list)
        _items = []
        if self.volume_devices:
            for _item_volume_devices in self.volume_devices:
                if _item_volume_devices:
                    _items.append(_item_volume_devices.to_dict())
            _dict['volumeDevices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volume_mounts (list)
        _items = []
        if self.volume_mounts:
            for _item_volume_mounts in self.volume_mounts:
                if _item_volume_mounts:
                    _items.append(_item_volume_mounts.to_dict())
            _dict['volumeMounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1EphemeralContainerCommon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "args": obj.get("args"),
            "command": obj.get("command"),
            "env": [IoK8sApiCoreV1EnvVar.from_dict(_item) for _item in obj["env"]] if obj.get("env") is not None else None,
            "envFrom": [IoK8sApiCoreV1EnvFromSource.from_dict(_item) for _item in obj["envFrom"]] if obj.get("envFrom") is not None else None,
            "image": obj.get("image"),
            "imagePullPolicy": obj.get("imagePullPolicy"),
            "lifecycle": IoK8sApiCoreV1Lifecycle.from_dict(obj["lifecycle"]) if obj.get("lifecycle") is not None else None,
            "livenessProbe": IoK8sApiCoreV1Probe.from_dict(obj["livenessProbe"]) if obj.get("livenessProbe") is not None else None,
            "name": obj.get("name") if obj.get("name") is not None else '',
            "ports": [IoK8sApiCoreV1ContainerPort.from_dict(_item) for _item in obj["ports"]] if obj.get("ports") is not None else None,
            "readinessProbe": IoK8sApiCoreV1Probe.from_dict(obj["readinessProbe"]) if obj.get("readinessProbe") is not None else None,
            "resizePolicy": [IoK8sApiCoreV1ContainerResizePolicy.from_dict(_item) for _item in obj["resizePolicy"]] if obj.get("resizePolicy") is not None else None,
            "resources": IoK8sApiCoreV1ResourceRequirements.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "restartPolicy": obj.get("restartPolicy"),
            "securityContext": IoK8sApiCoreV1SecurityContext.from_dict(obj["securityContext"]) if obj.get("securityContext") is not None else None,
            "startupProbe": IoK8sApiCoreV1Probe.from_dict(obj["startupProbe"]) if obj.get("startupProbe") is not None else None,
            "stdin": obj.get("stdin"),
            "stdinOnce": obj.get("stdinOnce"),
            "terminationMessagePath": obj.get("terminationMessagePath"),
            "terminationMessagePolicy": obj.get("terminationMessagePolicy"),
            "tty": obj.get("tty"),
            "volumeDevices": [IoK8sApiCoreV1VolumeDevice.from_dict(_item) for _item in obj["volumeDevices"]] if obj.get("volumeDevices") is not None else None,
            "volumeMounts": [IoK8sApiCoreV1VolumeMount.from_dict(_item) for _item in obj["volumeMounts"]] if obj.get("volumeMounts") is not None else None,
            "workingDir": obj.get("workingDir")
        })
        return _obj


