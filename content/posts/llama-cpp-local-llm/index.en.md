---
title: "Run Your Own LLM on a Gaming Laptop — Fully Free, Offline AI with llama.cpp"
description: "Can you run Claude- or ChatGPT-style AI on your own laptop with no internet and no bill? A hands-on log of installing llama.cpp on a gaming laptop (RTX 4060 8GB) to run an open-source LLM for free — why go local, the install, picking a quantized model, and the common traps."
slug: "llama-cpp-local-llm"
date: 2026-07-06T20:45:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "llama.cpp", "local LLM", "LLM", "GGUF", "local AI", "open source"]
---

Everyone uses Claude or ChatGPT these days. But what if you could run that kind of AI **on your own laptop — no internet, no bill**? "Don't you need a server room full of GPUs for that?" you might think. The short answer: **one gaming laptop at home, without spending a cent**, does the job. Last time I built a "local image server" with ComfyUI; this time it's a hands-on log of putting a **talking, writing LLM** onto my own GPU with `llama.cpp`.

## Why go local at all?

Honestly, if you only care about raw smarts, cloud AI wins. And yet there are clear reasons to run things locally.

The biggest one is **unlimited tokens**. Cloud APIs charge for every single token in and out. Summarize hundreds of documents, classify tens of thousands of log lines, or run something overnight, and the bill quietly balloons. Local costs nothing but electricity, so you never hesitate with "ugh, that's a lot of tokens." Write prompts as long as you want, and re-run them as many times as it takes.

On top of that:

- **No rate limits.** APIs cap requests per minute, so big jobs mean constant waiting. My GPU is entirely mine — no queue.
- **Your data never leaves the machine.** This is decisive when you handle internal documents, personal data, or unreleased code you'd rather not upload. Nothing is transmitted, so there's nothing to leak.
- **No internet required.** On a plane, or on an air-gapped network, it just works.
- **The model won't vanish on you.** Cloud models get deprecated; the file on your disk stays that exact version forever.

In a nutshell: **cloud wins on smarts; local wins on freedom, cost, and privacy.** The more sensitive your data or the more repetitive your workload, the more local shines.

## What do you run it with? — Three candidates

There are a few ways to run a local LLM. I compared three and picked one.

| Tool | Upside | Downside |
|------|--------|----------|
| **Ollama** | One command and it's up — the easiest | Under the hood it's llama.cpp; one extra layer for fine tuning |
| **LM Studio** | Pretty GUI, a few clicks | A bit heavy for calling from a program to automate |
| **llama.cpp ← chosen** | **The engine itself**, best at squeezing VRAM, OpenAI-compatible API | You need to get comfortable with a few commands |

The truth is, **llama.cpp is the engine** Ollama and LM Studio run inside. You can hand-tune exactly how many layers go onto the GPU — perfect for squeezing an 8GB laptop — and its bundled `llama-server` exposes an **API in the exact same format as OpenAI's**, so any app plugs in cleanly.

## The big picture — the idea is simple

Same principle as with ComfyUI: the heavy compute runs on the local GPU, and outside programs just call it via API.

```
User/app: "Summarize this paragraph"
   ↓
llama-server (local, http://127.0.0.1:8080/v1)  ← OpenAI-compatible API
   ↓
A GGUF model generates tokens on the RTX 4060
   ↓
The answer streams back out
```

Just two terms to know. **llama.cpp** is an LLM inference engine written in C/C++; even with a weak GPU it splits the model across CPU and GPU to run it. **GGUF** is llama.cpp's model format — the original model **quantized** to slash file size and VRAM use.

## Will my laptop handle it? — Check the specs

First, is it even feasible? Same HP Victus 16 laptop as in the ComfyUI post.

| Item | Needed (7–8B model) | My laptop | Verdict |
|---|---|---|---|
| GPU VRAM | 6GB+ (at Q4) | RTX 4060 Laptop 8GB | Pass |
| RAM | 16GB | 16GB | Pass |
| Disk | ~5GB per model | Plenty free | Pass |

With 8GB of VRAM, a **7–8B model quantized to Q4 fits entirely on the GPU** — the fastest zone. From 13–14B up you have to spill some layers to RAM and speed drops sharply; 30B+ is asking too much of this laptop.

## Picking a model — quantization is half the battle

Even for the same model, **quantization** changes size, speed, and quality. This is where I hit my first snag. Going "higher quality is better," I grabbed Q8 — and ran into **the model only half-loading onto the GPU because VRAM ran out.** The realistic answer for 8GB turned out to be **`Q4_K_M`**.

| Quantization | 7B model size | Notes |
|---|---|---|
| Q8_0 | ~7.5GB | Closest to the original, but heavy for 8GB |
| **Q4_K_M** | **~4.5GB** | **Balance of speed and quality — the de facto local standard** |
| Q3_K_M | ~3.5GB | Lighter, but quality drop starts to show |

A 7–8B instruct-class model (e.g. Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct) is a safe bet. GGUF files are usually available per-quantization from distributors like `bartowski` on Hugging Face.

## Installing (on Windows 11)

### 1. Grab the llama.cpp binary

You can build from source, but the fastest path is a **prebuilt CUDA binary**. From the [GitHub releases](https://github.com/ggml-org/llama.cpp/releases), download a file like `llama-bxxxx-bin-win-cuda-x64.zip` and unzip it into `C:\llama`.

### 2. Download a GGUF model

```powershell
# 7B-class Q4_K_M model (~4.5GB) → save into C:\llama\models\
curl.exe -L -o C:\llama\models\model-q4_k_m.gguf ^
  "https://huggingface.co/bartowski/Qwen2.5-7B-Instruct-GGUF/resolve/main/Qwen2.5-7B-Instruct-Q4_K_M.gguf"
```

### 3. Run the server

Remember exactly one thing here: **`-ngl`** — the number of layers to put on the GPU. `-ngl 99` means "offload as many as you can," and a 7–8B Q4 model fits entirely in 8GB.

```powershell
C:\llama\llama-server.exe -m C:\llama\models\model-q4_k_m.gguf -ngl 99 -c 8192 --port 8080
```

- `-ngl 99` : put all layers on the GPU (lower the number if VRAM is tight)
- `-c 8192` : context length of 8k tokens
- `--port 8080` : server port

### 4. Check that it works

Open `http://127.0.0.1:8080` in your browser and a chat UI appears immediately. To confirm it's really using the GPU, look at the startup log for a line like `offloaded 29/29 layers to GPU`. If that number is maxed out, you're good.

### Three common traps (a heads-up)

The install itself is easy — but people trip on exactly these three spots.

- **Trap 1 — grabbing the CPU build.** The release has several files; casually download the `win-cpu` build and your GPU sits idle while answers crawl. **On NVIDIA, always get the `cuda` build.** (AMD: the `vulkan` build.)
- **Trap 2 — forgetting `-ngl`.** Leave this out and the model runs entirely on the CPU — painfully slow. If you're wondering "I have a GPU, why is this so slow?", this is almost certainly it.
- **Trap 3 — over-reaching with a big model or high quantization.** That's the snag I hit above. Exceed VRAM and speed collapses. For 8GB, 7–8B at Q4 is the answer.

## Plugging into apps — the OpenAI-compatible API

What makes `llama-server` genuinely convenient is that it exposes an **API in the exact same format as OpenAI's**. Take code that used OpenAI, **just change the address to the local one**, and it works as-is.

```python
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="local")

resp = client.chat.completions.create(
    model="local",
    messages=[{"role": "user", "content": "Hi, introduce yourself"}],
)
print(resp.choices[0].message.content)
```

With that one line, you've got your own backend running summarization, code completion, and translation **offline and free of charge.**

## How fast is it?

- With a 7–8B Q4_K_M and all layers on the GPU, roughly **40–60 tokens per second** — fast enough to outrun your reading.
- Time to first response is a few seconds, including loading the model into VRAM.
- Push the context long (say 16k) and you can run short on VRAM; then just lower `-ngl` to spill some layers to RAM. A bit slower, but it runs.

## An honest verdict — where it works, and where it doesn't

- **It works:** for free, with no internet, a genuinely useful LLM runs on my laptop. For practical work like summarizing, translating, classifying, and coding assistance, 7–8B is plenty. Above all, being able to **run it freely without token anxiety** is huge.
- **The limits:** even the best local model isn't as smart as a top-tier cloud model (like Claude). For complex reasoning or long code design, cloud is still better.
- **The realistic combo:** so I think the best setup is **local for sensitive data and bulk repetitive work, cloud for the hard problems.** They're not rivals — it's a division of labor.

That you can get this far on a single laptop for free says a lot about how much AI has lowered the barrier. Next, I'm thinking of wiring this local LLM into a tool like Claude Code to build a **fully offline coding assistant.**
