import yaml

with open('flowzone_workflow.yml', 'r') as f:
    data = yaml.safe_load(f)

jobs = data.get('jobs', {})
for job_name, job_data in jobs.items():
    needs = job_data.get('needs', [])
    if isinstance(needs, str):
        needs = [needs]
    
    # Recursively check if event_types is in the dependency chain
    def depends_on_event_types(name):
        if name == 'event_types':
            return True
        job = jobs.get(name)
        if not job:
            return False
        job_needs = job.get('needs', [])
        if isinstance(job_needs, str):
            job_needs = [job_needs]
        for n in job_needs:
            if depends_on_event_types(n):
                return True
        return False

    if not depends_on_event_types(job_name):
        print(f"Job '{job_name}' does not depend on event_types")
