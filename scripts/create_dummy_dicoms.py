from pydicom.dataset import Dataset
import os

# Directory where the DICOM files will be saved
output_dir = 'dicom_files'
os.makedirs(output_dir, exist_ok=True)

# Create 10 dummy DICOM files
for i in range(10):
    ds = Dataset()
    ds.PatientName = f'Dummy Patient {i}'
    ds.PatientID = f'PATIENT-{i:03d}'
    ds.StudyInstanceUID = f"{i}"
    ds.SeriesInstanceUID = f'{i}.1'
    ds.SOPInstanceUID = f'{i}.1.1'
    ds.SOPClassUID = "1.2.840.10008.5.1.4.1.1.4"  # MR
    ds.Modality = 'MR'
    ds.ContentDate = '20240830'
    ds.ContentTime = '120000'
    ds.InstanceNumber = i + 1

    # Set necessary attributes to save as DICOM
    ds.is_little_endian = True
    ds.is_implicit_VR = True

    # Save the DICOM file
    filename = os.path.join(output_dir, f'{ds.SOPInstanceUID}.dcm')
    ds.save_as(filename)
    print(f'Created: {filename}')
