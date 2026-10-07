# AKS Kubernetes role research

Research date: 2026-10-07. Documentation guides realistic phrasing; candidate experience is based on the user's instructions, not inferred from these references.

- AKS upgrades: review disruption budgets, surge capacity, workload readiness and upgrade windows. [Microsoft upgrade options](https://learn.microsoft.com/en-us/azure/aks/upgrade-options).
- GPU node pools: validate GPU readiness and schedule workloads using GPU requests and isolation. [Microsoft GPU guidance](https://learn.microsoft.com/azure/aks/gpu-cluster) and [scheduler practices](https://learn.microsoft.com/azure/aks/operator-best-practices-advanced-scheduler).
- Vector database deployments: use Helm and account for storage and resource configuration; Milvus and Qdrant have separate deployment requirements. [Milvus Helm installation](https://milvus.io/docs/install_cluster-helm.md), [Qdrant installation](https://qdrant.tech/documentation/installation/).
- GKE lifecycle: consider managed control-plane upgrades, node upgrades and notifications when evaluating the platform. [GKE upgrade concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades). GKE remains an evaluation target for this resume.

User explicitly selected AKS-only hands-on claims. Do not claim Prisma/Twistlock, Dynatrace or Azure/GCP vendor relationship experience. No new certifications or invented metrics.
