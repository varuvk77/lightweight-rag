# 📄 Local-First Document Q&A using PyMuPDF4LLM and Llama.cpp

## Overview

This project implements a **local-first Retrieval-Augmented Generation (RAG)** workflow inspired by the Mozilla.ai Lightweight RAG Blueprint.

The application allows users to ask questions about PDF documents completely offline. The PDF is converted into Markdown using **PyMuPDF4LLM**, divided into chunks, searched using semantic embeddings, and answered using a locally running **Qwen2.5 GGUF model** through **Llama.cpp**.

No cloud APIs or external LLM services are required.

---

## Features

* Local-first document question answering
* PDF to Markdown conversion using PyMuPDF4LLM
* Automatic document chunking
* Semantic search using Sentence Transformers
* Local
