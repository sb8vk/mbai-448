# Project Context: Automated Defect Detection System

## 1. What we're building

An automated defect detection system that classifies manufacturing components as defective or non-defective using deep learning.

---

## 2. How AI helps solve the business problem

- **Addresses staffing challenges**: Automates quality control tasks that previously required manual inspection, maintaining production levels despite pandemic-related workforce constraints
- **Reduces costs and improves efficiency**: Eliminates bottlenecks in the inspection process by automatically flagging defective or substandard products with minimal human intervention
- **Leverages pretrained knowledge**: Uses transfer learning from ImageNet-trained models to adapt general image recognition capabilities to specialized manufacturing defect detection, reducing training time and data requirements
- **Provides interpretable insights**: Enables visual inspection of what features the model attends to, helping quality control teams understand and trust the automated system's decisions

---

## 3. Key file locations and data structure

### Notebook and Code
- `./mbai448_week04_assignment.ipynb` – Main assignment notebook containing the full pipeline implementation

### Data
- `./images.zip` – Compressed archive containing labeled manufacturing component images
  - Training set: Images for model fine-tuning
  - Validation set: Images for hyperparameter tuning and monitoring training progress
  - Test set: Held-out images for final performance evaluation
- Expected structure: Images organized by class labels (defective/non-defective)

### Reference Materials
- `./ref/imagenet_classes.txt` – ImageNet class labels for pretrained model inspection

### Model Artifacts
- `./models/` – (To be created) Directory for saved model checkpoints
  - `defect_detector.pth` – Fine-tuned model weights
  - `training_history.json` – Loss and accuracy logs from training

### Project Documentation
- `./agents.md` – This file; defines project scope, AI role, and coding conventions for Copilot context
- `./README.md` – (To be created in Act II) Technical handoff document explaining prototype capabilities, how it works, and known limitations

### Stakeholder Agent Definitions (Act III)
- `./.github/agents/ops_mgr.agent.md` – Manufacturing Operations Manager persona for workflow and floor-level impact discussions
- `./.github/agents/quality_compliance.agent.md` – Quality & Compliance Lead persona for accountability, auditability, and risk assessment
- `./.github/agents/production_mgr.agent.md` – Production Economics Manager persona for cost-benefit and efficiency tradeoff analysis

---

## 4. High-level execution plan

### Step 0: Environment setup
**Goal**: Establish working development environment with required dependencies

#### If working in VS Code locally:
- Create Python virtual environment: `python -m venv venv`
- Activate environment:
  - **Windows**: `venv\Scripts\activate`
  - **MacOS/Linux**: `source venv/bin/activate`
- Set as notebook kernel in VS Code (top-right corner of notebook)
- Install required packages:
  - `torch` and `torchvision` (PyTorch deep learning framework)
  - `captum` (model interpretation library)
  - `pillow` (image processing)
  - `matplotlib` (visualization)
  - `numpy` (numerical operations)
  - `scikit-learn` (metrics and evaluation)
  - Optional: `tqdm` (progress bars), `seaborn` (enhanced visualizations)
- Verify GPU availability if applicable: `torch.cuda.is_available()`
- **Check**: Run `import torch; print(torch.__version__)` successfully

#### If working in Google Colab:
- Connect to Google Drive if needed for data storage
- Select GPU runtime (Runtime → Change runtime type → GPU)
- Install Captum: `!pip install captum`
- Upload `images.zip` or mount Drive to access it
- **Check**: Verify GPU with `!nvidia-smi`

#### Data extraction:
- Extract `images.zip` programmatically using Python's `zipfile` module or manually
- Expected structure after extraction:
  ```
  images/
    train/
      defective/
        image001.jpg
        image002.jpg
        ...
      non_defective/
        image001.jpg
        ...
    val/
      defective/
      non_defective/
    test/
      defective/
      non_defective/
  ```
- Verify images are `.jpg` or `.png` format
- Note: ResNet models expect 224×224 pixel input (torchvision transforms will handle resizing)

---

### Step 1: Data loading and inspection
**Goal**: Establish ground truth and understand data characteristics before any modeling
- Extract and load image dataset from `images.zip` archive
- Organize data into training (for learning), validation (for tuning), and test (for unbiased evaluation) splits
- Count images per class to identify potential imbalance issues
- Display a grid of sample images with labels to verify correct data loading
- Document observed variation in lighting, camera angle, background, and component orientation
- **Check**: Confirm image counts, verify visual quality, ensure labels match expectations

### Step 2: Pretrained model evaluation
**Goal**: Understand the starting point before any adaptation
- Load a pretrained ResNet model from PyTorch (e.g., ResNet-18 or ResNet-50) trained on ImageNet's 1000 object categories
- Print model architecture summary showing layer types, dimensions, and parameter counts
- Identify the final fully-connected layer that outputs 1000 class probabilities
- Load and inspect `imagenet_classes.txt` to understand what categories the model was originally trained to recognize (animals, vehicles, household objects)
- **Check**: Confirm output shape is 1000 classes, verify model loads without errors

### Step 3: Baseline behavior observation
**Goal**: See what the unmodified model predicts on manufacturing data
- Select 5-10 diverse manufacturing component images (both defective and non-defective)
- Run inference using the pretrained model without any modifications
- For each image, extract the top-3 predicted ImageNet class names and confidence scores
- Display images alongside their predicted labels (expect irrelevant predictions like "screw," "nail," or animal names)
- Document why predictions are nonsensical (model lacks manufacturing defect concepts)
- **Check**: Confirm predictions are ImageNet categories, observe confidence distribution, understand baseline ignorance

### Step 4: Model interpretation (pretrained)
**Goal**: Understand what visual features the model attends to before fine-tuning
- Use the Captum library (PyTorch interpretability toolkit) to generate attribution maps
- Apply Integrated Gradients or GradCAM to highlight which image regions most influence predictions
- Overlay heatmaps on original images to visualize attention patterns
- Select at least 2 examples: one where the model has reasonable confidence and one surprising/confused prediction
- Analyze whether the model focuses on component edges, textures, or background artifacts
- **Check**: Generate visual overlays, confirm highlighted regions are visible, note whether attention aligns with defect locations

### Step 5: Model fine-tuning
**Goal**: Adapt the model to recognize defective vs. non-defective components
- Replace ResNet's final 1000-class layer with a new 2-class layer (defective/non-defective)
- Freeze early convolutional layers (retain ImageNet features) or allow full fine-tuning depending on dataset size
- Define binary cross-entropy loss function and optimizer (e.g., Adam or SGD)
- Train for multiple epochs using training set, validate on validation set after each epoch
- Track and log training loss, validation loss, and accuracy to detect overfitting
- Implement early stopping if validation performance plateaus
- **Save model checkpoint**: Store fine-tuned weights to `./models/defect_detector.pth` to avoid retraining
- Save training history (loss/accuracy logs) for documentation
- **Check**: Confirm training completes, plot loss curves, verify validation accuracy improves over baseline

### Step 6: Performance evaluation and comparison
**Goal**: Quantify improvement and identify failure modes
- Evaluate both pretrained (baseline) and fine-tuned models on the same held-out test set
- Generate confusion matrices showing true positives, false positives, true negatives, false negatives for both models
- Calculate precision (defect prediction accuracy), recall (defect detection rate), and F1 score
- Compare metrics side-by-side to demonstrate fine-tuning benefit
- Identify systematic errors: Does the model miss subtle defects? Flag too many false alarms?
- Consider business implications: False negatives (missed defects) risk downstream quality failures; false positives (incorrect rejections) waste good components
- **Check**: Produce comparison tables, highlight one clear improvement, identify one remaining weakness

### Step 7: Model interpretation (fine-tuned)
**Goal**: Verify whether fine-tuning shifted attention toward defect-relevant features
- Reapply the same Captum interpretation method to the fine-tuned model
- Use the exact same example images from Step 4 for direct comparison
- Generate before-and-after heatmap pairs showing attention changes
- Analyze whether the fine-tuned model now focuses on scratches, cracks, discoloration, or other defect indicators instead of generic object features
- Document cases where attention shifted meaningfully vs. cases where it remains unclear
- Discuss model drift risk: If production data changes (new lighting, camera upgrades), how would attention shift be detected?
- **Check**: Display at least one clear before/after example, confirm attention moved toward defect regions

---

### Act II → Act III Transition: Create Technical Documentation

**Goal**: Document the prototype for stakeholder handoff

Before proceeding to Act III, create `./README.md` capturing the prototype's current state as if handing off to a colleague. Keep it concise and evidence-based.

#### Required sections in README.md:

**1. What this prototype does**
- One-sentence description of the capability built and the problem it addresses
- Example: "A ResNet-based classifier that identifies defective manufacturing components with 87% accuracy on held-out test images."

**2. How it works (at a high level)**
- What data the system operates over (manufacturing component images, train/val/test splits)
- What representation or model it uses (ResNet-18/50 pretrained on ImageNet, fine-tuned on defect labels)
- How results are produced (outputs binary classification: defective vs. non-defective with confidence scores)

**3. Limitations and open questions**
- Most important observed limitations (e.g., "Struggles with subtle surface defects in low-light conditions")
- Open questions before broader deployment (e.g., "How will the model perform on new component types not in training data?")
- Model drift considerations (lighting changes, camera upgrades, new defect types)
- False positive/negative tradeoffs and business implications

---

### Act III: Stakeholder Socialization

**Goal**: Discuss prototype implications with colleagues across different operational domains

You will have structured conversations with three stakeholders, each representing a distinct perspective on how automated defect detection integrates into TUV Limited's manufacturing operations. These conversations use the custom agent definitions in `./.github/agents/`.

#### Stakeholder 1: Manufacturing Operations Manager
**Agent file**: `./.github/agents/ops_mgr.agent.md`

**Focus areas**:
- Workflow integration: How does the system fit into current quality control processes?
- Trust and override protocols: When do floor operators trust the model vs. override it?
- Impact on throughput: Does automation speed up or create new bottlenecks?
- Error handling: What happens when the system flags defects that operators disagree with?
- Staffing implications: How does this change operator roles and training needs?

**Conversation approach**:
- Reference specific evidence from your prototype (confusion matrix, example predictions)
- Explain model behavior in concrete terms operators can understand
- Acknowledge uncertainty where it exists (e.g., edge cases, failure modes)
- Address concerns about false positives slowing production or false negatives reaching customers

**Completion**: Conversation ends when the Operations Manager understands workflow implications and has enough information to plan integration.

---

#### Stakeholder 2: Quality & Compliance Lead
**Agent file**: `./.github/agents/quality_compliance.agent.md`

**Focus areas**:
- Accountability: Who is responsible when defective parts pass inspection?
- Auditability: Can decisions be traced and explained after the fact?
- Regulatory compliance: Does the system meet industry standards for quality control?
- Safety-critical contexts: What happens if defects cause downstream failures?
- Model reliability: How do we know the system maintains accuracy over time?

**Conversation approach**:
- Discuss model interpretability (Step 4 and 7 attention visualizations)
- Explain limitations honestly (when does the model fail?)
- Address traceability (can we log every prediction with confidence scores?)
- Acknowledge gaps in current prototype (no monitoring for drift, no uncertainty quantification)

**Completion**: Conversation ends when the Compliance Lead understands risks, accountability gaps, and what additional safeguards would be needed.

---

#### Stakeholder 3: Production Economics Manager
**Agent file**: `./.github/agents/production_mgr.agent.md`

**Focus areas**:
- Cost-benefit analysis: Does automation save money vs. manual inspection?
- False positive vs. false negative tradeoffs: Which error type is more expensive?
- Production velocity: Does the system increase throughput or create delays?
- Efficiency gains: Where does automation eliminate friction?
- Hidden costs: Does automation introduce new forms of overhead (IT support, model maintenance, retraining)?

**Conversation approach**:
- Quantify tradeoffs using Step 6 metrics (precision, recall, confusion matrix)
- Discuss business impact: False negatives risk customer complaints/returns; false positives waste good components
- Reference throughput implications from Operations Manager conversation
- Be realistic about ongoing costs (model updates, data labeling, drift monitoring)

**Completion**: Conversation ends when the Economics Manager has enough information to model costs and benefits.

---

### Submission Requirements

**Files to submit**:
1. **`./mbai448_week04_assignment.ipynb`** – Completed notebook with all cells executed and outputs visible
2. **`./agents.md`** – This file (project context for Copilot)
3. **`./README.md`** – Technical handoff document created after Act II
4. **Copilot chat history** – Export as `.txt`, `.json`, or `.md` and save in `./assignment/` directory
   - In VS Code: Open Copilot Chat panel → Click "..." menu → Export session
   - Should demonstrate thoughtful, iterative interaction (not "generate everything for me" prompts)
5. **Optional**: Saved model weights (`./models/defect_detector.pth`) if you want to preserve trained model

**Submission process**:
1. Ensure all files are saved in your GitHub repository
2. Shut down Google Colab session (if applicable) to avoid runtime charges
3. **Upload completed notebook to [Canvas Assignment 4](https://canvas.northwestern.edu/courses/245397/assignments/1668983)**
4. Verify submission includes all required components

**Grading considerations**:
- Submissions that ask Copilot to "just read the notebook and produce all outputs" will receive reduced credit
- Demonstrate disciplined iteration: Plan → Validate → Execute → Check loop
- Show evidence of understanding model behavior, not just running code
- Stakeholder conversations should reference specific prototype evidence

---

## 5. Code conventions and constraints

### Core principles:
- **Keep it simple**: Use straightforward, readable Python code that prioritizes clarity over optimization. Avoid unnecessary complexity or advanced techniques unless explicitly required.
- **Standard libraries only**: Rely on established deep learning frameworks and common tools. Do not introduce specialized or niche packages without clear justification.
- **Disciplined iteration**: Follow the Plan → Validate → Execute → Check loop at every step. Ensure each code block is accompanied by verification outputs that confirm expected behavior.
- **Exploratory mindset**: This is a prototype, not production code. Prioritize understanding model behavior over achieving perfect performance metrics.

### Required dependencies:
- **PyTorch ecosystem**: `torch`, `torchvision` (deep learning framework and vision utilities)
- **Interpretability**: `captum` (attribution methods for model explanation)
- **Data manipulation**: `numpy` (numerical operations), `pillow` (image loading/processing)
- **Visualization**: `matplotlib` (plotting), optional `seaborn` (enhanced visualizations)
- **Evaluation**: `scikit-learn` (confusion matrix, precision/recall/F1 metrics)
- **Utilities**: Optional `tqdm` (progress bars during training)

### Version compatibility notes:
- Ensure PyTorch version matches your CUDA version if using GPU acceleration
- Captum requires PyTorch >= 1.6
- Test imports before starting: `import torch; import torchvision; import captum`

### Troubleshooting common issues:

**Training diverges (loss → NaN)**:
- Reduce learning rate (try 0.001 or 0.0001)
- Check for invalid data (corrupted images, incorrect labels)
- Verify loss function matches task (binary cross-entropy for 2-class classification)

**GPU out of memory**:
- Reduce batch size (try 16 or 8 instead of 32)
- Use smaller model (ResNet-18 instead of ResNet-50)
- Clear cache: `torch.cuda.empty_cache()`

**Class imbalance (many more non-defective than defective)**:
- Use weighted loss function: assign higher weight to minority class
- Consider oversampling defective examples or undersampling non-defective
- Focus on precision/recall/F1 rather than raw accuracy

**Underfitting (both train and val accuracy low)**:
- Train longer (more epochs)
- Unfreeze more layers for fine-tuning
- Increase model capacity (use ResNet-50 instead of ResNet-18)
- Verify data quality and labels

**Overfitting (train accuracy high, val accuracy low)**:
- Stop training earlier (use early stopping)
- Add data augmentation (random flips, rotations, color jitter)
- Increase regularization (dropout, weight decay)
- Collect more training data if possible

**Interpretations unclear or noisy**:
- Try different attribution methods (GradCAM vs. Integrated Gradients)
- Smooth heatmaps with Gaussian blur
- Test on clearer examples first (high-confidence predictions)
- Verify preprocessing matches training (normalization, resizing)
