# GOSH-FHIRworks2020-BloodReportGenerator
FHIR API: Uses a dummy FHIR database to retrieve patient data from their UUID and returns a JSON response with the patient's blood details. FHIRapp: Uses the FHIR_API to generate a word document with the patient's latest blood test report.

First, ensure you have downloaded the correct files for the dotnet-azure server, filled in the appSettings.json file and ran the "dotnet run" command.
-- see https://github.com/goshdrive/FHIRworks_2020 for further help.

Next, activate the virtual environment "venv":
- ".\venv\Scripts\activate" (Windows)
- "source env/bin/activate" (macOS/Linux)

Finally, go into the "FHIR_API" directory and the run the commands:
- "pip install -r requirements.txt"
- "python manage.py runserver"

The API should now be running on your localhost:8000
- Entering the url: "http://localhost:8000/<PATIENT_UUID> will return said patient's blood test results.

If you would like to run my application then run the FHIRapp.py file in the FHIRapp directory.

Below are some test patients:
    Test patientID:
    - e3d4ce63-c4c0-4dd2-ab9b-6cc3e43f0e25
    - b9f1a32d-39c8-473b-ad98-2aff11813ec1
    - ac529235-6fbc-48f0-a3fa-de7f1924d497

Demo video:
- https://youtu.be/s6AJ6hTTDx0
