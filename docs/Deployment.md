# Deployment

## Prerequisites

- Terraform >= 1.5
- Python 3.11
- AWS CLI
- Docker

## Deploy

```bash
terraform init

terraform apply
```

---

Package Lambda

```bash
bash scripts/package_lambda.sh
```

---

Deploy Lambda

```bash
bash scripts/deploy.sh
```

---

Train ML Model

```bash
python ml/train.py
```
