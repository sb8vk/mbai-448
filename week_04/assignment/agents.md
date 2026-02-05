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

---

## 4. High-level execution plan

### Step 0: Environment setup
**Goal**: Establish working development environment with required dependencies

### Step 1: Data loading and inspection
**Goal**: Establish ground truth and understand data characteristics before any modeling
**Check**: Confirm image counts, verify visual quality, ensure labels match expectations

### Step 2: Pretrained model evaluation
**Goal**: Understand the starting point before any adaptation
**Check**: Confirm output shape is 1000 classes, verify model loads without errors

### Step 3: Baseline behavior observation
**Goal**: See what the unmodified model predicts on manufacturing data
**Check**: Confirm predictions are ImageNet categories, observe confidence distribution, understand baseline ignorance

### Step 4: Model interpretation (pretrained)
**Goal**: Understand what visual features the model attends to before fine-tuning
**Check**: Generate visual overlays, confirm highlighted regions are visible, note whether attention aligns with defect locations

### Step 5: Model fine-tuning
**Goal**: Adapt the model to recognize defective vs. non-defective components
**Check**: Confirm training completes, plot loss curves, verify validation accuracy improves over baseline

### Step 6: Performance evaluation and comparison
**Goal**: Quantify improvement and identify failure modes
**Check**: Produce comparison tables, highlight one clear improvement, identify one remaining weakness

### Step 7: Model interpretation (fine-tuned)
**Goal**: Verify whether fine-tuning shifted attention toward defect-relevant features
**Check**: Display at least one clear before/after example, confirm attention moved toward defect regions

## 5. Code conventions and constraints

### Core principles:
- **Keep it simple**: Use straightforward, readable Python code that prioritizes clarity over optimization. Avoid unnecessary complexity or advanced techniques unless explicitly required.
- **Standard libraries only**: Rely on established deep learning frameworks and common tools. Do not introduce specialized or niche packages without clear justification.
- **Disciplined iteration**: Follow the Plan → Validate → Execute → Check loop at every step. Ensure each code block is accompanied by verification outputs that confirm expected behavior.
- **Exploratory mindset**: This is a prototype, not production code. Prioritize understanding model behavior over achieving perfect performance metrics.