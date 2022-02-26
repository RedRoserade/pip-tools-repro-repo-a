pip install -U "pip<22" "pip-tools<6.3.0"

pip-compile requirements.in --output-file requirements-6.2.X.txt
