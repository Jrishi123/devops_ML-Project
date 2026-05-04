# register_best.py — find and register the best model
import mlflow
from mlflow.tracking import MlflowClient
 
mlflow.set_tracking_uri('file:./mlruns')
client = MlflowClient()
 
def find_best_model():
    # Search all runs in the experiment
    experiment = client.get_experiment_by_name('iris-classification')
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        order_by=['metrics.cv_mean DESC'],
        max_results=1
    )
 
    best_run = runs[0]
    print(f'Best run: {best_run.info.run_name}')
    print(f'  CV Mean:  {best_run.data.metrics["cv_mean"]:.4f}')
    print(f'  Accuracy: {best_run.data.metrics["accuracy"]:.4f}')
    return best_run
 
def register_model(run):
    model_uri = f'runs:/{run.info.run_id}/model'
    # Register in Model Registry
    result = mlflow.register_model(model_uri, 'iris-production-model')
    print(f'Model registered as version: {result.version}')
 
    # Promote to Production stage
    client.transition_model_version_stage(
        name='iris-production-model',
        version=result.version,
        stage='Production'
    )
    print('Model promoted to Production!')
    return result.version
 
if __name__ == '__main__':
    best = find_best_model()
    version = register_model(best)
    print(f'Done! Production model is version {version}')
