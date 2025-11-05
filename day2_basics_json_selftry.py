

cloud_services = ["PubSub", "BigQuery", "Dataflow", "Dataproc", "Composer"]
print("\nCloud services to be used")
print(cloud_services)


gcp_project = {
    "project_id": "Python-learning-project",
    "region": "europe-west3",
    "project_name": "Self leraning Python",
    "services_enabled": ["GKE","BigQuery", "Storage", "Cloud Run"],
    "team": {"lead": "Nana", "members": 5},
    "geographics": {"country": "germany", "state": "NRW", "year": 2025}

}
print("\nProject Info")
for key, value in gcp_project.items():
    if isinstance (value, dict):
        print(f"{key}")
        for k,v in value.items():
            print(f"  {k}:{v}")
    else:
        print(f"{key}:{value}")
        