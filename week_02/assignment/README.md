# Week 02 Assignment: Multimodal Search for Fashion E-commerce

## 1. What This Prototype Does

**In one sentence:** Customers can select a fashion product image and refine their search with text modifiers (e.g., "blue version of this dress") to find similar items in the catalog.

---

## 2. How It Works

### Data & Representation
- **Data**: Product images + captions from H&M Fashion dataset (5,000 products for prototyping)
- **Model**: OpenAI CLIP (openai/clip-vit-base-patch16) - aligns images and text in a shared 512-dimensional semantic space
- **Embeddings**: L2-normalized vectors for both images and captions (ensures cosine similarity = dot product)

### Results Production
- **Image Search**: Query image → CLIP image encoder → 512-dim vector → cosine similarity ranking against all product images
- **Text Search**: Text query (e.g., "leather jacket") → CLIP text encoder → 512-dim vector → cosine similarity ranking against all product captions
- **Output**: Top-5 ranked products with similarity scores (0-1 range)

### Key Technical Choices
- **Similarity Metric**: Cosine similarity (captures semantic direction, normalized for speed)
- **No Fine-tuning**: Uses pretrained CLIP (trained on 400M image-text pairs) directly
- **L2 Normalization**: Makes embeddings unit-length for efficient similarity computation

---

## 3. Limitations and Open Questions

### Most Important Limitations

**1. Color Interpretation Gap**
- CLIP's image encoder focuses on style/silhouette; color information primarily comes from text captions
- *Consequence*: Searching for "red dress" may not return visually red dresses if captions don't mention color explicitly
- *Mitigation*: Fine-tune on H&M color metadata or add color histogram as auxiliary feature

**2. Caption Quality Variance**
- Product descriptions range from minimal ("Shirt") to detailed ("Blue denim button-up oxford shirt")
- *Consequence*: Search quality varies depending on caption richness
- *Mitigation*: Standardize caption generation or use OCR + product attribute extraction

**3. No Learning from User Behavior**
- Embeddings are static; system doesn't adapt to user feedback or trending searches
- *Consequence*: Can't optimize for user satisfaction or business metrics (e.g., add-to-cart rate)
- *Mitigation*: Implement feedback loop for online learning

**4. Computational Cost**
- Embedding generation for 5,000 products takes 10-15 minutes on CPU
- *Consequence*: Full catalog (69K items) requires GPU acceleration or pre-computed cache
- *Mitigation*: Cache embeddings in production; use quantization for storage

### Open Questions for Stakeholder Review

**For Product Management:**
- What does "similar" mean for your business? By visual style, by category, or by purchase likelihood?
- Should recommendations expose reasoning (e.g., "Similar pattern" vs "Similar sleeve length")?
- How will this impact key metrics (discovery rate for new items, conversion, average order value)?

**For Catalog/Marketplace Strategy:**
- Should recommendations prioritize in-stock inventory, or include out-of-stock items for customer interest signaling?
- How do we balance search precision (exact matches) vs. discovery (aspirational recommendations)?
- Will this feature create visibility blind spots for certain product categories?

**For Operations/Risk:**
- What error handling is needed for edge cases (ambiguous queries, contradictory inputs)?
- What SLA do we target for query latency (P95 response time)?
- How will system degradation (model inference failure, missing embeddings) surface to customers?

---

## 4. Notebook Structure

The exploration notebook (`multimodal_search_exploration.ipynb`) contains 9 sections:

1. **Load & Explore Dataset**: Load 5K products from H&M Fashion dataset; sample 3 items
2. **Load CLIP Model**: Initialize pretrained model and processor
3. **Generate Image Embeddings**: Create 512-dim vector for each product image
4. **Generate Caption Embeddings**: Create 512-dim vector for each product description
5. **Define Search Functions**: Implement `search_by_image()` and `search_by_text()` with cosine similarity
6. **Image-Based Search Demo**: Search for products similar to product #42 (top-5 results)
7. **Text-Based Search Demo**: Search for "blue denim shirt", "leather jacket", "white sneakers" (top-5 each)
8. **Contrastive Analysis**: Compare results for "red shirt" vs "blue shirt" to show semantic differentiation
9. **Stress Testing**: Test edge cases (nonsense queries, contradictory modifiers, ambiguous terms) and document model behavior

**Runtime**: ~15-20 minutes total (most time spent on embedding generation in Sections 3-4)

---

## 5. How to Run

```bash
# Install dependencies
pip install torch transformers datasets scikit-learn pandas numpy pillow

# Open notebook
jupyter notebook multimodal_search_exploration.ipynb

# Execute cells sequentially (1-9)
# Expected output: search results, similarity scores, contrastive analysis, edge case observations
```

**GPU Support** (optional): If CUDA is available, model will use GPU (~3x faster embedding generation)

---

## Files in This Directory

- **`multimodal_search_exploration.ipynb`** – Main notebook with 9 exploration sections
- **`agents.md`** – Project scope document and Copilot guidance
- **`README.md`** – This file
- **`mbai448_week02_assignment.ipynb`** – Original assignment template
- **`mbai448_week02_walkthrough.ipynb`** – Reference walkthrough (Week 02 materials)

---

## Next Steps

### Short-term Improvements
1. Fine-tune CLIP on H&M-specific color/attribute annotations
2. Implement embedding caching (Redis) for production deployment
3. Add user feedback collection (thumbs up/down) for learning

### Medium-term Enhancements
1. Integrate with inventory system for real-time stock filtering
2. Add personalization (user history, past purchases)
3. Build A/B test framework to measure business impact

### Long-term Strategy
1. Multimodal fusion (combine image + text embeddings more effectively)
2. Real-time embedding updates for new products
3. Deploy with monitoring, SLA tracking, and incident alerting
