# Runaway Snack：Rotating Arm

## Align the default arm direction

The servo is mounted across the box, so the software applies an approximately
90-degree offset. The default positions are:

- REST: 1700 us, pointing toward the user
- ESCAPE: 1200 us, rotating away

Both positions remain inside the 1200–1800 us range already tested on the
assembled hardware. Check the actual direction with:

```bash
cd ~/Interactive-Lab-Hub/"Lab 4"
source .venv/bin/activate
python rotating_arm/rotating_arm.py align
```

The servo moves to and holds the default REST position (1700 us). If it points
toward the user, press `Ctrl+C` and continue with the sweep test. No change to the
servo cutout or body orientation is required.

For small software adjustments after the horn is reinstalled, test in 25–50 us
steps. For example:

```bash
python rotating_arm/rotating_arm.py align --rest-us 1675
python rotating_arm/rotating_arm.py sweep --rest-us 1675 --escape-us 1200
python rotating_arm/rotating_arm.py run --near 30 --far 10 --rest-us 1675 --escape-us 1200
```

Use the same `--rest-us` value for `align`, `sweep`, and `run`. Keep both pulse
widths within 1000–2000 us and stop immediately if the arm hits the enclosure or
the servo buzzes at an endpoint.
