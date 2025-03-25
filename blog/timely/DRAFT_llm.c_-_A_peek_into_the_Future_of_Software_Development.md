
llm.c - A Peek Into the future of Software Development

"...python and pytorch and everything else is just a crutch because we humans are finite we have finite knowledge intelligence and attention, but actually don't you want to write all code in custom CUDA kernels?" (22m:16s)
- @Andrej Karpathy 

This is the future of software development.

No, not every application needs to be written in CUDA kernels, but as large language models improve, their coding proficiency will as well. So much so, that having humans write code is actually a major efficiency killer. 

LLM.c implemented gpt2 training, inference, and eval in C code achieving 29% less memory, 19% faster training, and compiles + runs 10x faster than it's PyTorch equivalent.

He concludes with: 
"...in the early stages of these llms and their intelligence, they might not be able to write this code from scratch if you just prompted them 'write gpt2 in C' you probably won't get LLM.c, but you're a lot more likely to get it if you put LLM.c in the context of such an llm, and you can expect that the few shot learning would be very helpful for the llm to basically give it example code and so I think LLM.c could be very useful for this example code to give to the LLM as they're about to write all of our custom applications and so I think this is actually not unlikely to happen"

Here's the deal: 
1. Human intelligence is limited by our biology. 
2. Model intelligence scales with compute. 
3. Model performance is improving exponentially.
4. Composite AI Systems outperform singletons. 

What's the takeaway here? 
Build a meticulously curated codebase and draft examples of using your components in scripts and BOOM, you're a few knowledge agents away from implementing almost any use case that your code base supports. 

There are several agent providers that have implemented this, but most agentic systems are still nacent and lack production ready robustness. These projects have gained a lot of traction in the past 2 years, but I have yet to see very many projects that take full advantage of this opportunity.

I got the chance to watch a keynote from Andrej Karpathy on one of his latest projects, LLM.C, which attempts to take the PyTorch eval, train, and inference modules that implement GPT-2 in PyTorch and directly implements it in C and CUDA kernels. Over three months, with a crack team of open source developers, they were able to write C code that compiles instantly, runs instantly, trains 20% faster, and uses 30% less memory, because everything is essentially pre-planned and pre-allocated on a single thread. And it takes only $672 worth of something like 6 hours of H100 GPUs to train GPT-2, which was the foundation, leading state-of-the-art for large-language models back in 2019. He goes on to say that his motivation for this project, beyond the maybe simple reason that he initially began the project with, which included all of these errors that he was seeing that didn't really make any sense when he was trying to run GPT-2 from PyTorch and trying to get around those, it demonstrated that it's technically feasible, although highly non-trivial, to create custom, to write custom CUDA kernels for training models that outperform PyTorch. And that's potentially probably about as good as you can get it. The problem is that it takes a team of developers three months to do every single implementation. And each time you try to do a new model, you're starting from scratch, essentially. You might be able to build up some of the components, but the reality is a lot of that is implemented specifically for GPT-2. The amazing thing that he pointed out is something that I think quintessentially describes the effort that Evangelos Technologies is trying to undertake, which is, you know, you wouldn't be able to arrive at the end product that LLM.C created by simply prompting an LLM to do it. But you would be able to do that if you provided the entirety of the 3,000 lines of code that LLM.C has in the context of a large-language model, and then enabled it with a few-shot prompting and learning to potentially self-extend or create other implementations of it. And so he made a much broader argument that this is really the future of software, and I couldn't agree more. And so I began drafting a Medium article that I think is kind of turning into just a general content article that helped to use the anecdote of LLM.C and this concept of self-extending software agents or software development agents to extend components.

---
![One More Thought](..assets/llmc-OneMoreThought.png)

---


here's the deal. Humans, human intelligence is limited by our biology. Model intelligence scales with compute. Model intelligence is increasing exponentially with each new generation. And composite AI systems outperform singletons across most benchmarks for quality and robustness and performance. Perhaps maybe not cost. And then models collapse without external stimuli, like context and real world data. Because agents and models that operate on generated data tend to collapse in intelligence because they're not getting the right context. They're just giving you essentially dumber and dumber answers because they're synthesis machines. And that's even more relevant today after a recent court ruling that LLMs do not copy. They synthesize information from a recent court case against OpenAI. And I think this also had to do with the New York Times. So I'll need to find that reference. But the agents are composed of data, models, and tools. That's my own definition. If we extend this, if we break down what I mean by data, I mean state and context. And then agents are components within a system. And systems can be described, any system can be described as a graph composed of nodes and edges. Which means that the use case layer, the application layer, that any graph can also represent any data structure or process. So what I'm proposing is the determinants of data, models, tools, agents, graphs, and systems. And leveraging technology to implement these modules and these modules' components. If you can write meticulously crafted, reviewed, and well-implemented with powerful or extremely performant technology, and you have the right decoupling patterns, then you should have an AI-native software system that not only scales, but it can simulate or generate arbitrary versions of different technologies. So instead of sitting down and trying to write all the components that might make up the system, all you need are the bare primitives, all the bare structures and decoupling patterns to help make the technology work, to have this AI-native software system that self-extends itself. It's composable, and these agents and their graphs, and the graphs that define agent qualities, and path qualities, hierarchies, and path networks, those are just some of the options for what intelligence looks like for this, or whatever your use case might be, and it presents a foundation for AI-native software development, where you can structure it more importantly, where you have the ability to scope your questions, and then everything is almost really tangible. It's a truly realized AI-native system. Now, I've decided that I like, generally, people can take these instructions and implement them with their own papers. I have my own technologies that I think are entitled, but I don't have experience in everything, and I think there's plenty of room for other people to innovate with their own technologies, and I've been implementing the decoupling patterns, and the integrations, and the modules of the components and strategies that make up the system. The services, the applications that are capable of being created are established, quite literally, as needed. There are so many benefits to a diverse system like this, and I'd like to highlight a couple pieces of social proof beyond LLM. I think it would be fair to mention that there have already been a few things that have already been implemented, with their own choices of technologies and implementations.





 %% 
March 12 2025 
Authored by Everett Kleven
Reviwed by Evelyn Mitchell
Special Thanks to 
%%