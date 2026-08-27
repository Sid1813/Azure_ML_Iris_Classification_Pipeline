from azure.ai.ml import MLClient
from azure.identity import AzureCliCredential

credential = AzureCliCredential()

ml_client = MLClient(
    credential=credential,
    subscription_id="YOUR_SUBSCRIPTION_ID",
    resource_group_name="azure-ml-toy",
    workspace_name="iris-ml-demo",
)

print("Connected to Azure ML!")
print(f"Workspace: {ml_client.workspace_name}")