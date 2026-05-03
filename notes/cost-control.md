# Cost Control

## Default rules

- Use one AWS Region per lab.
- Set AWS Budgets before paid labs.
- Avoid provisioned throughput unless explicitly required.
- Avoid OpenSearch Serverless until cost is understood.
- Delete resources after every lab.
- Check billing after cleanup.

## Lab template

### Used services

### Potential cost sources

### Cost limits

### Cleanup steps

### Verification after cleanup

## High-risk services

- Amazon Bedrock model calls
- Embeddings
- Bedrock Knowledge Bases
- OpenSearch Serverless
- CloudWatch Logs
- Provisioned throughput
- Agents/tool loops

## Mandatory lab checklist

Before every lab:

- [ ] One AWS Region selected
- [ ] AWS Budget configured
- [ ] Token/request limit defined
- [ ] Cleanup steps written
- [ ] No provisioned throughput unless explicitly justified
- [ ] No OpenSearch Serverless unless explicitly justified
