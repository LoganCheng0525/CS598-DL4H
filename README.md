# Reproducing and Extending ViewXGen

This repository contains the code and scripts needed to reproduce and extend the ViewXGen model from:

Lee, H., Lee, D. Y., Kim, W., Kim, J.-H., Kim, T., Kim, J., Sunwoo, L., & Choi, E. (2023). Vision-Language Generative Model for View-Specific Chest X-ray Generation. arXiv:2302.12172.

```bash
# Download JPEG images (≈500 GB)
wget -r -N -c -np \
  --user logancheng --ask-password \
  https://physionet.org/files/mimic-cxr-jpg/2.1.0/

# Download accompanying DICOM metadata & reports (≈4 TB, excluding .dcm files)
wget -r -N -c -np --reject dcm \
  --user logancheng --ask-password \
  https://physionet.org/files/mimic-cxr/2.1.0/
```

## Demo
https://mediaspace.illinois.edu/media/t/1_4xm4f30e

## Installation
Follow these steps to set up and run the ScholarScope Dashboard on your local machine. The instructions assume that MySQL, MongoDB, and Neo4j are already installed and populated with the Academic World dataset.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CS411DSO-SP25/Anthony_Logan.git

2. **Install Required Python Packages**: Navigate to the project directory and install dependencies:
   ```bash
   pip install -r requirements.txt

3. **Create a `.env` file**:
In the project root, create a file named `.env` with the following contents (replace the placeholders with your own credentials):
```dotenv
# MySQL
MYSQL_HOST=localhost
MYSQL_USER=<your_mysql_username>
MYSQL_PASSWORD=<your_mysql_password>
MYSQL_DATABASE=academicworld

# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=<your_neo4j_username>
NEO4J_PASSWORD=<your_neo4j_password>

# MongoDB
MONGO_URI=mongodb://localhost:27017
MONGO_DATABASE=academicworld
```
4. **Run the Application**:
   ```bash
   python app.py
The dashboard will be available at `http://127.0.0.1:8050` in your web browser.
