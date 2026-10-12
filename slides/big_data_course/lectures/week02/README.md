# Week 2: Introduction to Big Data & HDFS

## Overview

This week introduces the fundamental concepts of Big Data and the Hadoop Distributed File System (HDFS).

---

## Session 2A: Introduction to Big Data

### Learning Objectives
1. Define Big Data and the 5 V's (Volume, Velocity, Variety, Veracity, Value)
2. Distinguish between structured, semi-structured, and unstructured data
3. Understand why traditional databases cannot handle Big Data
4. Identify real-world Big Data applications

### Pre-Class Video
**"What is Big Data?"** - Simplilearn (~15 min)  
🔗 https://www.youtube.com/watch?v=bAyrObl7TYE

### Materials
- 📊 Slides: `slides/SE446_W02A_intro_to_big_data.pdf`
- 📓 Notebook: `notebooks/SE446_W02A_intro_to_big_data.ipynb`

---

## Session 2B: HDFS Fundamentals

### Learning Objectives
1. Understand HDFS architecture (NameNode, DataNode)
2. Explain the concept of data replication
3. Perform basic HDFS operations (simulated)
4. Compare file formats (CSV, Parquet, JSON)

### Pre-Class Video
**"HDFS Tutorial for Beginners"** - Edureka (~20 min)  
🔗 https://www.youtube.com/watch?v=m2rY9XdPNlc

### Materials
- 📊 Slides: `slides/SE446_W02B_hdfs_fundamentals.pdf`
- 📓 Notebook: `notebooks/SE446_W02B_hdfs_fundamentals.ipynb`

---

## Key Concepts

### The 5 V's of Big Data

| V | Description | Example |
|---|-------------|---------|
| **Volume** | Massive amounts of data | Petabytes of social media posts |
| **Velocity** | Speed of data generation | Real-time sensor streams |
| **Variety** | Different data types | Text, images, videos, logs |
| **Veracity** | Data quality and accuracy | Cleaning noisy data |
| **Value** | Extracting useful insights | Predictive analytics |

### HDFS Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        HDFS CLUSTER                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────┐                                         │
│  │   NameNode    │  ← Metadata: file names, block locations│
│  │   (Master)    │                                         │
│  └───────────────┘                                         │
│          │                                                  │
│          ▼                                                  │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐   │
│  │  DataNode 1   │  │  DataNode 2   │  │  DataNode 3   │   │
│  │  Block A      │  │  Block A      │  │  Block B      │   │
│  │  Block B      │  │  Block C      │  │  Block A      │   │
│  └───────────────┘  └───────────────┘  └───────────────┘   │
│                                                             │
│  Replication Factor = 3 (each block stored 3 times)        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ExamGPT Topics

The in-class quiz will cover:
- Definition of the 5 V's
- HDFS architecture components
- Replication factor concept
- File format comparisons (CSV vs Parquet)

---

## Homework

Before Week 3:
1. Complete both notebooks
2. Commit your work to your team's GitHub repository
3. Prepare for Milestone 1 (Data Loading)
