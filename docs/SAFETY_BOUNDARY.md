# Safety Boundary

## Current authority states

Only these states are permitted in the current project phase:

- `DISABLED`
- `SHADOW`
- `HIL_ONLY`

There is no `ACTIVE` vehicle-control state in this repository.

## Prohibited current capabilities

Do not implement or enable:

- live steering actuation;
- brake or throttle actuation;
- BMW DSC/EPS/IAS command injection;
- Panda safety bypasses;
- sendcan for BMW control;
- FlexRay transmit/MITM;
- suppression of OEM driver override/fault handling.

## Required validation ladder before any future authority discussion

1. Static interface tests.
2. Recorded-log replay.
3. Sensor disagreement analysis.
4. Simulation.
5. Hardware-in-the-loop.
6. Human review of transport and safety logic.
7. Closed-course validation.
8. Defined override/fault behavior.

## Mandatory future override classes

Any future control architecture must remove authority on at least:

- steering torque/driver override;
- brake application;
- accelerator override;
- stalk/gear state conflicts;
- stale or missing sensor messages;
- bus faults;
- FlexRay synchronization loss where relevant;
- ECU faults;
- KAFAS/radar invalidity;
- IAS/rear-steering fault or inconsistency.

This document is a design constraint, not a claim that future control is safe or production ready.
