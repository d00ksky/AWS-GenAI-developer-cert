# IAM Basics for GenAI Labs

## Concepts to learn

- IAM user
- IAM role
- IAM policy
- permission boundary
- least privilege
- resource-based policy
- S3 bucket policy
- KMS key policy
- CloudTrail audit logs

## Questions

1. Why should a Lambda use an IAM role instead of hardcoded credentials?
2. What is the difference between identity-based and resource-based policies?
3. How would I restrict Bedrock access to only selected models?
4. How would I restrict S3 retrieval to documents the user is allowed to access?

## Key rule for RAG security

System prompt is not access control.

Bad:

1. Retrieve all documents.
2. Pass restricted chunks to the model.
3. Ask the model not to reveal them.

Better:

1. Identify user.
2. Determine allowed documents.
3. Retrieve only authorized chunks.
4. Generate answer only from allowed context.
