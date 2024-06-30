from azureml.core import Workspace, Model
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice

def deploy_financial_advisor_model():
    ws = Workspace.from_config()
    model = Model(ws, name="financial_advisor_model", version=1)
    
    inference_config = InferenceConfig(
        entry_script="score.py",
        environment=from_conda_environment("financial_advisor_env.yml")
    )
    
    deployment_config = AciWebservice.deploy_configuration(
        cpu_cores=1,
        memory_gb=1,
        auth_enabled=True
    )
    
    service = Model.deploy(
        ws,
        "financial-advisor-service",
        [model],
        inference_config,
        deployment_config
    )
    
    service.wait_for_deployment(show_output=True)
    print(service.get_logs())

if __name__ == "__main__":
    deploy_financial_advisor_model()