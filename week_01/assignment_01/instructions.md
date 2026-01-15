# MBAi 448 | The AI Landscape  
## Week 01 Assignment: Getting Started with Custom Agents in VS Code

This assignment is designed to get you familiar with using **VS Code**, **GitHub Copilot**, and **Copilot’s Custom Agents capability** to interact with files and shape how AI tools behave. The focus this week is not on building models or writing code, but on developing comfort and intuition with the tooling you will use throughout the course.

You will explore how different agent configurations affect how an AI system interprets and responds to the same material.

---

## Instructions

### 1. Open the assignment folder in VS Code

If you have not already done so, open the `assignment_01` folder in VS Code. You should see `State of AI Report - 2025 ONLINE.txt` and `Agents_in_VS_Code.txt` files in this directory that will serve as the source material for this assignment, along with the `.github/agents` directory in which you will be defining your custom agents.

Make sure GitHub Copilot is enabled and available in your VS Code environment.

---

### 2. Interact with the provided text files using Ask

Before creating any custom agents, spend a few minutes using Copilot’s **Ask** functionality to interact with one or both of the provided `.txt` files.

Try a handful of prompts to get a feel for how Copilot behaves by default. For example, you might ask it to summarize sections, or identify key themes. Feel free to try varying the selected LLM, but pleae note only the `0x` models do not count against your monthly premium request limit.

If you have questions about using the Ask functionality, you can check the VS Code documentation here: https://code.visualstudio.com/docs/copilot/chat/copilot-chat

---

### 3. Create two custom agents with different dispositions

Next, create **two custom agents** with clearly different dispositions or points of view.

Custom agent definitions should live in the `.github/agents` directory. You will find the `demo.agent.md` file from class there as an example. You may delete it, rename it, modify it, or ignore it entirely.

Your two agents should be intentionally different in how they approach the same material. For example, one might be more skeptical, risk-focused, or cautious, while the other might be more optimistic, opportunity-focused, or forward-looking. The specific framing is up to you.

If you have questions about creating custom agents:
- You may use Ask to query the provided `Agents_in_VS_Code.txt` file, or
- You may consult the VS Code documentation:  
  https://code.visualstudio.com/docs/copilot/customization/custom-agents

---

### 4. Refine the agent instructions and observe behavior changes

Once both agents are set up, spend some time refining their instructions. Make small, deliberate changes to how each agent is described and observe how those changes affect the agent’s responses.

Try running the same prompt through both agents multiple times as you refine them. Pay attention to differences in tone, emphasis, what is highlighted or ignored, and how uncertainty is handled.

This part of the assignment is exploratory. You are encouraged to iterate.

---

### 5. Complete the comparison form below

After you have finished exploring and refining your agents, complete the form below.

#### Custom agents used

Agent 1 name and short description:  
(Describe the agent’s intended disposition or perspective.)

Agent 2 name and short description:  
(Describe the agent’s intended disposition or perspective.)

---

#### Prompt comparisons

Use the **same prompt** for both agents in each row.

Prompt 1:  
(Insert the exact prompt used.)

Agent 1 response:  
(Paste the response.)

Agent 2 response:  
(Paste the response.)

---

Prompt 2:  
(Insert the exact prompt used.)

Agent 1 response:  
(Paste the response.)

Agent 2 response:  
(Paste the response.)

---

Prompt 3:  
(Insert the exact prompt used.)

Agent 1 response:  
(Paste the response.)

Agent 2 response:  
(Paste the response.)

---

#### Reflection

Answer the following questions briefly. A few sentences for each is sufficient.

1. How did the custom agent configuration affect the agent’s behavior?  

2. How do you think custom agents could help you in your day-to-day work?  

---

## Submission

Submit to Canvas:
- This completed markdown file, and
- Your Copilot chat history from this assignment (you can copy and paste your chat, or you can export it as a file: https://code.visualstudio.com/docs/copilot/chat/chat-sessions#_export-a-chat-session-as-a-json-file )