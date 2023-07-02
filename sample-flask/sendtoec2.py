import docker
import subprocess

# Find the latest version of the image
client = docker.from_env()
images = client.images.list()

existing_versions = [float(image.tags[0].split(":")[1]) for image in images if image.tags and image.tags[0].startswith("tomerkul/myflask:")]

if existing_versions:
    latest_version = max(existing_versions)
    next_version = latest_version + 0.1
else:
    next_version = 1.0

# Format the version number to one decimal place
next_version = f"{next_version:.1f}"
IPadd = "44.202.126.178"
image_name = f"tomerkul/myflask:{latest_version}"

# Save the image as a tar file
subprocess.run(["docker", "save", "-o", "latest_image.tar", image_name], check=True)

# Transfer the tar file to the EC2 instance
subprocess.run(["scp", "-i", "/home/tomer/.ssh/mykeyVir", "-o", "StrictHostKeyChecking=no", "latest_image.tar", f"ec2-user@{IPadd}:/home/ec2-user"], check=True)

# Remove the local tar file
subprocess.run(["rm", "latest_image.tar"], check=True)

# Run the downloaded image on the EC2 instance
subprocess.run(["ssh", "-i", "/home/tomer/.ssh/mykeyVir", "-o", "StrictHostKeyChecking=no", f"ec2-user@{IPadd}", "docker", "load", "-i", "/home/ec2-user/latest_image.tar"], check=True)
subprocess.run(["ssh", "-i", "/home/tomer/.ssh/mykeyVir", "-o", "StrictHostKeyChecking=no", f"ec2-user@{IPadd}", "docker", "run", "-d", "-p", "5000:5000", image_name], check=True)
