# KAFAS4 as a KAFAS2 Replacement

## Objective

Use **KAFAS4 HIGH as the only BMW windshield perception ECU** in the final F13 architecture, together with Comma Four/openpilot.

KAFAS2 is a reverse-engineering reference, not a runtime dependency.

## Why this is preferable

A parallel KAFAS2 + KAFAS4 installation creates unnecessary optical, electrical and software complexity. It also encourages us to preserve an older ADAS architecture that openpilot is intended to replace.

The cleaner engineering target is:

```text
KAFAS4 HIGH
   |
   +--> native BMW perception extraction
   |
   +--> KAFAS4 bridge
            |
            +--> openpilot semantic observations
            |
            +--> optional F13 compatibility semantics
```

## Important distinction

"Replace KAFAS2" does **not** initially mean byte-for-byte ECU impersonation.

There are three possible compatibility levels:

### Level 0 — no KAFAS2 emulation
KAFAS4 only feeds openpilot. F13 vehicle state comes from existing chassis ECUs.

### Level 1 — semantic compatibility
The bridge derives F-series-compatible states where another F13 subsystem genuinely requires them, without pretending to be a full KAFAS2 ECU.

### Level 2 — protocol compatibility
Only if proven necessary, the bridge reproduces narrowly defined KAFAS2-facing messages/services. This must be based on captured traffic and bench validation.

Level 0/1 are preferred. Level 2 is a last resort.

## Engineering work packages

### WP1 — KAFAS2 reference map
Document the functions an F13/F10-era KAFAS2 can provide and which vehicle ECUs consume them. Separate camera perception from FSC/coding and chassis dependencies.

### WP2 — KAFAS4 native boot
Determine KAFAS4 HIGH power, ground, wake, network-management, Ethernet/CAN requirements, coding, FSC and calibration dependencies.

### WP3 — Native outputs
Identify useful outputs such as:
- lane boundaries / lane confidence;
- object tracks;
- pedestrian/vehicle classification;
- sign recognition;
- validity/degradation states;
- calibration status;
- diagnostic health.

### WP4 — openpilot adapter
Normalize KAFAS4 output into project semantic interfaces. Do not inject KAFAS data directly into the neural model unless a later research branch proves that useful.

### WP5 — F13 gap analysis
For every function expected from KAFAS2, classify it as:
- obsolete because openpilot replaces it;
- provided independently by an F13 ECU;
- useful only for cluster/HUD/body presentation;
- genuinely required for another chassis subsystem.

Only the final category justifies a compatibility adapter.

### WP6 — physical integration
Develop an F13 windshield carrier and shroud for KAFAS4 HIGH while retaining the Comma Four intact.

## Success criterion

The replacement is successful when the car can operate the intended supervised openpilot stack with:
- KAFAS4 HIGH installed;
- Comma Four installed;
- no KAFAS2 installed;
- no dependency on OEM F13 ACC decision logic;
- F13 chassis ECUs left responsible for their native low-level functions;
- KAFAS4 observations available to openpilot with validated timing, confidence and health information.

## Current safety state

DISABLED / SHADOW / HIL_ONLY. This document defines architecture and reverse-engineering work, not permission for live vehicle actuation.
