# agents.md

## 1. Task Overview
The goal is to generate compelling sales collateral for rental properties using only the property images in the `./images/` directory. This will be accomplished by leveraging Vision Language Models (VLMs) to analyze images and produce persuasive, accurate, and professional marketing content for a junior salesforce.

## 2. Your Role (Human Developer)
- **Define objectives:** Clarify what makes sales content effective and appropriate for the business context.
- **Prompt engineering:** Design and refine prompts to elicit high-quality, relevant outputs from the VLM.
- **Validation:** Review and validate generated content for factual accuracy, professionalism, and alignment with visible property features.
- **Iteration:** Adjust prompts, workflow, or model parameters based on output quality.
- **Compliance:** Ensure outputs avoid unsubstantiated claims and adhere to legal/business standards.

## 3. AI Assistant's Role (GitHub Copilot)
- **Code generation:** Provide code for loading VLMs, processing images, and generating text outputs.
- **Helper utilities:** Suggest functions for batch processing, prompt management, and output formatting.
- **Prompt suggestions:** Recommend prompt variations to improve content quality and relevance.
- **Debugging:** Assist in troubleshooting errors or unexpected model behavior.

## 4. Validation Strategy
- **Sample testing:** Run the workflow on a variety of images to check output diversity and relevance.
- **Manual review:** Compare generated descriptions to actual image content for factual accuracy.
- **Checklist:** Ensure outputs are clear, professional, and grounded in visible features.
- **Edge cases:** Test with images of varying quality and content to assess robustness.

## 5. Quality Standards ("Good Enough" Criteria)
- **Relevance:** Descriptions accurately reflect visible features in the image.
- **Professional tone:** Language is suitable for sales/marketing and free of errors.
- **Grounded claims:** No information is included that cannot be visually confirmed.
- **Actionable:** Content helps a junior salesperson understand and present the property.
- **Consistency:** Similar images yield similarly structured, high-quality outputs.

---