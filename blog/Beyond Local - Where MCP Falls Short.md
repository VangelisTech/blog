

Its almost half way through March of 2025 and Anthropic just closed its Series E round with $3.5 B in funding. At $18.2B raised, the frontier AI research startup has garnered significant traction from it's flagship family of Claude Large Language Models and accompanying software products. Products now include the recently released Claude Code terminal agent as well as the more familiar chat apps on desktop, mobile, and web. These products in conjunction with developer API endpoints and SDKs form the majority of Anthropic's ecosystem. 

Anthropic's latest model release, Claude-3.7,  has received mixed reviews. Our sentiment has aligned with the broader developer community - the thing can code, but tends to over-perform  user requests, generally introducing more re-work than useful code. Given Anthropic's recent emphasis on supporting programming as a primary focus the latest "features" feel more like a chainsaw than the scalpel precision we were used to. This has been especially disappointing since a majority of developers favor Claude-3.5 to even the most advanced reasoning models. 

As a closed source AI R&D firm, Anthropic holds all of the advantages and risks of releasing new models.  The closed-source foundation language model startup has raised billions from backers like Amazon, Google, and Menlo Ventures. This latest round should shore up some of the uncertainty introduced by DeepSeek's disruption earlier in the year, which as you might remember, sent markets into a frenzy with NVIDIA loosing $500B in valuation to a single trading session.  

> [**Open-source software**](https://en.wikipedia.org/wiki/Open-source_software) (**OSS**) is computer software in which the copyright holder grants users the rights to use, study, change, and distribute the software and its source code to anyone and for any purpose. 

DeepSeek represented the first major disruption of big money AI from the open-source software community, and certainly wont be the last. OSS has been a major focus within big tech for decades. Every major tech company relies on open source software to run large swaths of its infrastructure. Behind every cloud managed service lies open-source software that has been optimized on that company's hardware assets and proprietary code. 



There are quite a few beneftis to OSS projects. 

**For Companies** that steward open source software projects. Chiefest among them is the standardization of processes by means of mass adoption. More adoption means a more mature feature set, more focus on security and robust testing, resulting in an all around more compelling piece of software. 

**For contributors**
from multiple companies come together, the developers enjoy more collaboration and transparency, without the burden of  which leads to wider adoption and stronger security. Last but not least, its great marketing to developers. T


**For Consumers** 

So 

Anthropic is no different. It too hold

In fact Anthropic's biggest competitor, OpenAI, who currently dominates usage and adoption of  foundation models has a long history of open source contributions. Many of these projects, including OpenAI's API client SDK and OpenAI Gym have become standardized interfaces within their respective specialty, enabling developers to contribute to and enjoy a larger ecosystem of interoperable software. 

To make it crystal clear, open source projects that become industry standard, become the bedrock for adoption. They form the first filter in the funnel through which downstream projects can 

This standardization effect is most prevelent when it comes to Protocols. 

> **Protocol** (computing)
> A set of rules governing the exchange or transmission of data between devices.

Lets start with the basics...

### What is MCP  ?

Back in November, Anthropic [introduced](https://www.anthropic.com/news/model-context-protocol) *Model Context Protocol* as an open source protocol to standardize how applications provision context and tools to LLMs. The pitch is pretty straightforward: The burgeoning AI Tools ecosystem is fragmented and needs a standardized means of connecting LLMs with data sources and tools. This isn’t the same thing as tool-use, as I will elaborate on later, but instead a means of providing a two way connection for an Agent to request resources and have that resource respond.

---
![[MCP-Request-Diagram.png]]
%%MCP's Sequence Diagram%%

---

MCP uses a client-server model to achieve this, enabling the user of a given client to connect to multiple resources and tools over the network. Most modern web apps use a client-srever architecture nowadays, but since LLMs aren’t just . In short, this helps AI app developers setup resources and tools once, and simply request that resource in a chat interface later under some sort of command or mention (using slash or @).

Since its introduction, MCP has garnered significant adoption, thanks in part to Anthropic’s reputation as a foundation model provider and it’s growing language support. Several major AI tool providers (considered clients in MCP) have adopted the standard with a majority of them focused on IDE based coding assistants. As of writing this post in February of 2025, MCP maintains SDKs in Python, TypeScript, Java, and Kotlin, all of which uses JSON-RPC 2.0 for the transport layer.

### On Adoption

Recently there has been a massive influx of new MCP integrations on both the client and server side. Naturally, servers present the most benefit to users, with integrations with Docker, Kubernetes, and Github

I came back to the protocol earlier today after I saw a feature within Cursor to add your own MCP server. For Cursor (AI enabled VS Code) the idea here is that you can give chat or composer programmatic access to your data and tools by using MCP's prebuilt primitives. Digging in to the source code, the first thing I wanted to find was the context engine. Specifically, how does MCP prompt LLMs to use tools or resources?

### How does MCP work?

For this, everything comes down to the [_Sampling_](https://modelcontextprotocol.io/docs/concepts/sampling) mechanism, which is what enables the MCP _servers_ to request completions from LLMs. MCP's _Sampling_ request schema includes a couple neat features like model selection and context, but technically MCP doesn't actually interface directly with the LLM. 

![[MCPClientFeatureSupportMatrix_Feb2024.png]]

This brings us to our first caveat for MCP.  without an implementation on the client side, your mcp will lack the basic features needed to support [_Sampling_](https://modelcontextprotocol.io/docs/concepts/sampling). 

### Wait… What?

You heard me. Turns out the llm client ends up doing it (as it always has) which means the implementation of how any given application actually uses an llm to choose tools is eventually up to the developer. In MCP, [_clients_](https://modelcontextprotocol.io/clients) actually implement the logic, so innovation is limited by what the _client_ supports. See MCP’s [example client](https://modelcontextprotocol.io/quickstart/client) for their reference implementation. Overall, the fact that MCP doesn’t over specify how an llm selects a tool provides developers with more flexibility, but it does make the Model Context Protocol feel less impressive.



This is where the details start to really matter. MCP is NOT a tool calling framework. MCP gives you the primitives to define tools and resources, but not how they end up being used by the LLM. That burden rests entirely with the client/server developers, which, at the end of the day, is a good thing.

---
### How Tool Calling Works

>If you aren't familiar with how llm clients actually use tools, the implementation is a little more sophisticated than you might think. One of the first libraries to implement tool calling (well) was Outlines from DotTxt. I’m not going to go into all of the details on how the mechanics work, but essentially in order to ensure an llm doesnt hallucinate an incorrect tool calling schema, you have to freeze the logits of the actual model. I highly recommend reading through [Outlines technical docs](https://dottxt-ai.github.io/outlines/latest/reference/generation/structured_generation_explanation/) if you are interested in learning more.

--- 

All in all, MCP is exactly what it says it is, a USB-C cord for llms to interface with external apis. It is not a

### Where MCP falls short

The first thing I will say is MCP is clearly geared towards local systems. JSON-RPC is a decent transport for web focused use-cases, but support for other transports that are common in distributed or Cloud Native technologies would make the project much more enticing.

Why support distributed or HPC technologies? To be curt, the context window problem. Large Language Models can only attend to so many tokens of context before their performance drops off, or they lose the content entirely. The only models where this isn't as big of a problem are the Gemini Models from Google with a minimum of 1M token context window AND [uniform needle-in-the-haystack recall performance](https://cloud.google.com/blog/products/ai-machine-learning/the-needle-in-the-haystack-test-and-how-gemini-pro-solves-it). 

Complex tasks require more context, and if the *Model **Context** Protocol* doesn't solve this issue, then what is it really doing? One might argue that context windowing across models could be implemented client side, but the client is the last place you want to perform mass data processing or orchestration. That needs to happen server side, where the big boi compute is.

The lack of common sense defaults for security is also disappointing. Authentication and TLS should be a mandatory part of the documentation at minimum, especially since this "standard" is intended to become widely adopted. Authentication also opens the door for one of the most lucrative features of any enterprise SaaS application: Access Controls. Using MCP beyond a single user risks the abuse of resources and tools, and for a semi-autonomous system, those risks are highly non-trivial. AGAIN, local only.

Which brings me to my last point. The cost and performance arguments in the sampling request schema is a nice idea, but really MCP doesn't actually implement any model routing logic itself. Again it relies on adopter implementations, which if you actually look at the client adopters, none support _Sampling_ or If you are serving models yourself, either from open source repositories like HuggingFace, or from proprietary models you train internally, model routing should be integrated with your serving infrastructure. You can't call a cheaper model if it isn't spun up yet!

### Quick Links: 
[Docs](https://modelcontextprotocol.io/introduction) 
[Github](https://github.com/modelcontextprotocol)

%% 
Published March 12 2025 
Authored by Everett Kleven
Reviewed by Evelyn Mitchell
Special Thanks to 

The content of this article is subject to copyright of Vangelis Technologies Inc 2025 
%%

