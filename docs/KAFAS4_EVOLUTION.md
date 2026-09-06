# KAFAS4 Evolution Plan

## Phase K0 — research inventory

Goal: identify the exact KAFAS4 HIGH and five-radar donor family before buying hardware.

Questions to close for each ECU/sensor:
- exact part number / HW generation / SW generation;
- power and wake requirements;
- CAN/local-CAN connectivity;
- automotive Ethernet / OABR / 100BASE-T1 topology;
- network-management dependencies;
- coding / CAFD / FSC requirements;
- calibration requirements;
- expected partner ECUs such as SAS/BDC;
- whether useful outputs remain available without those partners.

## Phase K1 — bench boot

Power KAFAS4 and radars on the bench with protected supplies and passive capture only.

Success criteria:
- repeatable boot;
- stable network presence;
- identified wake/network-management behavior;
- no vehicle-control outputs;
- capture format documented.

## Phase K2 — donor-network teaching

Use the minimum donor network necessary to observe normal sensor startup. SAS/BDC may be used on the bench as teacher/reference ECUs.

Then remove or substitute donor dependencies one at a time to determine the minimum context required for each sensor to operate.

## Phase K3 — semantic decoding

Create validated semantic outputs:

```text
BMWKafasObservation
FrontRadarState
SurroundRadarState
```

No signal is promoted from hypothesis to validated until supported by captures/replay tests.

## Phase K4 — sensor fusion

Fuse independent evidence from:
- Comma Four/openpilot perception;
- KAFAS4 HIGH;
- front LRR;
- four side radars.

Produce a `FrontFusionState` / world-state representation with source masks, timestamps, confidence and disagreement metrics.

## Phase K5 — F13 passive integration

Add read-only F13 vehicle dynamics from CAN/FlexRay as available and validated. Keep OEM ACC/chassis systems operating independently.

Special requirement: model Integral Active Steering / rear steering in effective-curvature validation.

## Phase K6 — replay and HIL

Build repeatable scenarios for:
- lead vehicle;
- cut-in/cut-out;
- adjacent-lane vehicles;
- crossing traffic;
- cyclist/pedestrian evidence where exposed;
- lane merge/split;
- degraded camera/radar validity;
- disagreement between Comma, KAFAS and radar;
- IAS rear-angle changes versus effective curvature.

Current project scope stops at passive/shadow/HIL validation.
