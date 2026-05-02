# AWS Certified Generative AI Developer - Professional — AIP-C01 Checklist

Skala:
0 = nie wiem
1 = kojarzę termin
2 = wyjaśniam ogólnie
3 = stosuję w prostym scenariuszu
4 = umiem zaprojektować i obronić decyzję

## Domain 1: Foundation Model Integration, Data Management, and Compliance — 31%

### 1.1 Analyze requirements and design GenAI solutions

- [ ] Umiem dobrać architekturę GenAI do wymagań biznesowych i technicznych.
- [ ] Umiem zaprojektować PoC w Amazon Bedrock.
- [ ] Umiem użyć AWS Well-Architected / Generative AI Lens jako ramy oceny.

Ocena 0–4:

### 1.2 Select and configure foundation models

- [ ] Umiem porównać modele pod use case, koszt, latency, jakość i limity.
- [ ] Umiem zaprojektować model routing / provider switching.
- [ ] Umiem zaplanować fallback i graceful degradation.
- [ ] Rozumiem kiedy używać on-demand, provisioned throughput, fine-tuning/custom model.

Ocena 0–4:

### 1.3 Data validation and processing pipelines

- [ ] Umiem walidować dane przed użyciem przez FM.
- [ ] Umiem przygotować tekst, obraz, audio, tabelki pod model.
- [ ] Znam formaty requestów Bedrock API.
- [ ] Umiem poprawiać jakość inputu przed inferencją.

Ocena 0–4:

### 1.4 Vector store solutions

- [ ] Rozumiem embeddings i vector stores.
- [ ] Umiem zaprojektować metadata schema.
- [ ] Umiem wybrać vector store: OpenSearch, Aurora pgvector, managed KB, etc.
- [ ] Umiem zaplanować aktualizację i synchronizację indeksu.

Ocena 0–4:

### 1.5 Retrieval mechanisms for FM augmentation

- [ ] Rozumiem chunking: fixed, semantic, hierarchical.
- [ ] Umiem dobrać embedding model.
- [ ] Rozumiem semantic search, hybrid search, reranking.
- [ ] Umiem zaprojektować query expansion/decomposition.
- [ ] Umiem zaprojektować source attribution i no-answer behavior.

Ocena 0–4:

### 1.6 Prompt engineering and governance

- [ ] Umiem tworzyć prompt templates.
- [ ] Rozumiem Prompt Management.
- [ ] Rozumiem Guardrails.
- [ ] Umiem testować prompt regression.
- [ ] Umiem projektować prompt chains / Prompt Flows.

Ocena 0–4:

---

## Domain 2: Implementation and Integration — 26%

### 2.1 Agentic AI and tool integrations

- [ ] Rozumiem agents, tools, memory, state.
- [ ] Umiem ograniczyć tool permissions.
- [ ] Umiem dodać timeout, stopping conditions, validation.
- [ ] Rozumiem human-in-the-loop.

Ocena 0–4:

### 2.2 Model deployment strategies

- [ ] Rozumiem on-demand invocation.
- [ ] Rozumiem provisioned throughput i jego kosztowe ryzyko.
- [ ] Umiem dobrać model pod latency/cost/quality.
- [ ] Rozumiem kiedy nie trenować/fine-tunować modelu.

Ocena 0–4:

### 2.3 Enterprise integration architecture

- [ ] Umiem użyć API Gateway, Lambda, EventBridge, SQS, Step Functions.
- [ ] Umiem zaprojektować integrację z legacy systemem.
- [ ] Rozumiem RBAC i identity federation.
- [ ] Rozumiem CI/CD dla GenAI komponentów.

Ocena 0–4:

### 2.4 FM API integrations

- [ ] Umiem użyć Bedrock API z boto3.
- [ ] Umiem obsłużyć streaming.
- [ ] Umiem dodać retries, exponential backoff, rate limiting.
- [ ] Umiem logować błędy i request metadata.

Ocena 0–4:

### 2.5 Application integration patterns and dev tools

- [ ] Rozumiem API-first design.
- [ ] Umiem projektować GenAI gateway.
- [ ] Rozumiem Amazon Q Developer jako narzędzie developerskie.
- [ ] Umiem użyć CloudWatch Logs Insights/X-Ray do troubleshootingu.

Ocena 0–4:

---

## Domain 3: AI Safety, Security, and Governance — 20%

### 3.1 Input/output safety controls

- [ ] Rozumiem prompt injection i jailbreak.
- [ ] Umiem użyć Guardrails.
- [ ] Umiem dodać pre-processing i post-processing filters.
- [ ] Umiem ograniczać hallucinations przez grounding i schema validation.

Ocena 0–4:

### 3.2 Data security and privacy

- [ ] Rozumiem IAM least privilege dla Bedrock/S3.
- [ ] Rozumiem KMS, VPC endpoints, S3 bucket policies.
- [ ] Umiem wykrywać/maskować PII.
- [ ] Rozumiem data retention i logging ryzyka.

Ocena 0–4:

### 3.3 Governance and compliance

- [ ] Umiem zaprojektować audit logging.
- [ ] Umiem śledzić data lineage/source attribution.
- [ ] Umiem zaprojektować policy checks.
- [ ] Rozumiem monitoring misuse/drift/policy violations.

Ocena 0–4:

### 3.4 Responsible AI

- [ ] Rozumiem transparency/explainability.
- [ ] Rozumiem fairness evaluation.
- [ ] Umiem dokumentować model limitations.
- [ ] Umiem projektować human review.

Ocena 0–4:

---

## Domain 4: Operational Efficiency and Optimization — 12%

### 4.1 Cost optimization

- [ ] Umiem liczyć koszt tokenów.
- [ ] Umiem ograniczać context window.
- [ ] Umiem użyć caching/prompt compression.
- [ ] Umiem dobrać model tańszy/wystarczający.

Ocena 0–4:

### 4.2 Performance optimization

- [ ] Rozumiem latency-cost tradeoff.
- [ ] Umiem użyć streaming.
- [ ] Umiem optymalizować retrieval.
- [ ] Umiem testować temperature/top-p/top-k.

Ocena 0–4:

### 4.3 Monitoring systems

- [ ] Umiem monitorować token usage, latency, errors.
- [ ] Umiem użyć CloudWatch.
- [ ] Rozumiem Bedrock model invocation logging.
- [ ] Umiem zaprojektować dashboard cost/latency/quality.

Ocena 0–4:

---

## Domain 5: Testing, Validation, and Troubleshooting — 11%

### 5.1 Evaluation systems

- [ ] Umiem stworzyć golden dataset.
- [ ] Rozumiem relevance, factual accuracy, consistency, fluency.
- [ ] Umiem porównać modele.
- [ ] Rozumiem RAG evaluation.
- [ ] Rozumiem LLM-as-a-judge i jego ograniczenia.

Ocena 0–4:

### 5.2 Troubleshooting

- [ ] Umiem diagnozować context overflow.
- [ ] Umiem diagnozować słaby retrieval.
- [ ] Umiem diagnozować błędy Bedrock API.
- [ ] Umiem diagnozować prompt confusion.
- [ ] Umiem naprawiać chunking/embedding/vector search problemy.

Ocena 0–4:
