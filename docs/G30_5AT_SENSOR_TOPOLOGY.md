# G30 5AT sensor topology — research baseline

Status: research baseline; exact donor HW/SW/PNs remain unvalidated.

## Confirmed architectural facts

BMW G30 5AT documentation describes a front perception system using a KAFAS stereo camera and five radar sensors: front full-range ACC radar, front-left and front-right radar sensors, and two rear/side short-range radar sensors.

The G30 local-CAN architecture is not a single flat sensor bus. BMW documentation shows local CAN links between SAS and front-side radars, and a local radar network involving the primary/secondary lane-change-warning radar units. Local CAN runs at 500 kbit/s.

This matters for the bridge: we must discover the actual sensor-facing topology before assuming each radar can simply be attached to one generic CAN interface.

## Candidate bench topology

```text
KAFAS camera ---- automotive Ethernet / vehicle networks ----+
                                                             |
Front full-range radar --------------------------------------+--> donor reference network
                                                             |
SAS (bench teacher only) ------------------------------------+
   |                    |
 local CAN           local CAN
   |                    |
 front-right         front-left + side radar network
```

The final in-car target does NOT require donor SAS if we can reproduce only the minimum startup/network context needed by the sensors.

## Research sequence

1. Select one coherent G30/G31 donor generation and 5AT configuration.
2. Record exact VIN/build date and every donor sensor PN/HWEL/SWFL/CAFD available.
3. Obtain connector/pinout data before applying power.
4. Establish protected bench power, grounds, terminal/wake behaviour and current limits.
5. Capture passive CAN/Ethernet traffic with donor modules present.
6. Determine which module provides network management and sensor wake-up.
7. Remove/substitute donor dependencies one at a time.
8. Identify useful semantic outputs: object tracks, range/range-rate, lane geometry, classifications, validity and diagnostic/calibration state.
9. Only after repeatable replay/bench results promote a sensor to `validated` in the hardware manifest.

## Open questions

- Can KAFAS operate sufficiently without BDC/SAS after minimal network-management emulation?
- Is the front full-range radar independently usable, or does useful object output depend on SAS fusion?
- Which of the four side radars are primary nodes/gateways versus secondary local-CAN nodes?
- Which messages are raw detections, tracked objects, diagnostics, or fused results?
- Which signals require coding/FSC/calibration before useful output appears?
- Which automotive-Ethernet endpoints and addressing/network-management context are required?

## Safety

All initial work is passive/bench/replay. No vehicle actuator commands are part of this repository phase.