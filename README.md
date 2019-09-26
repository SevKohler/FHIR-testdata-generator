# FHIR-testdata-generator
Script for generating randomized testdata for FHIR

The script currently supports only the resources Patient, Observation, (Molecular)Sequence and DiagnoricReport.

How to
------
Enter your Server URL in the rest_client.py, choose a method how the posts should be handled (single or as bundle) and the 
amount of resources that should be posted.
All resources will be linked within and filled with radomized data.
