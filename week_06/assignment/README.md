## Solution Summary

This prototype generates draft leasing/sales collateral from a property photo using a Vision-Language Model (VLM). You provide an image of a room (e.g., kitchen, bedroom, living room, bathroom), and the model produces structured marketing copy that is intended to sound like real rental listing text while staying grounded in what is visible.

How it works:

Loads a VLM that can “see” images and follow instructions (a multimodal large language model).

Builds a prompt that instructs the model to produce four sections:

Description: neutral, factual summary of visible elements

Features: short bullet list of visible selling points

Possibilities: reasonable, non-committal ways a renter could use the space

Testimonial: a generic renter-style blurb (kept intentionally cautious)

Runs inference on the image and returns the formatted output.

The notebook iterates on prompt design to improve grounding and reduce overconfident claims (hallucinations), then wraps the best prompt into a simple end-to-end workflow.

## Limitations and Assumptions

Grounding risk (hallucinations)

The model can invent plausible details that are not visible (e.g., “granite countertops,” “stainless steel appliances,” “recently renovated,” “hardwood floors,” “great views,” “walk-in closet”). In real estate marketing this is a credibility and compliance risk.

This prototype mitigates risk mainly through prompt wording, which is helpful but not sufficient for production.

Single-image limitation

A single photo cannot support unit-wide claims (e.g., “open concept,” “modern appliances throughout,” “quiet building,” “secure entry,” “in-unit laundry”). If it’s not visible, the system should not claim it.

Multi-room or full-listing collateral will be incomplete or biased if generated from one image.

Image quality dependency
Works best when images are:

well-lit, sharp, and show a clear view of the room

not overly wide-angle distorted

not heavily staged/filtered
Poor lighting, blur, extreme angles, or partial room coverage increases errors and vague outputs.

Speculative sections are inherently riskier

“Possibilities” and “Testimonial” are more likely to drift into implied promises, even when phrased carefully.

These sections should be treated as draft text requiring human review.

Compliance not fully enforced

The prototype does not implement automated compliance controls (e.g., Fair Housing-safe language checks, banned-claim filters, audit logs).

The output is not guaranteed to be compliant without human review.

No formal evaluation framework

The notebook demonstrates qualitative testing, but there is no quantitative scoring (hallucination rate, claim verifiability, inter-rater agreement, etc.).

Outputs may vary across images and runs due to model randomness.

## Suggested Next Steps

Add reliability and safety guardrails

Introduce a claims policy layer:

Allowlist: claims that are typically image-verifiable (e.g., “large windows,” “tile flooring,” “ceiling fan,” “double vanity”).

Blocklist: claims that are frequently hallucinated or high-risk (renovation status, neighborhood safety, appliance material, square footage, building amenities unless shown, views unless clearly visible).

Require evidence for each claim:

Have the model output a structured JSON format where each feature includes “what I saw” justification.

Validate claims before rendering final copy (rule-based checks + optional second-pass verification model).

Make it multi-image and listing-aware

Support multiple images per listing and aggregate across rooms.

Deduplicate features, resolve inconsistencies, and generate a cohesive “whole listing” narrative only from supported evidence.

Add human review tools

Provide an editing UI for leasing teams:

highlight risky claims and allow one-click removal or softening

keep a changelog so edits can feed back into evaluation and prompt tuning

Implement evaluation and monitoring

Build a labeled test set:

for each image: vetted description + approved features + disallowed claims

Track metrics:

hallucination/overclaim rate

banned-claim rate

readability/quality scores

time-to-edit (how long a human spends fixing the draft)

Add monitoring in production:

store prompts, model version, and outputs for auditability

sample outputs regularly for manual review

Harden for deployment and scale

Wrap inference in a service (batch + async jobs), with caching and retries.

Make outputs schema-driven (JSON) so downstream systems can render consistent collateral.

Version control prompts and model artifacts; enable A/B testing for prompt/model upgrades.

Compliance readiness

Add explicit Fair Housing and discriminatory-language filters.

Add “do not claim” policies for sensitive or unverifiable attributes.

Create review workflows and escalation paths for edge cases.

In short: the prototype proves you can generate plausible collateral from images, but production requires systematic grounding, multi-image aggregation, compliance controls, and measurable evaluation.