FROM python:latest
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set the working directory
WORKDIR /app

# Copy only necessary files
COPY SimpleTimeService.py requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install  -r /app/requirements.txt

# Change ownership and switch to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "SimpleTimeService.py"]