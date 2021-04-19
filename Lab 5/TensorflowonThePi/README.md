## Tensorflow on The Pi for Teachable Machines

A simple way to install Tensorflow to use with TeachableMachines models on the pi is the following:

1. Create a new virtual environment: ``python -m venv ~/tf_venv --system-site-packages``
1. Activate the environment: ``source ~/tf_venv/bin/activate``
1. Get the python wheel from GitHub: ``wget https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl``
1. The install the wheel with ``pip install tensorflow-2.4.0-cp37-none-linux_armv7l.whl``


After that it should just be running.
