# KAFAS evolution and donor selection

This document separates verified architectural facts from naming shorthand used during research.

## F-series baseline

Earlier F-series KAFAS systems use a forward camera/control-unit architecture for functions such as lane-departure warning and road-sign recognition. They belong to the F-series electrical architecture and should not be treated as plug-compatible with later G-series systems.

## Early G30/G12 generation

BMW technical documentation for the early G30 explicitly identifies a **KAFAS stereo camera**, inherited from the G12. It is a key sensor for frontal collision warning, pedestrian protection, lane-departure warning and road-sign recognition, and supports ACC, traffic-jam assistance, active lane keeping and intersection warning.

BMW also documents 5AT lane/traffic-jam functions using **five radar sensors plus the KAFAS stereo camera**.

## Later KAFAS HIGH / MID naming

BMW parts and service material uses MID/HIGH variants in later generations. We must not assume that every module casually sold as “KAFAS4” has the same optics, interfaces, firmware, feature set or dependencies.

Therefore `KAFAS4 HIGH` is currently a project target class, not yet a validated part number.

## Donor-selection rule

Prefer a coherent donor set over individually cheap modules:

- same platform family,
- compatible build period,
- same ADAS option family,
- known VIN if possible,
- KAFAS + front full-range radar + four side radars together,
- SAS/BDC information retained for bench reference even if those ECUs are not installed in the F13.

Do not buy a camera solely because a listing says `KAFAS4`.

## What we want from KAFAS

The bridge does not require raw camera frames to be useful. Useful semantic observations include:

- lane boundaries / lane confidence,
- tracked frontal objects,
- object class and confidence,
- estimated object range where exposed,
- pedestrians/cyclists,
- traffic-sign observations,
- traffic-control observations if exposed by the selected generation,
- camera validity/degradation state,
- calibration state.

Raw/stereo depth is a research bonus, not a requirement.

## Fusion philosophy

Comma/openpilot perception and KAFAS remain independent evidence sources. Radar supplies complementary physical range/range-rate evidence. The bridge preserves provenance and confidence rather than pretending all observations came from one sensor.

```text
Comma perception ----+
                     |
KAFAS observations ---+--> FrontFusionState --> openpilot-facing adapters
                     |
front radar ---------+
                     |
side radars ---------+--> SurroundRadarState / scene context
```

## Current gate

No KAFAS or radar part number becomes `validated` until we can document:

1. exact identity,
2. connector/power requirements,
3. network topology,
4. repeatable boot,
5. repeatable useful output,
6. coding/calibration dependencies,
7. capture/replay evidence.