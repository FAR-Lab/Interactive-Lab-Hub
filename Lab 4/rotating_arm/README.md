# Runaway Snack：Rotating Arm

## Align the default arm direction

The servo body remains in its laser-cut opening. The visible arm direction is set
by re-indexing the removable black horn on the HS-318's 25-tooth output spline;
the servo body does not need to rotate. The default positions remain:

- REST: 1200 us
- ESCAPE: 1800 us

These are the endpoints already tested on the assembled hardware. Move to the
actual REST position with:

```bash
cd ~/Interactive-Lab-Hub/"Lab 4"
source .venv/bin/activate
python rotating_arm/rotating_arm.py align
```

The servo moves to and holds REST at 1200 us. Press `Ctrl+C` and disconnect power.
Remove only the horn's centre screw through the round access hole. Lift the black
horn and attached cardboard arm straight off the spline without moving the servo
body. Rotate the horn about six spline teeth (roughly 86 degrees) so the arm points
toward the user, press it back onto the spline, and reinstall the centre screw.
Then reconnect power and run `align` again to check the direction.

For small software adjustments after the horn is reinstalled, test in 25–50 us
steps. For example:

```bash
python rotating_arm/rotating_arm.py align --rest-us 1175
python rotating_arm/rotating_arm.py sweep --rest-us 1175 --escape-us 1800
python rotating_arm/rotating_arm.py run --near 30 --far 10 --rest-us 1175 --escape-us 1800
```

Use the same `--rest-us` value for `align`, `sweep`, and `run`. Keep both pulse
widths within 1000–2000 us and stop immediately if the arm hits the enclosure or
the servo buzzes at an endpoint.
