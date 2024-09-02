# Orthanc Test Server

This repository provides the setup for an Orthanc server environment for testing purposes. It includes the necessary files and scripts to quickly build and run a local instance of Orthanc, as well as to generate fake DICOM images for testing.

## Features

- **Orthanc Server Setup**: Contains a `Dockerfile` and pre-configured configuration file for building and running an Orthanc server instance.
- **Fake DICOM Generation**: Includes a script to create fake DICOM files for testing purposes.
- **DICOM Query and Retrieve Examples**: Demonstrates how to use the `findscu` and `movescu` tools from the DCMTK suite to interact with the Orthanc server.

## Getting Started

### Prerequisites

- Docker: Ensure Docker is installed and running on your system.
- DCMTK Suite: `findscu` and `movescu` tools should be installed. You can download them from the [DCMTK official site](https://dicom.offis.de/dcmtk.php.en).
    - DCMTK Version: This repository has been tested with `$dcmtk: dcmdump v3.6.8 2023-12-19 $`.
- Pydicom: This repository has been tested with `pydicom` version 2.4.4.

### Building and Running the Orthanc Server

- Run the Orthanc container using Docker Compose:
    ```bash
    docker-compose up -d
    ```

### Generating and Uploading Fake DICOM Files

After the Orthanc server is up and running, generate and store fake DICOM files using the provided scripts:

1. **Generate Fake DICOMs**:
    ```bash
    ./scripts/create_dummy_dicoms.py
    ```

2. **Upload Fake DICOMs to Orthanc**:
    ```bash
    ./scripts/upload_dicoms.sh
    ```

<br>

## Using DCMTK Tools

### Querying with `findscu`

The `findscu` tool is used to perform a C-FIND operation to query the Orthanc server for specific DICOM studies. Below is an example command to query for studies using a `StudyInstanceUID`:

```bash
findscu -v -S -k QueryRetrieveLevel=STUDY -k StudyInstanceUID=8 -k PatientName -aet FAKE_AET -aec ORTHANC localhost 4242
```

- `-v`: Verbose mode to display detailed processing information. You can use `-d` instead for more logs.
- `-S`: Use Study Root information model.
- `-k`: Specifies DICOM query keys (e.g., `QueryRetrieveLevel`, `StudyInstanceUID`, `PatientName`).
- `-aet FAKE_AET`: Sets the calling AE title.
- `-aec ORTHANC`: Sets the called AE title (the AE title of the Orthanc server).
- `localhost 4242`: Address and port where the Orthanc server is running.

### Retrieving with `movescu`

The `movescu` tool is used to perform a C-MOVE operation to retrieve DICOM images from the Orthanc server. Here’s an example command:

```bash
movescu -v -aet FAKE_AET -aec ORTHANC -aem FAKE_AET -k StudyInstanceUID=5 --store --store-port 4243 --output-directory . localhost 4242
```

- `-v`: Verbose mode to display detailed processing information. You can use `-d` instead for more logs.
- `-aet FAKE_AET`: Sets the calling AE title.
- `-aec ORTHANC`: Sets the called AE title (the AE title of the Orthanc server).
- `-aem FAKE_AET`: Sets the move destination AE title (the AE title that Orthanc sends images to).
- `-k StudyInstanceUID=...`: Specifies the DICOM query key for StudyInstanceUID.
- `--store`: Initiates the storage SCP function to receive data.
- `--store-port 4243`: Port on which the SCU will listen to receive data.
- `--output-directory .`: Directory to store the received DICOM files.
- `localhost 4242`: Address and port of the Orthanc server.

## Notes

- Ensure that the AE titles and ports are correctly configured in your Orthanc configuration file at `DicomModalities` to match those used in the `findscu` and `movescu` commands.

<br>
---

This README provides a comprehensive overview and step-by-step instructions for setting up and using an Orthanc server for DICOM testing. If you encounter any issues, refer to the Orthanc and DCMTK documentation for additional guidance.
