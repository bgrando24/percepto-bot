FROM python:3.9

# Install system dependencies for OpenCV
# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y libgl1-mesa-glx


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD [ "python3", "src/main.py" ]