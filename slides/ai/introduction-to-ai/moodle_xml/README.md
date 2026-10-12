# 📋 Moodle XML Question Banks

This directory contains Moodle-compatible question banks for SE 444: Introduction to Artificial Intelligence.

---

## 📁 Contents

Question banks in Moodle XML format for direct import into the LMS.

---

## 📊 Question Types

| Type | Description | Topics |
|------|-------------|--------|
| Multiple Choice | Single correct answer | All lectures |
| Multiple Response | Multiple correct answers | L03, L06, L07 |
| True/False | Binary questions | L01, L02 |
| Short Answer | Exact text matching | L04, L09 |
| Numerical | Calculated answers | L10, L11, L12 |
| Matching | Pair matching | L05, L13 |

---

## 📥 Importing to Moodle

### Step-by-Step Guide

1. **Access Question Bank**
   - Go to your Moodle course
   - Navigate to: `Course Administration → Question Bank → Import`

2. **Select Format**
   - Choose: `Moodle XML format`

3. **Upload File**
   - Drag and drop the `.xml` file
   - Or use file picker

4. **Import**
   - Click `Import`
   - Verify questions imported correctly

5. **Organize**
   - Move questions to appropriate categories
   - Review and edit as needed

---

## 🏷️ Question Categories

Questions are organized by lecture topic:

| Category | Description |
|----------|-------------|
| `L03_Search` | BFS, DFS, A*, UCS questions |
| `L04_LocalSearch` | Hill climbing, SA questions |
| `L05_Adversarial` | Minimax, alpha-beta questions |
| `L06_CSP` | Constraint satisfaction problems |
| `L07_Logic` | Propositional logic, inference |
| `L09_Planning` | STRIPS, planning questions |
| `L10_Uncertainty` | Probability, Bayes questions |
| `L11_BayesianNet` | Bayesian network inference |
| `L12_MDP` | Value/policy iteration |
| `L13_GameTheory` | Nash equilibrium, games |

---

## 🎯 Usage Tips

### Creating Quizzes
1. Import question bank
2. Create new quiz activity
3. Add questions from bank
4. Use random question selection for variety

### Question Settings
- Set point values per question
- Configure feedback options
- Enable multiple attempts if desired

### Best Practices
- Review questions before deploying
- Test quiz with sample student account
- Adjust time limits based on question count

---

## ⚠️ Notes

- Questions are in English
- Mathematical notation uses MathJax
- Images are embedded (base64)
- Compatible with Moodle 3.x and 4.x

---

*Part of SE 444: Introduction to Artificial Intelligence - Alfaisal University*
