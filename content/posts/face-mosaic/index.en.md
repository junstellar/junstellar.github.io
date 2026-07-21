---
title: "🫥 Mosaic the Faces in Your Photos — No Server, Right in the Browser"
description: "I built a small web tool that finds and mosaics faces entirely inside your browser, without uploading the photo to any server. It runs on Google MediaPipe's on-device face detection, and you can hide faces with mosaic, blur, a black box, or an emoji."
slug: "face-mosaic"
date: 2026-07-01T07:00:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "web", "privacy", "security", "MediaPipe", "build-it-yourself"]
---

I added a small tool to the blog. [Face Mosaic](/tools/face-mosaic/) — a web tool that automatically finds and hides faces in a photo.

When you post a photo to social media or a blog, you sometimes need to hide the face of someone else caught in the frame. Usually that means installing an app, or uploading the photo to a website you don't really know. But **handing your face photos to someone else's server** just feels uneasy. So I built a tool where **the photo never leaves your browser** in the first place.

The key to finding faces without a server is **on-device AI**. It runs Google's [MediaPipe Face Detector](https://developers.google.com/mediapipe) model directly in the browser. You download the model file (about 200KB) once, and from then on:

1. The photo is loaded onto a canvas
2. The browser locates the faces
3. The effect is applied to those regions

All of this happens **inside your own computer**. The photo is never sent to a server, not even once.

I implemented **four ways to hide a face**:

- **Mosaic** — the classic pixelation
- **Blur** — soften it gently
- **Black box** — cover it completely
- **Emoji** — hide it under 😀🐱⭐

Strength and coverage area are adjustable with sliders. The detection model isn't perfect — it can miss profiles or small faces — so for those cases you can **drag a region by hand** to add one, or click a wrong one to remove it.

In fact, this tool was **built with Claude Code**. Even if you don't really know how to code, you can get this far just by talking to it: "make me a web page that mosaics faces in photos." You can absolutely build your own. And from a security standpoint, **building it yourself is actually the surest path.** Of course, if that's too much hassle, **just use the one I've made** — the photo never leaves your browser anyway.

### Try it

👉 **[Open the Face Mosaic tool](/tools/face-mosaic/)**

You can also reach it anytime from **Tools** in the top menu.
