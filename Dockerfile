
FROM python



COPY sifter.py /run

COPY requirements.txt /run
COPY requirementsFirst.txt /run
Run apt-get update
Run echo y | apt install portaudio19-dev 
Run pip install -r /run/requirementsFirst.txt
RUN pip install -r /run/requirements.txt

COPY Love_Galore.wav /run



#CMD [ “python", "run/sifter.py”, “run/Love_Galore.wav” ]