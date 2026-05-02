# Boot.dev Mapping to AWS GenAI Developer Cert

## Rule

Boot.dev is supplementary hands-on training.
The official AWS exam guide remains the source of truth.

Every Boot.dev section must map to:

- AWS service
- exam domain
- repo output
- possible exam scenario

---

## Learn AWS

Purpose:

- build AWS basics
- reinforce IAM, S3, CLI, monitoring, deployment concepts

Relevant exam areas:

- Domain 1
- Domain 2
- Domain 3
- Domain 4

AWS mapping:

- IAM
- S3
- CloudWatch
- AWS Budgets
- Lambda
- API Gateway
- Bedrock integration later

Repo output:

- notes/iam-basics.md
- notes/s3-security-for-rag.md
- notes/cost-control.md

---

## Learn Retrieval Augmented Generation

Purpose:

- understand retrieval from first principles
- learn chunking, embeddings, vector search, hybrid search, reranking, evaluation

Relevant exam areas:

- Domain 1
- Domain 3
- Domain 4
- Domain 5

AWS mapping:

- Amazon Bedrock
- Bedrock Knowledge Bases
- Amazon Titan Embeddings
- OpenSearch Serverless
- Aurora pgvector
- S3
- CloudWatch
- Guardrails

Repo output:

- examples/rag_local_mock.py
- notes/rag-design.md
- notes/chunking-tradeoffs.md
- notes/retrieval-debugging.md
- notes/evaluation.md

---

## Build an AI Agent in Python

Status:

- optional after AWS basics and RAG basics

Purpose:

- understand function calling, tool use, feedback loops, agent boundaries

Relevant exam areas:

- Domain 2
- Domain 3
- Domain 5

AWS mapping:

- Bedrock Agents
- tool permissions
- human-in-the-loop
- guardrails
- CloudWatch logs
- cost controls for loops

Risk:

- can become a distraction if started too early
