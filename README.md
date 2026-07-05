# AI Powered Self-Healing Infrastructure on AWS

## Overview

This project demonstrates an AI-powered self-healing infrastructure built on AWS.

The platform continuously monitors infrastructure metrics, detects anomalies using Machine Learning, determines the most appropriate remediation action, optionally requests human approval for high-risk actions, executes automated runbooks, and stores every incident for continuous improvement.

---

## Architecture

```
                 +----------------------+
                 | CloudWatch           |
                 | Prometheus           |
                 +----------+-----------+
                            |
                            v
                     Amazon EventBridge
                            |
                            v
                    AWS Lambda (Ingress)
                            |
                            v
                AWS Step Functions Workflow
                            |
           +----------------+----------------+
           |                                 |
           v                                 v
   SageMaker Endpoint              Amazon Bedrock
   (Anomaly Detection)             (Root Cause Analysis)
           |                                 |
           +----------------+----------------+
                            |
                            v
                  Decision Engine Lambda
                            |
                    Risk Classification
                            |
          +-----------------+----------------+
          |                                  |
      Low Risk                          High Risk
          |                                  |
          v                                  v
 AWS Systems Manager                  Slack Approval
 Automation Runbooks                        |
          |                                  |
          +---------------+------------------+
                          |
                          v
                  Infrastructure Healing
                          |
                          v
                 DynamoDB + S3 Archive
```

---

## AWS Services

- AWS Lambda
- Amazon SageMaker
- Amazon Bedrock
- AWS Step Functions
- Amazon CloudWatch
- Amazon EventBridge
- AWS Systems Manager
- Amazon DynamoDB
- Amazon S3
- Amazon SNS
- AWS Secrets Manager
- Amazon ECR
- AWS KMS

---

## Repository Structure

```
terraform/
lambda/
ml/
monitoring/
bedrock/
stepfunctions/
ssm/
docker/
scripts/
simulator/
tests/
.github/
docs/
```

---

## Deploy

```bash
git clone https://github.com/example/ai-self-healing.git

cd ai-self-healing

bash scripts/deploy.sh
```

---

## Train Model

```bash
cd ml

python train.py
```

---

## Generate Test Metrics

```bash
python simulator/generate_metrics.py
```

---

## Send Test Event

```bash
python simulator/send_events.py
```

---

## Execute Tests

```bash
pytest
```

---

## Dashboard

```
Grafana

http://localhost:3000
```

---

## Prometheus

```
http://localhost:9090
```

---

## Future Improvements

- Predictive Failure Detection
- Multi-region Recovery
- Cost Optimization
- Kubernetes Operators
- OpenTelemetry
- LLM Incident Summaries

---
