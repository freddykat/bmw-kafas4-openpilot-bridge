"""Semantic interfaces for passive BMW sensor integration.

These structures intentionally contain no vehicle-control transport logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Validity(str, Enum):
  UNKNOWN = "unknown"
  VALID = "valid"
  DEGRADED = "degraded"
  INVALID = "invalid"


@dataclass(frozen=True)
class ObjectObservation:
  track_id: int
  classification: str
  x_m: float
  y_m: float
  vx_mps: Optional[float] = None
  vy_mps: Optional[float] = None
  confidence: float = 0.0
  source: str = "unknown"


@dataclass(frozen=True)
class LaneBoundaryObservation:
  side: str
  lateral_offset_m: Optional[float] = None
  heading_rad: Optional[float] = None
  curvature_1pm: Optional[float] = None
  confidence: float = 0.0


@dataclass(frozen=True)
class BMWKafasObservation:
  timestamp_ns: int
  validity: Validity = Validity.UNKNOWN
  objects: tuple[ObjectObservation, ...] = ()
  lanes: tuple[LaneBoundaryObservation, ...] = ()
  traffic_signs: tuple[str, ...] = ()
  traffic_lights: tuple[str, ...] = ()
  notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class RadarTrack:
  track_id: int
  range_m: float
  azimuth_rad: float
  range_rate_mps: float
  confidence: float = 0.0
  source: str = "unknown"


@dataclass(frozen=True)
class FrontRadarState:
  timestamp_ns: int
  validity: Validity = Validity.UNKNOWN
  tracks: tuple[RadarTrack, ...] = ()


@dataclass(frozen=True)
class SurroundRadarState:
  timestamp_ns: int
  validity: Validity = Validity.UNKNOWN
  front_left: tuple[RadarTrack, ...] = ()
  front_right: tuple[RadarTrack, ...] = ()
  rear_left: tuple[RadarTrack, ...] = ()
  rear_right: tuple[RadarTrack, ...] = ()


@dataclass(frozen=True)
class BMWVehicleDynamics:
  timestamp_ns: int
  speed_mps: Optional[float] = None
  yaw_rate_rps: Optional[float] = None
  lateral_accel_mps2: Optional[float] = None
  front_steering_angle_rad: Optional[float] = None
  rear_steering_angle_rad: Optional[float] = None
  rear_steering_rate_rps: Optional[float] = None
  rear_steering_available: Optional[bool] = None
  rear_steering_fault: Optional[bool] = None
  estimated_curvature_1pm: Optional[float] = None
  validity: Validity = Validity.UNKNOWN


@dataclass(frozen=True)
class FrontFusionState:
  timestamp_ns: int
  objects: tuple[ObjectObservation, ...] = ()
  lane_sources: tuple[str, ...] = ()
  source_mask: tuple[str, ...] = ()
  disagreement_flags: tuple[str, ...] = ()
  metadata: dict[str, str] = field(default_factory=dict)
