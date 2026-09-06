# F13 Integration

## Initial vehicle policy

The BMW F13 remains the chassis authority during the research phase. The KAFAS4 + five-radar stack is added as an independent perception island for openpilot-facing research.

Retain initially where fitted/available:

- OEM F13 ACC / front radar path;
- KAFAS2 if present in a donor/retrofit configuration;
- ICM;
- DSC;
- DME / EGS;
- Integral Active Steering / rear-axle steering;
- body and gateway systems.

## OEM ACC coexistence

Do not remove OEM ACC only to make the KAFAS4 research stack work. During early phases, OEM ACC is a useful independent BMW longitudinal reference and fallback comparison source.

KAFAS4 is not assumed to electronically impersonate KAFAS2. Any later compatibility layer must be justified by captured message-level evidence and bench validation.

## Rear-axle steering

The F13 vehicle model must account for Integral Active Steering from the beginning.

Target semantic state:

```text
frontSteeringAngle
rearSteeringAngle
rearSteeringRate
rearSteeringAvailable
rearSteeringFault
yawRate
lateralAcceleration
vehicleSpeed
estimatedCurvature
```

The initial policy is observation only:

```text
openpilot / bridge -> observes vehicle dynamics
BMW OEM chassis   -> controls rear axle steering
```

No rear-steering command generation is part of the current project phase.

## Windshield integration concept

Preferred research packaging:

- keep Comma Four intact;
- mount KAFAS4 HIGH rigidly with controlled camera geometry;
- if KAFAS2 is retained during coexistence, give each camera a valid unobstructed optical zone;
- use a custom BMW-style shroud/carrier only after verifying field of view, frit/mask, lens-to-glass distance, heat and calibration constraints.

The KAFAS4 carrier must define repeatable X/Y/Z and pitch/yaw/roll. Arbitrary adhesive placement is not an acceptable final mounting method.
