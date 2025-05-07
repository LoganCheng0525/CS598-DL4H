# CS598-DL4H

# Download JPEG images (≈500 GB)
wget -r -N -c -np \
  --user logancheng --ask-password \
  https://physionet.org/files/mimic-cxr-jpg/2.1.0/

# Download accompanying DICOM metadata & reports (≈4 TB, excluding .dcm files)
wget -r -N -c -np --reject dcm \
  --user logancheng --ask-password \
  https://physionet.org/files/mimic-cxr/2.1.0/
