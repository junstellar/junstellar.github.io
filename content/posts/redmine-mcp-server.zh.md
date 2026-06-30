---
title: "自己动手做一个 Redmine MCP 服务器 —— 一周记录"
description: "为了让 Claude Code 直接操作内网中的公司 Redmine，我自己搭建了本地 MCP 服务器。从单个文件到 pip 包，这是设计 MCP 工具的一周记录。"
slug: "redmine-mcp-server"
date: 2026-06-29T22:00:00+09:00
draft: false
categories: ["AI"]
tags: ["MCP", "Claude Code", "Python", "Redmine", "MCP服务器"]
---

> 💻 **一键安装：** `pipx install git+https://github.com/junstellar/redmine-mcp-jun.git`

我想让 Claude Code 直接读写公司的 Redmine。问题是，我们的 Redmine 在内网里，用不了 Atlassian、GitHub 这类外部 SaaS 连接器。于是我自己做了一个只在自己电脑上运行的本地 MCP 服务器。这是从单文件起步、一路做成 pip 包的一周记录。

## MCP 是什么，工具怎么设计

MCP（Model Context Protocol）是一套「把 AI 和外部工具连起来」的标准。就像 USB——只要对上标准，任何工具都能插到 LLM 上用。

把服务器连到客户端的方式大体有两种。**stdio** 是把服务器作为本地进程在用户电脑上启动，只在这台机器内部收发。**HTTP（远程）** 则是单独托管服务器，通过网络连接。远程方式一旦部署好，多人共享很方便，但服务器运维、认证和密钥管理都得自己操心。我是在公司里给自己装来用，所以选了 **stdio**——密钥不出本机，安装也简单。

做这个 Redmine 集成时，比写代码更先做的，是写下「LLM 用它应该能做什么」。列出来才发现，平时在 Redmine 里做的事并不多——查看我的任务、搜索和阅读任务、创建任务、写评论、看和改 Wiki。照着这些把工具收敛到 10 个。

| 工具 | 作用 |
|---|---|
| `list_projects` / `list_issues` / `get_issue` | 项目·任务查看 |
| `create_issue` / `add_comment` | 创建任务·评论 |
| `list_wiki_pages` / `get_wiki` / `update_wiki` | Wiki |
| `get_my_today` | 「今天我的任务」快捷工具 |
| `list_enumerations` | 优先级·状态 ID |

这里学到一点：把常用流程单独抽成一个工具——比如 `get_my_today`——LLM 会挑得准得多。还有做的过程中攒下的三条：工具说明（description）要写充分（太简略就会叫错工具），输入 schema 要严格，响应直接把 JSON 原样传回。

## 真正难的不是代码，是分发

一开始我用一个文件（约 420 行）先跑通验证。真正耗时间的是「怎么装到别人电脑上」。各操作系统的路径分支越堆越多，再加上 Python 3.12 的 PEP 668 在某些环境直接拦下 `pip install`。最后干脆重做成正经的 pip 包、改用 pipx 安装，任何系统都两行搞定。

最费心的是动 Claude 的配置文件（`.claude.json`）。它是个共享文件，里面还有别的 MCP 配置，所以我强制在修改前先备份（实际上出过一次合并事故，但立刻就恢复了）。执行路径也用绝对路径写死，而不是直接 `python`，这样系统 Python 版本变了也不会坏。

| 卡点 | 解决 |
|---|---|
| PEP 668 拒绝 `pip install` | 改用 pipx |
| Python 升级后 MCP 不出现 | 命令改成绝对路径 |
| 合并配置时误删了别的条目 | 修改前强制备份 |
| LLM 不调用快捷工具而绕路 | 在 description 里加关键词 |

## 小结

做 MCP 服务器本身意外地简单（Python 400 行左右）。难的是 *分发*、*密钥管理*，以及 *把 description 调到让 LLM 能挑对工具*——就这三件。提前想清楚，几天就能搞定。

为需要的人，我把代码放上去了（[github.com/junstellar/redmine-mcp-jun](https://github.com/junstellar/redmine-mcp-jun)，MIT），可以直接拿去用。不过还是建议自己动手做一次。比如新任务一登记就提醒你的通知，或者把进来的任务自动分析、再自动回一条评论的机器人——把*你自己*真正需要的东西亲手接起来，收获会大得多。
