# 🧠 Complete AI Engineer Roadmap

> **A Comprehensive Learning Path from Mathematics to Production-Grade Generative AI**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com/yourusername)

---

## 📚 Overview

This roadmap is a **curated collection of 145+ topics** across **11 learning phases**, designed to take you from a beginner to a production-ready AI Engineer. With **~145 courses** and **~344 total topics**, this comprehensive guide covers everything from foundational mathematics to cutting-edge Generative AI technologies.

### 📊 Course Breakdown

| Course | Duration | Focus Areas |
|--------|----------|-------------|
| **Course A (Math)** | 22 hours | Linear Algebra, Calculus, Statistics, Probability |
| **Course B (Full ML+DL)** | 99 hours | Python, ML Algorithms, DL, NLP, MLOps, Docker, AWS |
| **Course C (GenAI)** | 57 hours | LangChain, RAG, Agents, LangGraph, Fine-tuning, MCP |

---

## 🗺️ Learning Phases

### Phase 1: Mathematics Foundations 📐
*20 hours*

#### Linear Algebra
- Scalars, Vectors — definitions and geometric intuition
- Vector Addition and Subtraction
- Vector Multiplication — Element-wise and Scalar
- Dot Product and Cosine Similarity (key for embeddings)
- Introduction to Matrices and Applications
- Matrix Operations — Multiplication, Transpose, Inverse
- Linear Transformations and Visualization
- Vector Length, Unit Vectors, Projection
- Inverse Functions and Matrix Inversion
- Eigenvalues and Eigenvectors (key for PCA)
- Equation of Line, Plane, and Hyperplane

#### Calculus for ML
- Slopes — What They Are and How to Calculate
- Introduction to Derivatives and Limits
- Mathematical Notation of Derivatives
- Finding a Derivative at a Point with Examples
- Power Rule, Constant, Sum, Difference Rules
- Derivatives of Trigonometric, Logarithmic, Exponential
- Product Rule in Derivatives
- Chain Rule of Derivatives (critical for backpropagation)
- Composition of 3 or More Functions
- Application of Chain Rule in Machine Learning

#### Statistics & Probability
- Introduction to Statistics and Types
- Population vs Sample Data, Types of Sampling
- Types of Data and Scales of Measurement
- Measure of Central Tendency - Mean, Median, Mode
- Measure of Dispersion - Variance, Std Dev
- Why Sample Variance is Divided by N-1
- Random Variables, Percentiles, Quartiles, 5-Number Summary
- Histogram and Skewness
- Correlation and Covariance
- Addition Rule and Multiplication Rule in Probability
- PDF, PMF, CDF - Relationships
- Types of Probability Distributions
- Bernoulli, Binomial, Poisson Distributions
- Normal/Gaussian Distribution, Z-Score
- Uniform, Log-Normal, Power Law, Pareto Distributions
- Central Limit Theorem and Estimates
- Hypothesis Testing Mechanism, P-value
- Z-Test, T-Distribution, T-Test, Z vs T Comparison
- Type 1 and Type 2 Errors
- Bayes Theorem, Confidence Interval, Margin of Error
- Chi-Square Test and Goodness of Fit
- ANOVA - Types, Assumptions, Partitioning of Variance

---

### Phase 2: Python Programming 🐍
*15 hours*

#### Python Basics
- Environment Setup — Anaconda, VS Code, Virtual Environments
- Python Basics — Syntax, Semantics, Variables
- Data Types — int, float, str, bool
- Operators — Arithmetic, Comparison, Logical, Bitwise
- Conditional Statements — if, elif, else
- Loops — for, while, break, continue
- Lists — Operations, Slicing, List Comprehension
- Tuples — Immutability and Use Cases
- Sets — Operations, Union, Intersection
- Dictionaries — CRUD, Iteration, Comprehension
- Real-World Use Cases of Lists
- Iterators and Generators with Practical Implementation
- Functions — Closures, Decorators
- Advanced Python Practice Problems

#### Data Libraries
- NumPy — Arrays, Broadcasting, Operations
- Pandas — DataFrame, Series, Data Manipulation
- Reading Data from CSV, Excel, JSON, SQL
- Data Visualization with Matplotlib
- Data Visualization with Seaborn
- SQLite3 — CRUD Operations with Python

#### Advanced Python
- Logging — Basic, Multiple Loggers, Real-World Example
- Multithreading — Practical Implementation
- Multiprocessing — Practical Implementation
- Thread Pool Executor and Process Pool
- Web Scraping with Multithreading
- Memory Allocation, Deallocation, Garbage Collection

#### Web Frameworks
- Flask Framework — App Skeleton, HTML Integration
- HTTP Verbs — GET, POST, PUT, DELETE
- Dynamic URLs, Jinja2 Template Engine
- Building REST APIs with Flask
- Building Web Apps with Streamlit
- ML App Example with Streamlit

---

### Phase 3: Data Preprocessing & EDA 📊
*10 hours*

#### Data Cleaning
- Handling Missing Values — Imputation Strategies
- Handling Imbalanced Datasets
- Handling Imbalanced Dataset Using SMOTE
- Handling Outliers with Python

#### Feature Engineering
- Data Encoding — Nominal and One-Hot Encoding
- Label Encoding and Ordinal Encoding
- Target Guided Ordinal Encoding

#### EDA Projects
- Red Wine Dataset — Full EDA
- Flight Price Dataset — EDA and Feature Engineering
- Google Play Store — Data Cleaning and EDA

---

### Phase 4: Machine Learning 🤖
*30 hours*

#### ML Fundamentals
- Introduction to Machine Learning and Types
- Equation of Line, 3D Plane, Hyperplane
- Distance of a Point from a Plane
- Instance-Based vs Model-Based Learning
- Overfitting and Underfitting — Bias-Variance Tradeoff
- Cross-Validation Types — K-Fold, Stratified
- Feature Selection Techniques
- Hyperparameter Tuning — GridSearchCV, RandomizedSearchCV

#### Regression Algorithms
- Simple Linear Regression — Equations and Intuition
- Cost Function and Convergence Algorithm
- Multiple Linear Regression
- Performance Metrics — MSE, MAE, RMSE, R²
- Linear Regression with OLS
- Polynomial Regression — Intuition and Implementation
- Ridge Regression (L2 Regularization)
- Lasso and ElasticNet (L1 + Combined Regularization)
- End-to-End Regression Projects with AWS Deployment

#### Classification Algorithms
- Logistic Regression — Math Intuition, OVR Strategy
- Performance Metrics — Confusion Matrix, Precision, Recall, F1, ROC-AUC
- Handling Imbalanced Classification
- Support Vector Machine — SoftMargin, HardMargin, Math
- SVM Cost Function, Kernels, SVR
- SVC and SVR Implementations
- Naive Bayes — Bayes Theorem, Variants, Implementation
- K-Nearest Neighbors — Classification and Regression
- KNN Optimization — KD-Tree and Ball Tree

#### Tree-Based Models
- Decision Trees — Entropy, Gini Impurity, Information Gain
- Entropy vs Gini Comparison
- Decision Tree Splits for Numerical Features
- Pre-Pruning and Post-Pruning
- Decision Tree Regression
- AdaBoost — Creating Stumps, Updating Weights, Normalizing
- Gradient Boosting — Classifier and Regressor
- XGBoost — Classification and Regression (In-depth)

#### Unsupervised Learning
- Introduction to Unsupervised ML
- Curse of Dimensionality
- PCA — Geometric Intuition, Math, Eigen Decomposition
- PCA Implementation with Sklearn
- K-Means Clustering — Elbow Method, KMeans++
- K-Means Implementation
- Hierarchical Clustering and Agglomerative Implementation
- DBSCAN — Working, Pros/Cons, Implementation
- Silhouette Score for Cluster Evaluation
- Anomaly Detection — Isolation Forest, LOF, DBSCAN

---

### Phase 5: MLOps & Deployment 🚀
*15 hours*

#### Containerization & Version Control
- Docker — Containers, Images, VMs vs Docker
- Docker Installation and Basic Commands
- Creating and Pushing Docker Images to Docker Hub
- Docker Compose for Multi-Container Apps
- Git — Merge, Push, Checkout, Log, Branch Conflicts

#### End-to-End ML Project Structure
- Project Structure, Logging, Exception Handling
- EDA and Model Training Discussion
- Data Ingestion Implementation
- Data Transformation with Pipelines
- Model Trainer Implementation
- Hyperparameter Tuning Pipeline
- Prediction Pipeline Building
- Model Pickling and Serving
- Deployment to AWS Beanstalk
- Deployment to EC2 with ECR
- Deployment to Azure with Container Images

#### Advanced MLOps
- ETL Pipeline Introduction and Setup
- MongoDB Atlas Setup and ETL with Python
- Data Ingestion Architecture and Implementation
- Data Validation (Parts 1 and 2)
- Data Transformation Architecture
- Model Experiment Tracking with MLflow
- MLflow Remote Tracking with DagsHub
- Model Pusher and Training Pipeline
- Batch Prediction Pipeline
- Artifacts Pusher to AWS S3
- GitHub Actions CI/CD — Docker Image to AWS ECR
- Final Deployment to EC2 Instance
- DVC — Data Version Control
- BentoML for ML Model Serving

---

### Phase 6: Natural Language Processing 📝
*15 hours*

#### NLP Fundamentals
- NLP Roadmap and Practical Use Cases
- Tokenization and Basic Terminologies
- Text Preprocessing — Stemming with NLTK
- Text Preprocessing — Lemmatization
- Text Preprocessing — Stopwords Removal
- Parts of Speech Tagging with NLTK
- Named Entity Recognition (NER)

#### Text Representation
- One-Hot Encoding — Intuition, Advantages, Disadvantages
- Bag of Words — Intuition, Advantages, Disadvantages, Implementation
- N-Grams and N-Gram BOW Implementation
- TF-IDF — Intuition, Advantages, Disadvantages, Implementation
- Word Embeddings — Introduction
- Word2Vec — Intuition, CBOW, SkipGram (In-depth)
- Average Word2Vec
- Word2Vec Practical Implementation with Gensim

#### NLP Projects
- Spam/Ham Classification with BOW
- Spam/Ham Classification with TF-IDF
- Text Classification with Word2Vec and AvgWord2Vec
- Kindle Review Sentiment Analysis (End-to-End)
- Best Practices for Solving ML Problems

---

### Phase 7: Deep Learning 🧠
*25 hours*

#### Neural Network Fundamentals
- Why Deep Learning is Getting Popular
- Perceptron — Intuition, Advantages, Disadvantages
- ANN — Architecture and Learning
- Backpropagation and Weight Updation
- Chain Rule of Derivatives in Backpropagation
- Vanishing Gradient Problem with Sigmoid

#### Activation Functions
- Sigmoid Activation Function (and limitations)
- Tanh Activation Function
- ReLU Activation Function
- Leaky ReLU and Parametric ReLU
- ELU Activation Function
- Softmax for Multi-Class Classification
- Which Activation Function to Use When

#### Loss Functions & Optimizers
- Loss Function vs Cost Function
- Regression Cost Functions
- Classification Loss Functions
- Which Loss Function to Use When
- Gradient Descent and Variants
- SGD, Mini-Batch SGD, SGD with Momentum
- Adagrad, RMSProp, Adam Optimizer
- Exploding Gradient Problem

#### Deep Learning Techniques
- Weight Initialization Techniques
- Dropout Layers
- CNN Introduction and Architecture
- Human Brain vs CNN
- Images — RGB, Channels
- Convolution Operation, Padding
- Max, Min, Average Pooling
- Flattening and Fully Connected Layers
- CNN with RGB Example

#### DL Projects
- ANN Classification Project with Streamlit
- Feature Transformation with Sklearn + ANN
- Step-by-Step ANN Training with Optimizer and Loss
- ANN Regression Practical Implementation
- Finding Optimal Hidden Layers and Neurons
- Deploying Streamlit Web App with ANN Model

---

### Phase 8: Advanced Deep Learning & NLP 🔬
*20 hours*

#### RNN & LSTM
- Introduction to NLP in Deep Learning
- RNN Architecture — RNN vs ANN
- Forward Propagation with Time in RNN
- Backward Propagation with Time in RNN
- Problems with Vanilla RNN (Vanishing Gradient)
- Word Embedding Layers with Keras/TensorFlow
- IMDB Dataset — Feature Engineering
- Training Simple RNN with Embedding Layer
- Prediction from Trained Simple RNN
- End-to-End Streamlit App with RNN
- Why LSTM? Long-Term Dependencies
- LSTM Architecture — Complete
- Forget Gate in LSTM
- Input Gate and Candidate Memory
- Output Gate in LSTM
- Training Process in LSTM
- Variants of LSTM
- GRU — Complete In-depth Intuition
- Bidirectional RNN — Architecture and Intuition
- LSTM Project — Data Collection, Training, Prediction
- GRU Variant Practical Implementation
- Streamlit Web App with LSTM

#### Transformers
- Encoder-Decoder / Sequence-to-Sequence Architecture
- Problems with Encoder-Decoder
- Attention Mechanism — In-depth Architecture
- What and Why Transformers
- Basic Transformer Architecture
- Self-Attention Layer — Complete Working (1hr deep dive)
- Multi-Head Attention
- Feed Forward Network with Multi-Head Attention
- Positional Encoding — In-depth Intuition
- Layer Normalization + Examples
- Complete Encoder Transformer Architecture
- Decoder — Masked Multi-Head Attention (complete)
- Encoder-Decoder Multi-Head Attention
- Final Decoder Linear and Softmax Layer

---

### Phase 9: Generative AI Foundations 🌟
*20 hours*

#### GenAI Basics
- AI vs ML vs DL vs Generative AI - Clear Distinction
- How ChatGPT and LLaMA are Trained (RLHF)
- Evolution of LLM Models
- All LLM Models Analysis
- Complete LangChain Ecosystem Overview

#### LangChain Core
- Getting Started with LangChain and OpenAI
- Basic Components and Modules in LangChain
- Data Ingestion with Document Loaders
- Text Splitting — Recursive, Character, HTML Header, JSON
- OpenAI Embeddings
- Ollama Embeddings
- HuggingFace Embeddings
- Vector Stores — FAISS
- Vector Store and Retriever — ChromaDB
- Understanding Retrievers and Chains
- Building Important LangChain Components
- Building GenAI Apps

#### LLM Integrations
- Introduction to Ollama — Setup and Local Models
- Simple GenAI App Using Ollama
- Tracking GenAI Apps with LangSmith
- Getting Started with Open Source Models via Groq API
- Building LLM, Prompt, StrOutput Chains with LCEL
- Deploy LangServe Runnable and Chain as API

#### Chatbots with Memory
- Building Chatbot with Message History
- Prompt Template and Message Chat History
- Managing Chat Conversation History
- Working with Vector Store and Retriever
- Building Conversational Q&A Chatbot with History
- Q&A Chatbot with Ollama and Open Source Models
- Groq Cloud and LPU Inference Engine
- RAG Document Q&A with Groq and LLaMA3

---

### Phase 10: Agents, Tools & Advanced RAG 🛠️
*15 hours*

#### LangChain Agents
- LangChain Version Updates Overview
- Creating Agents with LangChain
- LLM Model Integration with LangChain
- Invoking, Batch, and Streaming with LangChain
- Implementing Tools in LangChain
- Message Types in LangChain
- Introduction to Tools and Agents
- Creating Custom Tools
- Executing Tools and LLM with Agent Executors
- End-to-End Search Engine App with Tools, Agent, and Open Source LLM

#### Structured Output
- LLM Structured Output Using Pydantic
- LLM Structured Output Using TypedDict
- LLM Structured Output Using DataClass

#### Middleware & Summarization
- Summarization Middleware Using LangChain
- Human-in-the-Loop Middleware
- Stuff Chain and Map Reduce — Intuition
- Stuff and Map Reduce Summarization Implementation
- Refine Chain Summarization — Intuition and Implementation
- YouTube Video and Website URL Summarization App

#### SQL & Math Tools
- Preparing Data for SQLite3 Database
- Preparing Data for MySQL Database
- Streamlit App with LangChain SQL Toolkit and AgentType
- Text-to-Math Problem Solver Using Google Gemma2

---

### Phase 11: Production GenAI & Advanced AI Engineering 🏗️
*15 hours*

#### HuggingFace Integration
- Introduction to HuggingFace and LangChain Integration
- LangChain and HuggingFace Practical Implementation
- End-to-End GenAI Project with LangChain and HuggingFace
- PDF Query RAG with LangChain and AstraDB
- Multi-Language Code Assistant Implementation

#### Deployment
- Deployment of GenAI App on Streamlit Cloud
- Deployment of GenAI App on HuggingFace Spaces
- Life Cycle of GenAI Project in AWS Cloud
- Introduction to AWS Bedrock with Implementation
- Document Q&A RAG with LangChain and Bedrock
- Blog Generation with AWS Lambda and Bedrock
- HuggingFace Open Source LLMs on AWS SageMaker
- RAG Document Q&A with Nvidia NIM and LangChain

#### Multi-Agent & Search
- YouTube Videos to Blog Page Using CrewAI Agents
- Introduction to Hybrid Search
- Reciprocal Rank Fusion in Hybrid Search
- End-to-End Hybrid Search RAG with Pinecone and LangChain

#### Graph Databases
- Introduction to Graph DB with LangChain
- What is a Knowledge Graph
- Creating Neo4j AuraDB Database Instance
- RDBMS vs Graph Database
- Neo4j Property Graph Data Model
- Getting Started with Cypher Query Language
- Intermediate to Advanced Cypher Queries
- Inserting Data in Graph DB with Python and LangChain
- Creating GraphQuery Chain with LangChain
- Prompting Strategies for GraphDB with LLM

#### Fine-Tuning LLMs
- Quantization — In-depth Intuition (INT4, INT8)
- LoRA and QLoRA — Mathematical Intuition
- Fine-Tuning Custom Data with Google Gemma Model
- End-to-End Fine-Tuning with Lamini AI Cloud

#### LangGraph & MCP
- Introduction to LangGraph
- Creating Chatbots Using LangGraph
- Chatbots with External Tools Workflow in LangGraph
- End-to-End Multi-AI RAG Chatbots with LangGraph and AstraDB
- Introduction to MCP (Model Context Protocol)
- Important Components of MCP
- Communication Between MCP Components
- MCP Demo with Claude Desktop

---

## 🎯 Prerequisites

- Basic programming knowledge (any language But Python Prefered)
- Understanding of basic mathematics (high school level)
- Willingness to learn and practice consistently

## 🛠️ Tools & Technologies Covered

| Category | Technologies |
|----------|--------------|
| **Languages** | Python |
| **Libraries** | NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow, Keras |
| **ML Frameworks** | Scikit-learn, XGBoost |
| **DL Frameworks** | TensorFlow, Keras |
| **NLP Tools** | NLTK, Gensim, SpaCy |
| **GenAI Stack** | LangChain, LangGraph, LangServe, HuggingFace, Ollama, Groq |
| **Vector DBs** | FAISS, ChromaDB, Pinecone, AstraDB |
| **Graph DBs** | Neo4j |
| **MLOps** | Docker, Git, MLflow, DVC, BentoML |
| **Cloud** | AWS (EC2, ECR, Beanstalk, S3, Bedrock, Lambda, SageMaker), Azure |
| **CI/CD** | GitHub Actions |
| **Web Frameworks** | Flask, Streamlit |

## 📅 Suggested Timeline

| Phase | Duration | Focus |
|-------|----------|-------|
| Phase 1 | 3-4 weeks | Mathematics Foundations |
| Phase 2 | 2-3 weeks | Python Programming |
| Phase 3 | 1-2 weeks | Data Preprocessing & EDA |
| Phase 4 | 4-6 weeks | Machine Learning |
| Phase 5 | 2-3 weeks | MLOps & Deployment |
| Phase 6 | 2-3 weeks | Natural Language Processing |
| Phase 7 | 3-4 weeks | Deep Learning |
| Phase 8 | 2-3 weeks | Advanced DL & NLP |
| Phase 9 | 3-4 weeks | Generative AI Foundations |
| Phase 10 | 2-3 weeks | Agents, Tools & Advanced RAG |
| Phase 11 | 2-3 weeks | Production GenAI & Advanced Engineering |

> **Total Estimated Time**: 25-35 weeks (6-9 months) with consistent daily practice

## 💡 Tips for Success

1. **Practice Daily**: Consistency is key. Code every day, even if it's just for 30 minutes.
2. **Build Projects**: Apply what you learn by building real-world projects.
3. **Join Communities**: Engage with AI/ML communities on Discord, Reddit, or LinkedIn.
4. **Stay Updated**: AI evolves rapidly. Follow research papers and industry blogs.
5. **Contribute to Open Source**: It's a great way to learn and build your portfolio.
6. **Document Your Learning**: Maintain a blog or GitHub repository of your projects.

## 📚 Recommended Resources

- **Books**: 
  - "Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow" - Aurélien Géron
  - "Deep Learning" - Ian Goodfellow
  - "Natural Language Processing with Transformers" - Lewis Tunstall

- **Online Platforms**:
  - Coursera - Machine Learning by Andrew Ng
  - Fast.ai - Practical Deep Learning
  - HuggingFace Course
  - LangChain Documentation

## 🤝 Contributing

If you find any errors or want to suggest improvements, please feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Special thanks to all the instructors, content creators, and open-source contributors who made this roadmap possible.

---

> **🚀 Remember**: The journey to becoming an AI Engineer is marathon, not a sprint. Stay curious, keep learning, and enjoy the process!

---
**🌟 If this roadmap helps you, please give it a star! 🌟**