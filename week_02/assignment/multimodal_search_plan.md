# Multimodal Search Plan: Image + Text Modifiers

## Problem Statement
HIM Holdings customers make multiple text searches to find products, which correlates with lower purchase likelihood. The friction of text-only search—especially for visual products like fashion—causes abandonment.

## Solution Overview
Enable customers to start their search with a **visual anchor** (select a product image) and then apply **text modifiers** (e.g., "long sleeve," "darker color," "taller fit") to refine results. This reduces search friction by:
- Allowing users to express "I want something like *this*, but different in this way"
- Reducing the number of searches needed to find the right product
- Leveraging the visual similarity strengths of encoded representations

## Technical Approach

### Core Components

**1. Visual Anchor (Image Search Foundation)**
- User selects a product image from catalog or uploads an image
- System generates embedding for the selected image using CLIP encoder (image modality)
- Retrieve nearest neighbors in embedding space as a baseline result set

**2. Text Modifier Processing**
- User enters a text description of desired modifications (e.g., "red version," "without pattern," "warmer tone")
- System encodes the modifier text using the same CLIP encoder (text modality)
- Modifier embedding is combined with the image embedding to create a refined search query

**3. Refined Similarity Search**
- Blend the image anchor embedding with the modifier embedding (e.g., weighted combination or vector arithmetic)
- Re-rank the baseline results using the refined query embedding
- Return top-N products that balance both image similarity and text-specified constraints

**4. Results & Feedback**
- Display results with similarity scores and which attributes changed relative to the anchor
- Allow users to refine further or return to the image selection step

## Execution Steps

1. **Load H&M dataset** with image and caption embeddings from the encoder
2. **Build the image search baseline** — retrieve similar products from image alone
3. **Implement text modifier encoding** — process user text through CLIP text encoder
4. **Design embedding combination strategy** — define how image + text modifiers blend
5. **Rank refined results** — apply blended embedding to re-rank candidates
6. **Stress test edge cases** — e.g., contradictory modifiers, modifiers not represented in data, non-existent variations
7. **Prototype UI interaction flow** — simulate user interactions in the notebook

## Key Design Decisions

- **Encoder Choice**: CLIP (already used in baseline) enables consistent image and text embeddings
- **Combination Strategy**: Start with simple linear interpolation (weighted average); consider more sophisticated approaches later
- **Scope**: Use H&M dataset subset to keep prototype fast and explorable
- **Validation**: Ensure that modifiers actually shift results meaningfully and don't introduce irrelevant noise

## Expected Outcome
A working prototype demonstrating that customers can reduce search effort by combining visual selection with targeted text modifiers, lowering friction and increasing conversion likelihood.
