
``` mermaid
flowchart LR
    
    subgraph Inputs
        IT[Topic]
        IP[Purpose]
        IR[Reference Sources]
        IO[Story Outline]
    end 


    IT --> C[Content Bucket]
    IP --> C
    IR --> C
    IO  --> C
    
    subgraph Content Formats
        B[Blog Post]
        P[Podcast]
        %% R[Repository]
        %% SAAS[SaaS Product]
    end

    C --> B[Blog Post]
    C --> P[Podcast]


    subgraph Blog Categories
        Meta
        Timeley
        Timeless
        Cyclical
        Authoritative
    end 

    subgraph Podcast Categories
        Interview
        PR[Paper Reading]
        Event
    end 


    %% Colors by modality style id1 fill:#f9f
    subgraph Derivative Content
        




    end

    subgraph Localization
        Arabic
        Catalan
        Chinese
        Czech
        Danish
        Dutch
        English
        Finnish
        French
        German
        Greek
        Hebrew
        Hungarian
        Indonesian
        Italian
        Japanese
        Korean
        Malay
        Norwegian
        Polish
        Portuguese
        Romanian
        Russian
        Spanish
        Swedish
        Thai
        Turkish
        Ukrainian
        Vietnamese
    end

    C --> D


    S --> SX[Twitter]
    S --> SL[LinkedIn]
    S --> SY[YouTube]
    S --> SF[Facebook]

    B --> BT[Twitter Article]
    B --> BL[LinkedIn Article]
    B --> BM[Medium]
   
    
    DSV[Short Form Video]

    
 
```