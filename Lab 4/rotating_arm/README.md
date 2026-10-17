# Runaway Snack：Rotating Arm

## Default direction with the 90-degree replacement lid

The replacement lid rotates the HS-318 body 90 degrees while preserving the
original shaft location. Testing on the assembled box showed that 1200 us still
points about 40–45 degrees to the user's right, so the program applies the
remaining software offset:

- REST: 1700 us, pointing forward
- ESCAPE: 1200 us, moved to the side

Move to the REST position and check that the arm points toward the user:

```bash
cd ~/Interactive-Lab-Hub/"Lab 4"
source .venv/bin/activate
python rotating_arm/rotating_arm.py align
```

The servo moves to and holds REST at 1700 us. Press `Ctrl+C` after checking the
direction. The replacement lid supplies the main 90-degree correction and this
pulse offset supplies the remaining alignment; no horn re-indexing is required.

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
