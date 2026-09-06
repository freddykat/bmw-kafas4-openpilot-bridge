# BMW KAFAS4 OpenPilot Bridge

Experimental research project for integrating BMW KAFAS4 HIGH and a modern five-radar BMW sensor set with openpilot while preserving BMW F-series chassis systems.

## Scope

Primary target: BMW F-series, initially the F13 6 Series.

The project focuses on:
- passive sensor capture and decoding;
- KAFAS4 HIGH observation extraction;
- front long-range radar decoding;
- four side-radar decoding;
- sensor fusion into semantic vehicle/world-state interfaces;
- openpilot-facing adapters;
- replay, simulation and HIL validation;
- coexistence with OEM F-series ACC/ADAS during development;
- modeling F13 Integral Active Steering / rear-wheel steering as observed vehicle dynamics.

## Safety boundary

Current authority state: **DISABLED / SHADOW / HIL_ONLY**.

This repository does not enable live steering, braking, throttle, DSC, EPS, FlexRay actuation, sendcan or safety bypasses. Any future actuation work must pass staged simulation, replay, HIL, human review and closed-course validation.

## Candidate architecture

```text
Comma Four -----------\
                      \
KAFAS4 HIGH ------------> Front/World Fusion ---> openpilot
                        /
Front LRR -------------/
Front-side radars -----/
Rear-side radars ------/

F13 CAN/FlexRay ---> BMW vehicle dynamics state ---> fusion/openpilot

F13 OEM systems retained initially:
- KAFAS2 where fitted
- OEM FRR/ACC
- ICM
- DSC
- DME/EGS
- Integral Active Steering / rear-axle steering
```

## Design principle

The bridge normalizes BMW sensor and chassis information into semantic interfaces. The planner must not create BMW CAN frames or FlexRay slots directly.

```text
raw BMW transport
      |
      v
decoders / adapters
      |
      v
BMWKafasObservation
SurroundRadarState
FrontFusionState
BMWVehicleDynamics
      |
      v
openpilot-facing adapters
```

## Repository status

Early research/scaffolding phase. No production-ready BMW signal definitions are assumed until validated from bench captures, replay or vehicle logs.
