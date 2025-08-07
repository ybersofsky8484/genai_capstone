
# Enhanced Capstone Workflow: Summary & Rubric Alignment

## Overview

This capstone project implements a **Retrieval-Augmented Generation (RAG)** workflow to automate research proposal drafting from NOFO documents and a proprietary research archive. The workflow merges enhancements suggested in iterative design sessions, incorporating advanced RAG optimization, multimodal processing, and agentic architecture.

The notebook preserves **original starter code (commented)** for traceability and adds **annotated enhancements** aligned with both the **project rubric** and the **approved mermaid workflow**.

---

## Enhancements and Rubric Mapping

### 1. Multi-Stage PDF Processing (Mermaid Node C, Rubric Step 2)

- **Enhancement**: Combines PyPDF for text extraction, Camelot/Tabula for tables, and OCR for scanned pages or figures.
- **Rationale**: Research corpus includes complex PDFs with tables, formulas, and images. Multi-stage processing ensures comprehensive data ingestion.
- **Rubric Link**: Improves **Research Paper Relevance Assessment** by providing cleaner, richer context for filtering.

---

### 2. Hybrid Indexing & Filtering (Mermaid Node D, Rubric Step 2)

- **Enhancement**: Implements BM25 + embeddings for hybrid retrieval and metadata filtering.
- **Rationale**: Hybrid search balances keyword precision (BM25) with semantic recall (embeddings).
- **Rubric Link**: Strengthens **topic alignment** and filtering, increasing relevance score accuracy.

---

### 3. Agentic Research Synthesis (Mermaid Node E & Subgraph, Rubric Step 3-4)

- **Enhancement**: Three-agent loop:
  - **Research Analyst**: Summarizes relevant papers and identifies gaps.
  - **Proposal Writer**: Drafts proposal sections using NOFO-aligned prompts.
  - **Compliance Checker**: Ensures alignment with evaluation criteria.
- **Rationale**: Modularizes tasks, supports collaboration, and enables iterative refinement with shared memory.
- **Rubric Link**: Supports **Proposal Ideation and Blueprint Preparation** tasks.

---

### 4. Proposal Blueprint + Draft Generation (Mermaid Node F, Rubric Step 4)

- **Enhancement**: Generates structured blueprint before full draft using role-based prompts and few-shot examples.
- **Rationale**: Improves organization and coherence of draft; aligns with NOFO and sample proposals.
- **Rubric Link**: Directly supports **Proposal Blueprint Preparation**.

---

### 5. Multi-Criteria Evaluation + Guardrails (Mermaid Node G, Rubric Step 5)

- **Enhancement**: Adds JSON-formatted evaluation against NIH criteria (Innovation, Significance, Approach, Investigator Expertise) and introduces guardrail flags (hallucination risk, compliance gaps).
- **Rationale**: Provides structured feedback and identifies high-risk content early.
- **Rubric Link**: Maps to **Proposal Evaluation Against NOFO Criteria**.

---

### 6. Targeted Refinement Loop (Mermaid Node I)

- **Enhancement**: Automatically re-prompts weak sections flagged during evaluation.
- **Rationale**: Focuses revision on specific deficiencies, reducing redundant computation.

---

### 7. Caching & Persistence (Mermaid Node J, Rubric Step 7)

- **Enhancement**: Persists embeddings, filtered documents, and draft proposals with checkpoints for reuse.
- **Rationale**: Saves compute time during iterative refinement and enables reproducibility.
- **Rubric Link**: Supports **Summary and Recommendation** step by retaining artifacts for review.

---

## Summary

These enhancements transform the baseline RAG pipeline into a **scalable, multimodal, agentic system** capable of handling complex NOFO-driven proposal generation. They directly improve alignment with rubric criteria, ensuring higher relevance, clearer proposals, and robust evaluation.

---

## Recommendations

- **Add UI Layer**: Implement a simple Streamlit interface for human review and proposal refinement.
- **Expand Guardrails**: Integrate toxicity/bias detection for sensitive research topics.
- **Fine-Tune Models**: Consider domain-specific fine-tuning on NIH proposals for higher accuracy in future iterations.
