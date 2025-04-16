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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_api_core_v1_typed_local_object_reference import IoK8sApiCoreV1TypedLocalObjectReference
from kubeflow.trainer.models.io_k8s_api_core_v1_typed_object_reference import IoK8sApiCoreV1TypedObjectReference
from kubeflow.trainer.models.io_k8s_api_core_v1_volume_resource_requirements import IoK8sApiCoreV1VolumeResourceRequirements
from kubeflow.trainer.models.io_k8s_apimachinery_pkg_apis_meta_v1_label_selector import IoK8sApimachineryPkgApisMetaV1LabelSelector
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1PersistentVolumeClaimSpec(BaseModel):
    """
    PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes
    """ # noqa: E501
    access_modes: Optional[List[StrictStr]] = Field(default=None, description="accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1", alias="accessModes")
    data_source: Optional[IoK8sApiCoreV1TypedLocalObjectReference] = Field(default=None, description="dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.", alias="dataSource")
    data_source_ref: Optional[IoK8sApiCoreV1TypedObjectReference] = Field(default=None, description="dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef   allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef   preserves all values, and generates an error if a disallowed value is   specified. * While dataSource only allows local objects, dataSourceRef allows objects   in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.", alias="dataSourceRef")
    resources: Optional[IoK8sApiCoreV1VolumeResourceRequirements] = Field(default=None, description="resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources")
    selector: Optional[IoK8sApimachineryPkgApisMetaV1LabelSelector] = Field(default=None, description="selector is a label query over volumes to consider for binding.")
    storage_class_name: Optional[StrictStr] = Field(default=None, description="storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1", alias="storageClassName")
    volume_attributes_class_name: Optional[StrictStr] = Field(default=None, description="volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default).", alias="volumeAttributesClassName")
    volume_mode: Optional[StrictStr] = Field(default=None, description="volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  Possible enum values:  - `\"Block\"` means the volume will not be formatted with a filesystem and will remain a raw block device.  - `\"Filesystem\"` means the volume will be or is formatted with a filesystem.", alias="volumeMode")
    volume_name: Optional[StrictStr] = Field(default=None, description="volumeName is the binding reference to the PersistentVolume backing this claim.", alias="volumeName")
    __properties: ClassVar[List[str]] = ["accessModes", "dataSource", "dataSourceRef", "resources", "selector", "storageClassName", "volumeAttributesClassName", "volumeMode", "volumeName"]

    @field_validator('access_modes')
    def access_modes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ReadOnlyMany', 'ReadWriteMany', 'ReadWriteOnce', 'ReadWriteOncePod']):
                raise ValueError("each list item must be one of ('ReadOnlyMany', 'ReadWriteMany', 'ReadWriteOnce', 'ReadWriteOncePod')")
        return value

    @field_validator('volume_mode')
    def volume_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Block', 'Filesystem']):
            raise ValueError("must be one of enum values ('Block', 'Filesystem')")
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
        """Create an instance of IoK8sApiCoreV1PersistentVolumeClaimSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data_source
        if self.data_source:
            _dict['dataSource'] = self.data_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_source_ref
        if self.data_source_ref:
            _dict['dataSourceRef'] = self.data_source_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1PersistentVolumeClaimSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessModes": obj.get("accessModes"),
            "dataSource": IoK8sApiCoreV1TypedLocalObjectReference.from_dict(obj["dataSource"]) if obj.get("dataSource") is not None else None,
            "dataSourceRef": IoK8sApiCoreV1TypedObjectReference.from_dict(obj["dataSourceRef"]) if obj.get("dataSourceRef") is not None else None,
            "resources": IoK8sApiCoreV1VolumeResourceRequirements.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "selector": IoK8sApimachineryPkgApisMetaV1LabelSelector.from_dict(obj["selector"]) if obj.get("selector") is not None else None,
            "storageClassName": obj.get("storageClassName"),
            "volumeAttributesClassName": obj.get("volumeAttributesClassName"),
            "volumeMode": obj.get("volumeMode"),
            "volumeName": obj.get("volumeName")
        })
        return _obj


