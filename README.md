# SageMaker Pipelines for End-to-End Model Deployment

This project demonstrates the use of Amazon SageMaker Pipelines to run end-to-end workflows for model deployment. The pipeline includes steps for preprocessing, training, and creating and registering a model.

## Features

- **Preprocessing**: Data preparation and cleaning steps.
- **Training**: Model training with specified algorithms and parameters. The trained model artifacts are saved in an S3 bucket for later use.
- **Model Creation and Registration**: Steps to create and register the model in the model registry. Users can manually change the approval status of the model.

## Workflow Overview

When the model's approval status is changed to "approved," an event is triggered via AWS EventBridge. This event invokes a Lambda function that deploys the model using the saved artifacts.

## Architecture

![Pipelines Architecture](ss/pipelines.png)

### Model Registration

- **Version Control**: Track different versions of your models.
- **Approval Workflow**: Manage model approvals before deployment.

![Model Registry Overview](ss/model_registry.png)

A user has the option to analyze the performance of a version of the model and then approve it for deployment.

![Change Status Screenshot](ss/change_status.png)

### Event Handling

Utilizes AWS EventBridge to respond to model package state changes (Pending --> Approved).

![EventBridge Configuration](ss/event_bridge.png)

### Lambda Functions

Leverage AWS Lambda for deployment of the approved model.

![Lambda Function Overview](ss/lambda.png)



