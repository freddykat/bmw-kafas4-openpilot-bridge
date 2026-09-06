# BMW KAFAS4 OpenPilot Bridge

Experimental research project for integrating BMW KAFAS4 HIGH with openpilot on BMW F-series vehicles, initially the F13 6 Series.

## Final target

The intended end-state is **KAFAS4 HIGH + Comma Four/openpilot** on the F13, with KAFAS4 replacing the role that KAFAS2 would otherwise occupy. KAFAS2 is treated only as a reference for expected F-series functions, coding behavior and vehicle-facing semantics; it is not a required ECU in the final car.

The project focuses on:
- passive sensor capture and decoding;
- KAFAS4 HIGH observation extraction;
- reverse-engineering the minimum environment KAFAS4 needs to boot, authenticate, calibrate and publish useful outputs;
- translating KAFAS4 observations into openpilot-facing semantic interfaces;
- preserving F13 chassis systems such as ICM, DSC, DME/EGS and Integral Active Steering;
- replay, simulation and HIL validation;
- designing a compatibility layer only where the F13 genuinely needs KAFAS2-like vehicle-facing behavior.

## Safety boundary

Current authority state: **DISABLED / SHADOW / HIL_ONLY**.

This repository does not enable live steering, braking, throttle, DSC, EPS, FlexRay actuation, sendcan or safety bypasses. Any future actuation work must pass staged simulation, replay, HIL, human review and closed-course validation.

## Target architecture

```text
Comma Four -------------------\
                               \
KAFAS4 HIGH --> KAFAS4 Bridge ---> Front/World Fusion ---> openpilot
                               /
F13 CAN/FlexRay --------------/

F13 chassis retained:
- ICM
- DSC
- DME / EGS
- Integral Active Steering / rear-axle steering
- body/gateway systems

Not required in final target:
- KAFAS2
- OEM F13 ACC decision logic
- G-series SAS/BDC/DSC/EPS transplant
```

## KAFAS4 replacement principle

The goal is **not** to make KAFAS4 pretend to be a KAFAS2 ECU unless a specific F13 subsystem requires that behavior.

Preferred approach:

```text
KAFAS4 native outputs
        |
        v
KAFAS4 decoder / state extractor
        |
        +--> openpilot semantic inputs
        |
        +--> optional F13 compatibility adapter
             only for functions that truly require it
```

This keeps KAFAS4 native where possible and confines any KAFAS2-compatibility work to a narrow, testable adapter.

## Repository status

Early research/scaffolding phase. No production-ready BMW signal definitions are assumed until validated from bench captures, replay or vehicle logs.
