---
title: "Building My Own Redmine MCP Server — A Week's Notes"
description: "I built a local MCP server so Claude Code could drive our private-network Redmine directly — a week of building MCP tools, from one file to a pip package."
slug: "redmine-mcp-server"
date: 2026-06-29T22:00:00+09:00
draft: false
categories: ["AI"]
tags: ["MCP", "Claude Code", "Python", "Redmine", "MCP server"]
---

> 💻 **Install:** `pipx install git+https://github.com/junstellar/redmine-mcp-jun.git`

I wanted Claude Code to read and write our company's Redmine directly. The catch: our Redmine sits on a private network, so external SaaS connectors like Atlassian or GitHub were out. So I built a local MCP server that runs only on my own PC. Here are a week's notes — starting from a single file and growing it into a pip package.

## What MCP is, and how I designed the tools

MCP (Model Context Protocol) is a standard for "connecting an AI to external tools." Like USB — match the standard, and you can plug any tool into an LLM.

There are basically two ways to connect the server to the client. **stdio** runs the server as a local process on the user's PC, exchanging messages only within that machine. **HTTP (remote)** hosts the server separately and connects over the network. The remote way is great when you spin it up once and many people share it, but you have to run the server and handle auth and key management yourself. Since I was installing it for my own use inside the company, I went with **stdio** — the key never leaves my PC, and installation is simple.

The first thing I did — before any code — was write down "what should the LLM be able to do with this?" Once I listed it out, I realized I don't actually do that many things in Redmine: check my issues, search and read issues, create issues, leave comments, read and edit the wiki. I trimmed it down to 10 tools accordingly.

| Tool | Role |
|---|---|
| `list_projects` / `list_issues` / `get_issue` | Browse projects & issues |
| `create_issue` / `add_comment` | Create issues & comment |
| `list_wiki_pages` / `get_wiki` / `update_wiki` | Wiki |
| `get_my_today` | "My issues today" shortcut |
| `list_enumerations` | Priority/status IDs |

One thing I learned: pulling frequent workflows out into a dedicated tool — like `get_my_today` — makes the LLM pick them far more reliably. And three things I picked up while building: write rich tool descriptions (skimpy ones make the LLM call the wrong tool), keep input schemas strict, and just pass the JSON through as-is.

## The hard part wasn't the code — it was distribution

I first threw together a single file (about 420 lines) just to confirm it worked. What actually ate my time was "how do I get this installed on other people's machines?" Per-OS path branching kept piling up, and on top of that, Python 3.12's PEP 668 blocked `pip install` in some environments. In the end I rebuilt it as a proper pip package and switched to pipx — which got installation down to two lines on any OS.

The part I was most careful about was touching Claude's config file (`.claude.json`). It's a shared file that holds other MCP settings too, so I forced a backup before every edit (a merge accident actually happened once, and it was instantly recovered). I also hard-coded an absolute path instead of plain `python`, so it doesn't break when the system Python version changes.

| Snag | Fix |
|---|---|
| PEP 668 blocks `pip install` | Switch to pipx |
| MCP stops loading after a Python upgrade | Use an absolute path for the command |
| Merge mishap wipes other config entries | Force a backup before editing |
| LLM ignores the shortcut tool | Add keywords to its description |

## Wrapping up

Building an MCP server itself is surprisingly easy (around 400 lines of Python). The hard parts are *distribution*, *key management*, and *tuning descriptions so the LLM picks the right tool* — those three. Think them through up front and it takes only a few days.

I've put the code up for anyone who needs it ([github.com/junstellar/redmine-mcp-jun](https://github.com/junstellar/redmine-mcp-jun), MIT) — feel free to grab it. Still, I'd recommend building one yourself at least once. Things like a notification when a new issue is filed, or a bot that auto-analyzes an incoming issue and posts a reply — wiring up what *you* actually need teaches you a lot more.
