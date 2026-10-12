# MAI 554: Deep Learning for Natural Language Processing

## Course Information

| | |
|---|---|
| **University** | Alfaisal University |
| **College** | College of Engineering |
| **Instructor** | Prof. Anis Koubaa |
| **Semester** | Spring 2026 |
| **Credits** | 3 |

## Course Description

This course covers the foundations and modern architectures of deep learning applied to natural language processing. Starting from how text is represented numerically (tokenization, embeddings, vectors), students progress through recurrent architectures (RNNs, LSTMs, GRUs), the Transformer architecture (self-attention, encoder-decoder), and key NLP applications (machine translation, named entity recognition, retrieval-augmented generation).

## Learning Objectives

By the end of this course, students will be able to:

1. Explain the role of tokenization in language models and compare character-level, word-level, and subword-level methods
2. Represent words as dense vectors using embedding techniques (Word2Vec, GloVe, fastText)
3. Understand and implement recurrent neural networks (RNN, LSTM, GRU) for sequence modeling
4. Master the Transformer architecture, including self-attention, multi-head attention, and positional encoding
5. Apply deep learning models to NLP tasks such as machine translation and named entity recognition
6. Understand retrieval-augmented generation (RAG) and its role in modern AI systems

## Weekly Schedule

| Lecture | Topic | Materials |
|---------|-------|-----------|
| 1 | Introduction to Deep Learning for NLP | Slides, Lecture Notes |
| 2 | Tokenization for Language Modeling | Slides, Lecture Notes, Notebook |
| 3 | Embedding and Vector Representation | Slides, Lecture Notes, Notebook |
| 4 | From Word Embedding to Contextual Embedding (RNN, LSTM, GRU) | Slides, Lecture Notes, Demo |
| 5 | Transformers: The Power of Self-Attention | Slides |
| 6 | Transformer Block and Architectures | Slides |
| 8 | Machine Translation | Slides |
| 9 | Named Entity Recognition (NER) | Slides |
| 10 | Introduction to Retrieval-Augmented Generation (RAG) | Slides |

## Repository Structure

```
deep_learning_for_natural_language_processing/
├── README.md
├── lectures/
│   ├── lecture_01/          # Introduction to Deep Learning for NLP
│   │   ├── slides/          #   Lecture slides (PDF)
│   │   └── lecture_notes/   #   Revision notes (PDF + LaTeX)
│   ├── lecture_02/          # Tokenization for Language Modeling
│   │   ├── slides/
│   │   ├── lecture_notes/
│   │   └── notebooks/       #   Hands-on BPE tutorial
│   ├── lecture_03/          # Embedding and Vector Representation
│   │   ├── slides/
│   │   ├── lecture_notes/
│   │   └── notebooks/       #   Word2Vec implementation
│   ├── lecture_04/          # RNN, LSTM, GRU
│   │   ├── slides/
│   │   ├── lecture_notes/
│   │   └── demos/           #   RNN animation
│   ├── lecture_05/          # Transformers: Self-Attention
│   │   └── slides/
│   ├── lecture_06/          # Transformer Block and Architectures
│   │   └── slides/
│   ├── lecture_08/          # Machine Translation
│   │   └── slides/
│   ├── lecture_09/          # Named Entity Recognition
│   │   └── slides/
│   └── lecture_10_introduction_to_rag/ # Retrieval-Augmented Generation
│       └── slides/
├── administration/          # Course syllabus
├── resources/
│   └── textbook/            # Building Transformers textbook
└── assessments/             # Exam structure
```

## Lecture Notes

Comprehensive revision notes are available for Lectures 1--4, designed to help students review key concepts. Each set of notes includes:

- **Intuition-first explanations** before every equation
- **Worked numerical examples** with step-by-step computations
- **Key equation reference cards** for quick revision
- **Self-check questions** with full solutions in the Appendix
- **TikZ diagrams** for visual understanding

| Lecture | Pages | Questions | Topics |
|---------|-------|-----------|--------|
| 1 | 19 | 7 | AI/ML/DL, CNNs, GANs, NLP evolution, Transformers preview |
| 2 | 18 | 7 | Unicode, character/word/subword tokenization, BPE algorithm |
| 3 | 17 | 7 | Vectors, dot product, normalization, cosine similarity, Word2Vec |
| 4 | 13 | 7 | RNN equations, vanishing gradients, LSTM gates, GRU |

## Textbook

**Building Transformers** -- Custom textbook available in `resources/textbook/`.

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Deep Learning | PyTorch |
| NLP Libraries | spaCy, Hugging Face Transformers, tiktoken |
| Visualization | Matplotlib, t-SNE |
| Notebooks | Jupyter |

## Contact

Prof. Anis Koubaa -- akoubaa@alfaisal.edu
GitHub: [github.com/aniskoubaa](https://github.com/aniskoubaa)
