# Architecture

## Goal

Use BMW KAFAS4 HIGH and a modern five-radar BMW sensor suite as independent perception sources for openpilot, while retaining F-series chassis control systems and OEM assistance during the research phase.

## Sensor paths

```text
Comma Four --------------------------> openpilot perception

KAFAS4 HIGH ---> kafas4d ------------> BMWKafasObservation --\
                                                              \
Front LRR -----> bmwlrrd ------------> RadarData --------------> frontfusiond ---> FrontFusionState
                                                                /
4 side radars -> surroundradard -----> SurroundRadarState -----/

F13 CAN/FlexRay -> bmwstated --------> BMWVehicleDynamics -----> world/fusion inputs
```

## Separation of concerns

1. Transport decoders know CAN, local CAN, automotive Ethernet and future validated FlexRay RX.
2. Semantic interfaces expose sensor meaning, validity, confidence and timestamps.
3. Fusion consumes semantic interfaces only.
4. openpilot adapters translate semantic state into openpilot-facing structures.
5. No planner component writes BMW transport frames directly.

## KAFAS4 role

KAFAS4 HIGH is treated as a BMW front-perception subsystem, not as a KAFAS2 emulator by default. Desired observations include lane boundaries, object tracks, classifications, traffic signs/lights where available, confidence/validity and range/depth-related estimates where exposed.

Raw stereo/depth access is a research question, not an assumption.

## Five-radar role

- Front long-range radar: primary absolute range and relative velocity source for forward targets.
- Front-left/front-right side radars: crossing traffic, adjacent-lane and near-front evidence.
- Rear-left/rear-right side radars: blind-zone, overtaking and rear-crossing evidence.

The four side radars should normally feed a surround/world representation rather than being forced into standard front RadarData.

## F13 coexistence

During development the F13 keeps its OEM chassis and assistance stack intact where present. KAFAS4 and the modern radars are additional sensors for the bridge/openpilot path.

The architecture explicitly accounts for Integral Active Steering / rear-wheel steering. Planner validation must use observed effective curvature and rear steering state, not a simple front-steer-only bicycle model.
