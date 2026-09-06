# F13 Integration

## Final vehicle policy

The BMW F13 remains the chassis authority while KAFAS4 becomes the target camera/perception ECU for the openpilot integration.

Final target:

```text
KAFAS4 HIGH + Comma Four/openpilot + F13 chassis state
```

KAFAS2 is **not** part of the final installed architecture. It is only a reference source for F-series functions, expected semantics, coding/FSC behavior and message-level reverse engineering.

Retain:
- ICM;
- DSC;
- DME / EGS;
- Integral Active Steering / rear-axle steering;
- body and gateway systems.

Do not depend on:
- KAFAS2;
- OEM F13 ACC decision logic;
- G-series SAS/BDC/DSC/EPS transplant.

## Replacement strategy

Do not start by forcing KAFAS4 to emulate KAFAS2 globally.

The preferred sequence is:
1. Boot KAFAS4 HIGH on the bench with the minimum donor context.
2. Identify native useful outputs: lanes, objects, signs, validity, diagnostics and calibration state.
3. Decode these into semantic observations for openpilot.
4. Determine which F13 functions, if any, still expect KAFAS2-specific messages or service behavior.
5. Implement only those required semantics in a narrow F13 compatibility adapter.
6. Validate with replay/HIL before any in-car integration.

This gives us a clean end-state where KAFAS4 is the real perception source rather than a KAFAS2 hidden behind another ECU.

## OEM ACC

OEM F13 ACC is not part of the target assistance architecture. If present during development, it may be logged passively as a benchmark, but the KAFAS4/openpilot stack must not require it for final operation.

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

Initial policy:

```text
openpilot / bridge -> observes vehicle dynamics
BMW OEM chassis   -> controls rear axle steering
```

No rear-steering command generation is part of the current project phase.

## Windshield integration

Preferred packaging:
- keep Comma Four intact;
- install only KAFAS4 HIGH as the BMW windshield camera in the final configuration;
- use a rigid hybrid F13/KAFAS4 carrier with repeatable X/Y/Z and pitch/yaw/roll;
- verify field of view, frit/mask, lens-to-glass distance, reflections, thermal behavior and calibration constraints.

No permanent KAFAS2 optical zone is required in the final design.
