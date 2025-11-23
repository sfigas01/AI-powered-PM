# AI Agent Platform Landscape (code / low-code / no-code)

## Code-first frameworks
- LangChain (Python/TS): tool-calling, agents, retrievers; hosted LangSmith/LangGraph
- LlamaIndex: data connectors, retrieval, agents; works with OpenAI/Anthropic/local models
- Haystack: pipelines, retrieval, toolcalling; production focus
- Semantic Kernel: .NET/TS orchestration, planner, connectors
- AutoGen / CrewAI: multi-agent coordination, tool plugins
- DSPy / Guidance / Marvin: structured prompting + tool use
- HF Transformers/Inference, vLLM, Ollama: model hosting + tool APIs
- OpenAI Assistants/Tools, Anthropic Tools, Cohere Tools: hosted tool-calling APIs

## Low-code builders/orchestrators
- Flowise (UI for LangChain), Dust.tt, Vellum, Humanloop, Relevance AI, Superagent
- Retool AI, Bubble + AI plugins, Pipedream, n8n, Zapier Interfaces/AI Actions, Make (Integromat), Parabola
- Cloud: GCP Vertex AI (agents/workbench/Workflows), Azure AI Studio (Orchestration), AWS Bedrock Agents, IBM watsonx orchestrations
- Observability/ops: LangSmith, AgentOps, PromptLayer, W&B Traces, Galileo, Martian

## No-code / SaaS agents
- OpenAI GPTs, Anthropic Artifacts (emerging), Cognosys-style hosted agents
- Enterprise chat/ops: Intercom Fin, Drift, Forethought, Moveworks, Ada, Kore.ai, Yellow.ai
- Productivity suites: Notion AI, ClickUp AI, Microsoft Copilot “agents”, Google Duet-style copilots

## Patterns to compare
- Tooling: function-calling, HTTP integrations (search/DB/CRM), RPA via Playwright/Selenium
- Memory/data: vector DBs (Pinecone/Qdrant/Weaviate/Milvus), graph stores (Neo4j), SQL connectors
- Control: single-agent vs. multi-agent graphs, planners/executors, guardrails (LlamaGuard/Guardrails/Rebuff), evals (Ragas/DeepEval)
- Ops: tracing, cost/tokens, rate limits, auth/PII handling, SOC2/ISO

## Quick picks by need
- Fast prototype (code): LangChain + LangGraph + OpenAI tools; or AutoGen/CrewAI for multi-agent
- Fast prototype (no-code): OpenAI GPTs or Flowise
- Enterprise compliance: Vertex AI / Azure AI Studio / Bedrock Agents; Intercom/Moveworks for IT/chat
- Observability-first: LangSmith or AgentOps alongside any framework

## Next steps
- Pick 2–3 candidates per category and score on: security (SOC2/PII), latency, cost, hosting model, allowed tools/integrations, rate limits, eval/guardrails, and admin/SSO.
