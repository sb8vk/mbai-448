# Automated Defect Detection Prototype — README

## 1. What this prototype does
This prototype implements an automated defect detection system for manufacturing components using deep learning. It classifies images of parts as either defective or non-defective to support quality control and reduce manual inspection workload.

## 2. How it works (at a high level)
- **Data**: Operates on a labeled image dataset of manufacturing components, organized into training, validation, and test splits, with classes for defective and non-defective parts.
- **Model**: Uses a pretrained ResNet image classifier (transfer learning from ImageNet), which is fine-tuned on the manufacturing dataset for binary classification.
- **Process**:
  - Loads and inspects the dataset, displaying class distributions and sample images.
  - Evaluates the baseline (pretrained) model’s predictions and interpretability on the data.
  - Fine-tunes the model on labeled images, tracks performance, and evaluates results on a held-out test set.
  - Applies interpretability techniques (e.g., occlusion analysis) to visualize model attention before and after fine-tuning.
- **Outputs**: Produces classification results, confusion matrices, and interpretability visualizations to support stakeholder understanding.

## 3. Limitations and open questions
- **Data limitations**: Prototype is trained and evaluated on a small, static dataset; real-world performance may differ with more diverse or larger-scale data.
- **Model generalization**: The model may not generalize well to new defect types, lighting conditions, or unseen production variations without further data and retraining.
- **Error costs**: False negatives (missed defects) are especially costly; current recall for the defective class may require improvement for production use.
- **Interpretability**: While interpretability tools are used, explanations may be noisy or ambiguous for some predictions.
- **Operationalization**: Integration with factory workflows, real-time inference, and human-in-the-loop processes are not addressed in this prototype.
- **Open questions**: What level of accuracy/recall is acceptable for deployment? How will the system be monitored and updated over time? What are the regulatory or compliance requirements for automated quality control?

---

For setup, troubleshooting, and detailed execution steps, see `agents.md` in this directory.
