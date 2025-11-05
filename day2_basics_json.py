# Day 2 – Python Basics and JSON parsing

# Lists
cloud_services = ["Compute Engine", "BigQuery", "GKE", "Cloud Storage"]
print("\nCloud Services:")
for svc in cloud_services:
    print("-", svc)

# Dictionaries
gcp_project = {
    "project_id": "my-gcp-project",
    "region": "europe-west3",
    "services_enabled": ["BigQuery", "Storage", "Cloud Run"],
    "team": {"lead": "Anya", "members": 3}
}

print("\nProject Info:")
# for key, value in gcp_project.items():
#     print(f"{key}: {value}")
for key, value in gcp_project.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for k, v in value.items():
            print(f"  {k}: {v}")
    else:
        print(f"{key}: {value}")


# Inline JSON example
import json

json_data = '{"name": "Pranav", "role": "Cloud Engineer", "skills": ["Python", "GCP", "Terraform"]}'
parsed = json.loads(json_data)

print("\nJSON Parsed Output:")
print(f"Name: {parsed['name']}")
print(f"Role: {parsed['role']}")
print("Skills:")
for s in parsed['skills']:
    print("  -", s)
