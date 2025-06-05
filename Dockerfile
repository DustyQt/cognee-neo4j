# Use a base image that includes CUDA drivers and libraries
FROM nvidia/cuda:12.3.2-devel-ubuntu22.04

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip curl
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama serve
RUN ollama pull deepseek-r1:8b
RUN ollama pull nomic-embed-text

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt


# Copy the rest of the application
COPY . .

# Command to run the application
CMD [ "python3", "-u", "./src/main.py" ]