# What is MCP? Falls Short

![Please Make it Stop](../assets/AndreiKarpathy_MCP_PleaseMakeItStop.png)




## Context

It's Sunday, March 23rdth, 2025

Its over half way through March of 2025 and Anthropic recently closed its Series E round with $3.5B in funding. At $18.2B raised, the frontier AI research startup has garnered significant traction from it's flagship family of Claude Large Language Models and accompanying software products. Products now include the recently released Claude Code terminal agent as well as the more familiar chat apps on desktop, mobile, and web. These products in conjunction with developer API endpoints and SDKs form the majority of Anthropic's ecosystem.

Anthropic's latest model release, Claude-3.7,  has received mixed reviews upon release. Our sentiment has aligned with the broader developer community - the thing can code, but tends to over-perform user requests, generally introducing more re-work than useful code. Given Anthropic's recent emphasis on supporting programming as a primary focus the latest "features" feel more like a chainsaw than the scalpel precision we were used to. This has been especially disappointing since a majority of developers favor Claude-3.5 to even the most advanced reasoning models. 

As a closed source AI R&D firm, Anthropic holds all of the advantages and risks of releasing new models. The closed-source foundation language model startup has raised billions from backers like Amazon, Google, and Menlo Ventures. This latest round should shore up some of the uncertainty introduced by DeepSeek's disruption earlier in the year, which as you might remember, sent markets into a frenzy with NVIDIA loosing $500B in valuation to a single trading session.  

> [**Open-source software**](https://en.wikipedia.org/wiki/Open-source_software) (**OSS**) is computer software in which the copyright holder grants users the rights to use, study, change, and distribute the software and its source code to anyone and for any purpose. 

DeepSeek represented the first major disruption of big-money/closed-source AI from the open-source software community. OSS has been a major focus within big tech for decades. Every major tech company relies on open source software to run large swaths of its infrastructure. Behind every cloud managed service lies open-source software that has been optimized on that company's hardware assets and proprietary code. OpenAI, has a long history of open source contributions. Many of these projects, including OpenAI's API client SDK and OpenAI Gym have become standardized interfaces within their respective specialty

## MCP Rise in Adoption

Recently, MCP has recieved significant adoption across a variety of domains. Several major AI IDE providers have adopted the standard to empower their coding assistants with new capabilities.  Anthropic's first open source project that has garnered significant a public adoption. Cloud providers are emerging to capitalize on the opportunity, and entire startups are forming around indexing them. 



My experience with [this figma context server](https://github.com/GLips/Figma-Context-MCP.git) has been productive. As advertised, after connecting my api token, I was able to provide cursor with a reference link to one of my figma designs and have the agent integrate it into my codebase. 

The experience was a bit surreal, to be honest. The theming was a bit off, but the structure was there. The only caveat was that the server insisted on importing the icons as SVGs, which was easily taken care of in my next prompt. All I did was ask cursor to replace the imported SVGs with lucide icons, which it performed flawlessly. 

This would have normally taken experienced developers at least several hours to do, but I was able to have it implemented with no-cognitive load investment on my end within minutes.

### What is MCP?

Back in November, Anthropic [introduced](https://www.anthropic.com/news/model-context-protocol) *Model Context Protocol* as an open source project to standardize how applications provision context and tools to LLMs. The pitch is pretty straightforward:

*The burgeoning AI Tools ecosystem is fragmented and needs a standardized means of connecting LLMs with data sources and tools.*

This isn't the same thing as tool-use, as I will elaborate on later, but an interface for a two way  connection between a Large Language Model and a _Resources_ or tool. MCP uses a client-server pattern to achieve this, enabling the user to connect multiple _Resources_ and tools over the network. 




Most modern applications use a client-server architecture these days. The introduction of client-server architectures was pioneered in the 1960s by researchers at Standford Research Institute while building ARPANET.  [Wikipedia](https://en.wikipedia.org/wiki/Client%E2%80%93server_model#Early_history) This approach has since become the backbone of modern distributed computing, from web applications to cloud services, making it a natural choice for AI tool integration frameworks like MCP.

 Leveraging the client-server model , Anthropic ensures that developers can easily understand and implement MCP without having to learn entirely new architectural concepts. In practice, this helps AI app developers setup _Resources_ and tools once, and simply request that resource in a chat interface later under some sort of command or mention (using slash or @).

MCP as a convention is an implementation of how to  (tools, _Resources_) how _Resources_ and tools are described to models, provides an interface for how to _Resources_ and tools respond to those requests. 

 
## What MCP is not

There has been quite a bit of confusion on what MCP actually is, particularly since many become aquainted with through developer implementations of different MCP servers. In this section, I want to break down a few of the misconceptions that prevent folks from understanding exactly what value the Model Context Protocol actually provides, and where it fits into the agent frameworks. 

First, *MCP is NOT a container, VM, or program*, it is an interface standard. As a protocol, MCP defines a core set of primatives and implements communication methods that connect how those primatives interact. The formal definition of a protocol is:

>***Protocol** (computing)*
>*A set of rules governing the exchange or transmission of data between devices.*

MCP is the set of rules by which LLM-powered clients exchange requests with tools and _Resources_. These Tools and _Resources_ are implementations of their respective interface standards that wrap a particular piece of software. The utility is entirely dependent on the implementation of the MCP primatives.

Second, *MCP does NOT specify Agent Tool or Resource choice*, it defines primatives for implementing that logic. MCP doesn't dictate which tools should be used but rather provides a communication standard by which tools and _Resources_ are made available for a model to use. The actual selection and execution are left to the client implementation. After all, LLMs seem to intuitively know which tools to use without much direction, provided they're properly described in the interface.

Third, *MCP is NOT a tool calling framework*. MCP gives you the primitives to define tools and _Resources_, but not how they end up being used by the LLM. That burden rests entirely with the client/server developers, which, at the end of the day, is a good thing.

If you aren't familiar with how llm clients actually use tools, the details are a more complicated than you might think. One of the first libraries to implement tool calling (well) was Outlines from DotTxt. I'm not going to go into all of the details on how the mechanics work, but essentially in order to ensure an llm doesnt hallucinate an incorrect tool calling schema, you have to freeze the logits of the actual model. I highly recommend reading through [Outlines technical docs](https://dottxt-ai.github.io/outlines/latest/reference/generation/structured_generation_explanation/) if you are interested in learning more.

All in all, MCP is exactly what it says it is, a USB-C for llms to interface with external apis. This helps LLMs provide more relevant and helpful responses that are grounded in user context.

## Limitations

First of all, MCP is clearly geared towards local systems. JSON-RPC is a decent transport for web focused use-cases, but support for other transports that are common in distributed or Cloud Native technologies would make the project much more enticing.

Why support distributed or HPC technologies? To be curt, the context window problem. Large Language Models can only attend to so many tokens of context before their performance drops off, or they lose the content entirely. The only models where this isn't as big of a problem are the Gemini Models from Google with a minimum of 1M token context window AND [uniform needle-in-the-haystack recall performance](https://cloud.google.com/blog/products/ai-machine-learning/the-needle-in-the-haystack-test-and-how-gemini-pro-solves-it). 

Complex tasks require more context, and if the *Model Context Protocol* doesn't solve this issue, then what is it really doing? One might argue that context windowing across models could be implemented client side, but the client is the last place you want to perform mass data processing or orchestration. That needs to happen server side, where data lives.

The lack of common sense defaults for security is also disappointing. Authentication and TLS should be a mandatory part of the documentation at minimum, especially since this "standard" is intended to become widely adopted. Authentication also opens the door for one of the most lucrative features of any enterprise SaaS application: Access Controls. Using MCP beyond a single user risks the abuse of _Resources_ and tools, and for a semi-autonomous system, those risks are highly non-trivial. AGAIN, local only. The best practices and security recommendations seem more like after thoughts than concious inclusions. 

Which brings me to my last point. The cost and performance arguments in the _Sampling_ request schema is a nice idea, but really MCP doesn't actually implement any model routing logic itself. Again it relies on adopter implementations, which if you actually look at the client adopters, none support _Sampling_ or If you are serving models yourself, either from open source repositories like HuggingFace, or from proprietary models you train internally, model routing should be integrated with your serving infrastructure. You can't call a cheaper model if it isn't spun up yet!

The reality is, a majority of MCP was written by Claude, and several of the implementation details expose MCP as Naive Vibe coding masked as a open source standard. 


## Conclusion

MCP represents a thoughtful contribution to the emerging standards landscape for LLM-tool interactions. Its architectural choices reflect careful consideration of developer ergonomics and implementation flexibility. However, like many early-stage protocols, MCP currently occupies an intermediate position — offering valuable primitives while leaving significant implementation challenges unaddressed. 

The protocol establishes a promising foundation but delegates numerous critical decisions to adopters, which has led to inconsistent implementations across the ecosystem. This fragmentation of approach, somewhat paradoxically, echoes the very interoperability challenges that standardization efforts like MCP aim to resolve. The protocol's current state reflects the inherent tension between prescriptive standards and implementation flexibility that all open specifications must navigate.

For now, MCP occupies a transitional space in the evolving AI ecosystem—a thoughtfully designed interface with significant room for maturation. MCP establishes foundational primitives that may eventually evolve into a robust standard, but for now the protocol's current limitations in distributed computing, security frameworks, and practical model routing remain unaddressed.  

As the open source AI Agents ecosystem continues to develop, MCP has the potential to grow beyond its local-first paradigm into a truly comprehensive standard—provided it embraces the sophisticated technical complexity required to address enterprise-scale challenges while maintaining the elegant simplicity that makes it accessible to individual developers. The path forward likely involves deeper integration with cloud-native technologies and a more prescriptive approach to security and authentication, balancing flexibility with the rigor necessary for production environments.

Lastly, the fact that Anthropic openly admits that a majority of MCP was written by Claude is an immediate red flag for long term staying power. Not just for it's lack of production features, but also for it's siloed perspective on the interoperability challenges of future agentic systems. The abstractions might have itched the AI hype cycle, but the actual MCP transports and server implementation is not likely to hold long term staying power.


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

