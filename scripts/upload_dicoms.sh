#!/bin/bash

# Define variables
ORTHANC_URL="http://localhost:8042/instances"  # URL of Orthanc
DICOM_DIR="dicom_files"  # Directory where DICOM files are stored

# Loop through all DICOM files in the specified directory and send them to Orthanc
for dicom_file in $DICOM_DIR/*.dcm; do
    echo "Sending DICOM file: $dicom_file"
    response=$(curl -X POST -w "%{http_code}" -o /dev/null -s $ORTHANC_URL --data-binary @$dicom_file)
    
    if [ "$response" -eq 200 ] || [ "$response" -eq 201 ]; then
        echo "Successfully sent: $dicom_file"
    else
        echo "Failed to send: $dicom_file. Response code: $response"
    fi
done

echo "All DICOM files have been processed."
