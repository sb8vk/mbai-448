# RAG Prototype for Cross-Team Research Knowledge Access

## Solution Summary

This prototype is a Retrieval Augmented Generation (RAG) system built for B10's Research Enablement team. It lets a user ask a natural-language question and get an answer grounded in a specific knowledge base — rather than relying on the general (and sometimes unreliable) knowledge of a language model alone.

The system works in three stages:

1. **Embed**: Every entry in the knowledge base (FAQ answers or document chunks) is converted into a numerical vector using a sentence-transformer model (`all-MiniLM-L6-v2`). These vectors capture semantic meaning, so similar ideas end up near each other in vector space.

2. **Retrieve**: When a user asks a question, it is embedded with the same model, and FAISS (a fast vector search library) finds the most semantically similar entries in the knowledge base. A confidence threshold filters out weak matches so the system doesn't answer questions it has no basis for.

3. **Generate**: The retrieved entries are passed as context to a small language model (`SmolLM2-1.7B-Instruct`), which synthesizes a fluent, natural-language answer. Source attribution is included so the user can trace where the information came from.

Two pipelines were built: one over the structured ChemLit-QA FAQ dataset (1,024 question-answer pairs from pharmaceutical chemistry), and a second over unstructured enterprise AI articles that were chunked into overlapping segments. Both pipelines use the same embedding, retrieval, and generation components.

## Limitations and Assumptions

- **FAQ structure assumption**: The first pipeline assumes each entry has a clean question and a self-contained answer. This works well for curated FAQ data but does not generalize to messy or contradictory sources without additional processing.

- **Chunking is naive**: The document pipeline uses fixed-size character-based chunking with overlap. This can split sentences awkwardly or group unrelated content. Smarter chunking (e.g., sentence-boundary-aware, or recursive text splitting) would improve retrieval quality.

- **Confidence threshold requires tuning**: The threshold (0.35 cosine similarity) was chosen empirically for this dataset. Different domains, embedding models, or data distributions would require recalibration. There is no automated threshold optimization.

- **Small LLM limitations**: SmolLM2-1.7B is compact and fast but can produce less coherent or less accurate answers than larger models, especially for complex multi-step reasoning.

- **No access controls**: The prototype treats all data as equally accessible. In a real deployment with sensitive research data, role-based access controls would be essential.

- **No evaluation infrastructure**: There is no automated metric for answer quality (e.g., RAGAS, human ratings). Evaluation was done by manual inspection during prototyping.

## Suggested Next Steps

1. **Smarter chunking**: Move from fixed-character chunking to sentence- or paragraph-aware splitting (e.g., using LangChain's RecursiveCharacterTextSplitter or similar). Evaluate whether retrieval quality improves.

2. **Evaluation pipeline**: Implement quantitative evaluation using metrics like retrieval precision/recall, answer faithfulness (does the answer match the source?), and relevance scoring. Libraries like RAGAS or custom LLM-as-judge approaches can help here.

3. **Larger or API-based LLM**: For production, swap SmolLM2 for a more capable model (e.g., a hosted API like Claude or GPT-4) to improve answer quality, especially for nuanced scientific questions.

4. **Access controls and audit logging**: Before deploying with real research data, implement authentication, role-based permissions for which data each user can query, and logging of all queries and retrieved sources for compliance.

5. **User interface**: Build a simple web UI (e.g., Streamlit or Gradio) that lets researchers type questions and see answers with source links. This would make the prototype testable by non-technical stakeholders.

6. **Hybrid retrieval**: Combine vector similarity search with keyword-based search (BM25) for better coverage — vector search handles paraphrases well but can miss exact terminology matches.
