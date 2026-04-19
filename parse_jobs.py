import yaml

with open('flowzone_workflow.yml', 'r') as f:
    data = yaml.safe_load(f)

jobs = data.get('jobs', {})
for job_name, job_data in jobs.items():
    needs = job_data.get('needs', [])
    if isinstance(needs, str):
        needs = [needs]
    print(f"{job_name}: {needs}")
