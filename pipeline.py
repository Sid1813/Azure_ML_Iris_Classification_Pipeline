from azure.ai.ml import MLClient, command, dsl, Output
from azure.ai.ml.entities import Environment
from azure.identity import AzureCliCredential


credential = AzureCliCredential()

ml_client = MLClient(
    credential=credential,
    subscription_id="YOUR_SUBSCRIPTION_ID",
    resource_group_name="azure-ml-toy",
    workspace_name="iris-ml-demo",
)


environment = Environment(
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
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
)


train_component = command(
    code=".",
    command="python train.py",
    environment=environment,
    compute="iris-cluster",
    outputs={
        "model_output": Output(
            type="uri_folder"
        )
    },
    display_name="train-iris-model",
)


@dsl.pipeline(
    description="Iris classification pipeline"
)
def iris_pipeline():

    training_job = train_component()

    return {
        "model": training_job.outputs.model_output
    }


pipeline_job = iris_pipeline()

returned_job = ml_client.jobs.create_or_update(
    pipeline_job,
    experiment_name="iris-pipeline-demo",
)

print("Pipeline submitted!")
print(f"Pipeline job: {returned_job.name}")
print(f"Studio URL: {returned_job.studio_url}")