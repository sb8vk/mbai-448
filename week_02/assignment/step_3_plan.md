# Step 3 Plan: Compare Items in Representation Space

## Objective
Develop a systematic approach to query the embedding space and retrieve semantically similar items, with explicit specification of the similarity metric and traceability to original data.

---

## 1. Define the Similarity Metric

**Metric Choice: Cosine Similarity**

- **Formula**: For two L2-normalized vectors `u` and `v`:
  ```
  cosine_similarity(u, v) = u · v  (dot product, since ||u|| = ||v|| = 1.0)
  ```

- **Why this choice**:
  - Both embeddings are already L2-normalized (norm = 1.0), making dot product equivalent to cosine similarity
  - Computationally efficient (single dot product operation)
  - Geometrically meaningful: measures angle between vectors in 512-dimensional space
  - Values range from -1 (opposite) to +1 (identical), interpretable as "agreement"

- **Explicit output**: For each retrieved neighbor, display:
  - Similarity score (float, range [-1, +1])
  - Original product metadata (name, category, color)
  - Link back to dataset index for verification

---

## 2. Query Item Selection Strategy

**Approach: Dual-query setup for interpretability**

- **Primary query**: Select a specific product from the dataset (e.g., product at index 42 or a user-specified index)
  - Extract the product's image embedding
  - Retrieve its nearest neighbors by image similarity
  
- **Rationale for this choice**:
  - Image-based query is intuitive: "Show me items that look like this"
  - Products in fashion domain benefit from visual matching
  - Allows validation against human intuition (does this retrieved item actually look similar?)

---

## 3. Retrieve Nearest Neighbors

**Algorithm: Vector similarity search via cosine similarity matrix**

1. **Compute similarity scores**:
   - Take the query embedding (512-dim vector)
   - Compute cosine similarity against all items in the index
   - Use sklearn.metrics.pairwise.cosine_similarity or NumPy dot product
   - Output: 5000 similarity scores, one per item

2. **Sort and rank**:
   - Sort scores in descending order
   - Retrieve top-k neighbors (e.g., k=5 for top 5 results)
   - Exclude the query item itself from results (optional but cleaner)

3. **Output structure**:
   - Array of indices (positions in embedding matrix)
   - Corresponding similarity scores
   - Mapping back to original dataset via product_ids array

---

## 4. Display the Query Alongside Retrieved Items

**Output Format: Structured comparison table**

```
QUERY ITEM
├── Product Name: [name from dataset]
├── Category: [subCategory]
├── Color: [baseColour]
├── Image: [visual preview if possible]
└── Embedding summary: (512-dim vector, first 10 values shown)

TOP-K NEIGHBORS (k=5)
├── Rank 1: [Name] | Category: [cat] | Color: [color] | Similarity: [0.92]
├── Rank 2: [Name] | Category: [cat] | Color: [color] | Similarity: [0.88]
├── Rank 3: [Name] | Category: [cat] | Color: [color] | Similarity: [0.85]
├── Rank 4: [Name] | Category: [cat] | Color: [color] | Similarity: [0.82]
└── Rank 5: [Name] | Category: [cat] | Color: [color] | Similarity: [0.78]
```

**Traceability**: Each result includes:
- Original dataset index (allows pulling full record)
- Product ID (matches product_ids array)
- Full product metadata (name, category, color)
- Raw similarity score (allows user to assess confidence)

---

## 5. Key Design Constraints (Validation Requirements)

✓ **Similarity metric is explicit**: Cosine similarity formula and rationale stated clearly in code comments

✓ **Results are traceable**: product_ids array + dataset index allow jumping back to original items
   - Code maintains index alignment: `product_id = product_ids[neighbor_index]`
   - All metadata retrievable from original dataset via index

✓ **No assumption of correctness**: 
   - Display raw similarity scores (not filtered or thresholded)
   - Include confidence/uncertainty signals (scores range from 0-1, enabling judgment)
   - Plan explicitly notes that high similarity ≠ user satisfaction
   - Will later test with contrastive examples (Step 4) to understand what "similar" actually means

---

## 6. Implementation Artifacts

**Code structure** (to be implemented):
```python
def search_by_image(query_index, top_k=5):
    """
    Retrieve neighbors for a query image via cosine similarity.
    
    Returns: (indices, scores, metadata_list)
    - indices: array of top-k neighbor indices
    - scores: array of cosine similarity scores
    - metadata_list: list of dicts with product info
    """
    # Compute cosine similarity
    # Sort and retrieve top-k
    # Map back to product_ids
    # Retrieve metadata from original dataset
    # Return with explicit scores
```

**Display structure**:
- Print query item metadata + image thumbnail
- Formatted table of top-k neighbors with similarities
- Note: Similarities are scores only; user must interpret if they're "good enough"

---

## 7. Validation Checklist (Before Implementation)

- [ ] Similarity metric is cosine similarity, formula explicitly stated
- [ ] Plan reuses embeddings and indices from Step 2 (no modification)
- [ ] Query item selection is clear (image-based, specific index)
- [ ] Retrieval method is deterministic and reproducible
- [ ] Results include raw similarity scores (not filtered)
- [ ] Traceability chain is complete: index → product_id → metadata → original dataset
- [ ] Display format is human-readable and allows side-by-side comparison
- [ ] Plan acknowledges that high similarity ≠ correctness

---

## Summary

This plan establishes a straightforward similarity-based search system:

1. **What**: Cosine similarity on L2-normalized embeddings
2. **How**: Dot product of query vector against all indexed vectors, sorted descending
3. **Why cosine**: Efficient, interpretable, aligned with normalized embeddings
4. **Display**: Query + top-5 neighbors with metadata and raw scores
5. **Traceability**: Full chain from similarity score back to original product
6. **Caveats**: Scores are numerical metrics only; don't assume neighbors are "correct" or desired by users

Next step: Validation → Does this plan address the assignment requirements? Any revisions needed?
