from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.iho.int/S-100/profile/s100_gmlProfile"


class ComplianceLevelValue(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class GmlProfileSchema:
    """
    This URI references the profile schema to which a GML application schema
    conforms.
    """
    class Meta:
        name = "gmlProfileSchema"
        namespace = "http://www.iho.int/S-100/profile/s100_gmlProfile"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ComplianceLevel:
    """
    Level 1 = Level 2 =
    """
    class Meta:
        name = "complianceLevel"
        namespace = "http://www.iho.int/S-100/profile/s100_gmlProfile"

    value: Optional[ComplianceLevelValue] = field(
        default=None
    )
