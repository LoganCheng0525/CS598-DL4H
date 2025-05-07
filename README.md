# Reproducing and Extending UniXGen

This repository contains the code and scripts needed to reproduce and extend the UniXGen model from the paper "Vision-Language Generative Model for View-Specific Chest X-ray Generation":

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LoganCheng0525/CS598-DL4H.git

2. **Set up environment:**:
   ```bash
   pip install -r requirements.txt

## Data Preparation
1. **Download MIMIC-CXR JPEGs:**:
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
