# agents.md — AI Collaboration Framework for RAG Prototype

## Task Overview

We are building a Retrieval Augmented Generation (RAG) system for B10's Research Enablement team. The system retrieves relevant context from a curated FAQ dataset (ChemLit-QA) and a set of enterprise AI articles, then generates natural language answers grounded in that source material. The goal is to prototype a tool that helps researchers access knowledge across organizational silos — quickly, accurately, and transparently.

## My Role

I am responsible for the decisions that shape the quality and trustworthiness of this prototype:

- **Embedding model selection**: Choosing a sentence-transformer model that produces meaningful semantic representations for scientific text.
- **Similarity thresholds**: Deciding the cutoff at which retrieved results are "close enough" to be useful, and when the system should decline to answer.
- **Prompt design**: Crafting the instructions given to the LLM so that it stays grounded in retrieved context rather than hallucinating.
- **Evaluation judgment**: Reviewing retrieval results and generated answers to assess whether they are relevant, faithful, and appropriately scoped.
- **Architecture decisions**: Determining chunk sizes, overlap strategies, and how to structure the document pipeline.

## AI Assistant's Role

I expect the AI coding assistant (GitHub Copilot) to help with:

- **Boilerplate and pipeline code**: Setting up FAISS indices, embedding pipelines, data loading, and LLM integration.
- **Library usage**: Correct API calls for sentence-transformers, FAISS, HuggingFace datasets, and transformer-based LLMs.
- **Iterative refinement**: Quickly generating code variants when I need to test different approaches (e.g., different chunk sizes, prompt templates).
- **Debugging**: Identifying issues in data processing, dimensionality mismatches, or pipeline errors.

The assistant writes code; I validate that the code does what the assignment requires and that the outputs make sense.

## Validation Strategy

- **Retrieval quality**: For each step, I will test with several in-domain and out-of-domain queries and manually inspect whether the retrieved results are relevant.
- **Embedding sanity checks**: Verify embedding dimensions, confirm that semantically similar questions produce similar vectors.
- **RAG vs. direct LLM**: Compare RAG-grounded answers against what the LLM would say without context to confirm that retrieval adds value.
- **Confidence filtering**: Test with clearly out-of-scope questions to verify the system declines gracefully.
- **Source attribution**: Check that cited sources actually support the generated answer.

## Quality Standards

For this prototype, "good enough" means:

- The system retrieves contextually relevant FAQ entries or document chunks for in-domain questions.
- Generated answers are grounded in the retrieved source material, not hallucinated.
- Source attribution is present so a user can verify the answer.
- The system declines to answer when no strong match exists, rather than fabricating a response.
- The code is readable, runs end-to-end, and each step produces inspectable intermediate outputs.
