from azure.ai.ml import MLClient, command
from azure.ai.ml.entities import Environment
from azure.identity import AzureCliCredential


# Connect to Azure ML
credential = AzureCliCredential()

ml_client = MLClient(
    credential=credential,
    subscription_id="YOUR_SUBSCRIPTION_ID",
    resource_group_name="azure-ml-toy",
    workspace_name="iris-ml-demo",
)


# Define the environment for our job
environment = Environment(
    name="iris-env",
    description="Environment for the Iris classification project",
    conda_file={
        "name": "iris-env",
        "channels": ["conda-forge"],
        "dependencies": [
            "python=3.12",
            "pip",
            {
                "pip": [
                    "scikit-learn",
                    "pandas",
                    "joblib",
                ]
            },
        ],
    },
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
)


# Define the Azure ML job
job = command(
    code=".",
    command="python train.py",
    environment=environment,
    compute="iris-cluster",
    display_name="iris-training-job",
    experiment_name="iris-demo",
)


# Submit the job
returned_job = ml_client.jobs.create_or_update(job)

print("Job submitted!")
print(f"Job name: {returned_job.name}")
print(f"Job status: {returned_job.status}")
print(f"Studio URL: {returned_job.studio_url}")