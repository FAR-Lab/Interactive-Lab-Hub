# Runaway Snack：Rotating Arm

## Align the default arm direction

The visible arm direction depends on both the REST pulse and how the servo horn is
installed on the output spline. Keep the tested 1200–1800 us travel and align the
horn at the actual REST command:

```bash
cd ~/Interactive-Lab-Hub/"Lab 4"
source .venv/bin/activate
python rotating_arm/rotating_arm.py align
```

The servo moves to and holds the default REST position (1200 us). Press `Ctrl+C`,
disconnect power, remove the horn's centre screw, lift the horn without turning the
servo shaft, and reinstall the arm pointing toward the user. Tighten the centre
screw before reconnecting power.

For small software adjustments after the horn is reinstalled, test in 25–50 us
steps. For example:

```bash
python rotating_arm/rotating_arm.py align --rest-us 1250
python rotating_arm/rotating_arm.py sweep --rest-us 1250 --escape-us 1800
python rotating_arm/rotating_arm.py run --near 30 --far 10 --rest-us 1250 --escape-us 1800
```

Use the same `--rest-us` value for `align`, `sweep`, and `run`. Keep both pulse
widths within 1000–2000 us and stop immediately if the arm hits the enclosure or
the servo buzzes at an endpoint.
