# Multi-Model AI Assistant with Live Web Search

An intelligent conversational assistant that dynamically routes queries between Meta's Llama and OpenAI's GPT models. It connects directly to the live internet to verify facts, fetch real-time data, and prevent AI hallucinations. 

This project was built with a product-first mindset: rather than just being a backend script, it offers three distinct, usable features tailored to different user needs.

## 🚀 Core Features

The application is divided into three main capabilities:

1. **Standard Chatbot:** A fast, conversational AI for general queries that do not require real-time data.
2. **Web-Connected Chatbot:** An intelligent assistant that uses tool-calling (via the Tavily API) to search the live web. It decides on its own when to pull live data to ensure accuracy.
3. **AI News Fetcher:** A dedicated tool with a built-in UI to instantly pull the latest AI industry news, filterable by Day, Week, or Month.

## 🛠️ Tech Stack

* **Large Language Models:** Meta Llama & OpenAI GPT
* **Inference & Orchestration:** Groq (for ultra-fast model routing)
* **Web Search Integration:** Tavily API 
* **Tracing & Evaluation:** LangSmith (used to track system performance, debug multi-step workflows, and reduce failure points)

## 💡 The Problem It Solves

Standard AI models often hallucinate or provide outdated information. By integrating Groq for fast switching and Tavily for live web searches, this system only relies on its internal memory when appropriate, and searches the live internet when facts are required. LangSmith is integrated on the backend to track every step the AI takes, ensuring the final output is accurate and useful for the end user.
