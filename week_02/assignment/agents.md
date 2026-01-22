# Agent Scope: Multimodal Search for HIM Holdings

## 1. What we're building

A prototype multimodal search system that enables customers to select a product image and refine results with text modifiers (e.g., "longer sleeves," "darker color"), reducing search friction and improving purchase conversion.

## 2. How AI helps solve the business problem

- **Pain point**: Customers make multiple text searches, each requiring manual keyword iteration → friction and abandonment
- **AI solution — visual anchor**: Start with a product image (or upload one) to bypass keyword formulation; CLIP encoder finds visually similar products immediately
- **AI solution — text refinement**: Layer text modifiers ("longer sleeves," "darker") as embeddings that blend with the image embedding, refining results without additional searches
- **Expected impact**: Fewer searches per user interaction → higher likelihood of purchase; customers reach desired product in 1-2 iterations instead of 5+

## 3. Key file locations and data structure

**Artifact paths:**
- **Notebook**: `mbai448_week02_assignment.ipynb` (working notebook for Steps 1–5)
- **Scoping document**: `agents.md` (this file; guidance for Copilot)
- **Project documentation**: `README.md` (to be created end of Act II)
- **Multimodal search plan**: `multimodal_search_plan.md` (reference design)

**Data structure (H&M Fashion Captions dataset):**
- **Source**: HuggingFace Datasets (`tomytjandra/h-and-m-fashion-caption`)
- **Item schema**: Each item contains `product_id` (string), `image` (PIL Image), `caption` (text description)
- **Working subset**: ~5,000 items (downloaded to reduce compute; full dataset is 69K+ items)
- **Format**: HuggingFace Dataset object with built-in batching and streaming support

## 4. High-level execution plan

**Act II Prototyping (Steps 1–5):**

1. **Load and explore** (Step 1): Download subset of H&M dataset; inspect raw items (image, caption, product_id); confirm data shape and availability
2. **Generate embeddings** (Step 2): Load pretrained CLIP model; encode all images into fixed-length vectors; encode all captions into fixed-length vectors; store both for retrieval
3. **Baseline image search** (Step 3): Define cosine similarity metric; select a query image; retrieve top-K nearest neighbors using image embedding alone; display results
4. **Contrastive text queries** (Step 4): Create two related text queries differing in one attribute (e.g., "red shirt" vs. "blue shirt"); encode both; compare result sets to observe how text embeddings shift similarity rankings
5. **Stress test edge cases** (Step 5): Choose 3+ test inputs intentionally designed to fail or produce ambiguous results (e.g., contradictory modifiers, non-existent color/size, abstract descriptions); document similarity scores and failure modes
6. **Document prototype** (End of Act II): Create README.md capturing what works, what breaks, and open questions; prepare for stakeholder conversations

**Key activities throughout:**
- Use GitHub Copilot to plan, validate, execute, and check each step (disciplined loop per assignment)
- Keep all embeddings and indices immutable once created (reuse for all downstream steps)
- Surface similarity scores explicitly so failures are quantifiable
- Document findings incrementally (not retrospectively)

## 5. Code conventions and constraints

- **Simplicity first**: Use straightforward NumPy/SciPy operations for similarity calculations (e.g., cosine distance) and standard Hugging Face APIs for model loading; avoid optimization or abstraction unless necessary
- **No fine-tuning**: Leverage pretrained CLIP encoder as-is; focus on understanding how multimodal representations combine and behave, not on model training
- **Readable over clever**: Prioritize clear variable names, explicit steps, and inline comments over optimized or concise code; each step should be easy to follow and modify
- **Exploratory mindset**: This prototype is *not* production-ready; goal is to document how encoder-based search behaves, what it does well, and where it fails

## Success Criteria for Prototype Completion

A working prototype means:
- **Step 1–3**: Baseline multimodal search (image + optional caption queries) returns results with visible similarity scores
- **Step 4**: Contrastive queries demonstrate that text embeddings meaningfully shift result rankings
- **Step 5**: At least one failure case is identified and explained (e.g., contradictory modifiers, system returns confident-but-wrong results)
- **Documentation**: README captures findings, limitations, and questions for stakeholder discussion
