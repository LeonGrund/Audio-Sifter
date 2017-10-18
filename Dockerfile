
FROM hypriot/rpi-python



COPY sifter.py /run

COPY requirements.txt /run
RUN pip install -r /run/requirements.txt

COPY Love_Galore.wav /run



CMD [ “python", "run/sifter.py”, “run/Love_Galore.wav” ]