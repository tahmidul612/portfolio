---
title: "AI Buddy Catalyst Labs"
summary: "Internship building AI agents, a RAG library on PyPI, and the Kubernetes deployment around them."
group: work
weight: 20
oldAnchor: "ai-buddy-catalyst-labs"
---

{{< alert "github" >}}
[insta_rag](https://github.com/AI-Buddy-Catalyst-Labs/insta_rag) || [ansible-playbooks](https://github.com/tahmidul612/ansible-playbooks)
{{< /alert >}}

An internship from May to October 2025 building AI agents and the automation around them. The public piece of that is insta_rag, a configuration-driven RAG library: semantic chunking, hybrid vector and BM25 retrieval, HyDE, optional reranking, Qdrant for vectors with MongoDB for content, and a Graph RAG mode on Neo4j. I set up its packaging, tests, pre-commit secret scanning, and the release workflow that publishes it to PyPI.

I also worked on a content pipeline that chains five different LLMs in sequence behind a FastAPI service, and wrote the Ansible playbooks and GitHub Actions workflows that stood up a kubeadm Kubernetes cluster with Tailscale, MetalLB, nginx ingress, and cert-manager.

{{< columns >}}

**Tech Used**

- Python
- n8n
- FastAPI
- Qdrant

<--->

**&nbsp;**

- Ansible
- Kubernetes
- GitHub Actions
- Neo4j

{{< /columns >}}
