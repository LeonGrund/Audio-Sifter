
FROM hypriot/rpi-python

COPY sifter.py /run

COPY requirements.txt /run

COPY Love_Galore.wav /run

RUN pip install -r requirements.txt

CMD [ “python", "run/sifter.py”, “run/Love_Galore.wav” ]