# Data Preparation Pipelines Project

## Goal
Build two data preparation pipelines using different datasets to get practice with data preparation and question building.

You will create a **new GitHub repository** for this work. Treat this as a **standalone project** that requires setting up a workspace and repository from scratch.

### Repository Structure (Best Practice)
Your repo should include **three main files**:
1. **Assignment details** (this file)
2. **Python file** answering Questions 1–3
3. **Python file** answering Question 4

---

## Step One: Dataset Review & Question Formation

Review the following two datasets and brainstorm problems that could be addressed with each dataset. Identify **one question per dataset**.

### Datasets
- **College Completion**
  - Data Dictionary + Dataset  
  - Dataset is located here

- **Job Placement**
  - Data Dictionary (informal)
  - You will need to infer meaning from column names and comments on the site

---

## Step Two: Data Preparation & Problem Framing

For **each dataset**, work through the steps outlined in the examples and include the following elements.

### Problem Definition
- Write a **generic question** that the dataset could address
- Identify an **independent business metric** for your problem  
  - Think about the case study examples discussed in class

### Data Preparation Steps
- Correct variable **type/class** as needed
- Collapse factor levels where appropriate
- One-hot encode categorical (factor) variables
- Normalize continuous variables
- Drop unneeded variables
- Create a **target variable**, if needed
- Calculate the **prevalence** of the target variable
- Create data partitions:
  - Train
  - Tune
  - Test

---

## Step Three: Data Assessment

Reflect on your instincts about the data:
- Can this dataset realistically address your problem?
- What areas or variables concern you?
- What limitations or risks do you see?

---

## Step Four: Pipeline Construction

Create **functions** for your two pipelines that produce the **training and testing datasets**.

### Requirements
- The end result should be a **series of reusable functions**
- These functions should:
  - Implement all data preparation steps
  - Be callable in sequence to produce final datasets
- This effectively creates a **DAG (Directed Acyclic Graph)** for your data prep steps
- You **do not** need a single monolithic pipeline function
- Instead, design **smaller, modular functions** that can be reused for future problems
- Use your judgment to determine how best to break up the functions

---

## Deliverable Summary
- GitHub repository with:
  - Assignment description (`.md`)
  - Python file for Questions 1–3
  - Python file for Question 4
- Two complete, reusable data preparation pipelines
- Clear problem framing and data assessment
