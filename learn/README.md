# Cryptography for Kids 

## Introduction

A couple of years back, me and my friends wanted to plan about our gifts for our other friend, Advika's birthday. We wanted to communicate in secret so that Advika wouldn't know about our plans.That day I asked my father ([Sunny Gupta]( https://www.linkedin.com/in/sunnygupta1)), what we could do and he told me about cryptography and then me and my friends used the shift code to talk about it.This code involves encrypting the message using a key. The key is a number, for example if the key is 3 then, A will become X.Then I started learning more about cryptography, I explored many topics like Post Quantum Cryptoghraphy, [Diffie-Hellman](https://www.bing.com/videos/riverview/relatedvideo?&q=diffie+hellman&adlt=strict&mid=9C33D774D1A6FBE6CC9D9C33D774D1A6FBE6CC9D&&FORM=VRDGAR), [Digital Certificate](https://www.bing.com/videos/riverview/relatedvideo?&q=digital+certificate&adlt=strict&mid=8030B3595712EB787C998030B3595712EB787C99&&FORM=GVRPTV), [Digital Signature](https://www.bing.com/videos/riverview/relatedvideo?&q=digital+signature&adlt=strict&mid=1FA30248B1778AA313EF1FA30248B1778AA313EF&&FORM=VRDGAR),RSA and more.

TODO: Explain how A becomes X when shift key = 3. Give another example to clarify (add one more column)
 
Below is the shift code for shift key, **k = -3** and **k = 4**

| Plain Character | Cipher Character (k = -3) | Cipher Character (k = 4) |
| --- | --- | --- |
| A | X | E |
| B | Y |
| C | Z | 
| D | A |
| E | B |
| I | F |
| J | G |
| K | H |
| L | I |
| M | J | 
| Q | N |
| R | O |
| S | P |
| T | Q |
| U | R |
| V | S |
| W | T |
| X | U |
| Y | V |
| Z | W |

## What's wrong if Alice sends only plain text?

``` mermaid
flowchart
    subgraph Alice
        p[/Plain Text\]
    end

    subgraph Bob
        ep[/Extracted Plain Text\]
        p --> ep
    end
    
    subgraph Tom
        ept[/Extracted Plain Text\]
        p -.-> ept
    end

    style p fill:red
    style p fill:red
```

If Alice sends only the plain text, it can not be a
secret message because everyone including Tom can see it.

That is why Alice generates a symmetric key. She encrypts the message using the symmetric key and send it to Bob along with the key. Then Bob will decrypt it using Alice's symmetric key.

### What's wrong if Alice sends only the encrypted plain text ?

``` mermaid
flowchart
    subgraph Alice
        p[/Plain Text\]
        sk[/Symmetric Key\]
        ena(Encryption Algorithm)
        c[Cipher Text]
    
        sk --> ena
        p --> ena --> c
    end

    subgraph Bob
        dca(Decryption Algorithm)
        c --> dca
        sk --> dca --> ep
        ep[/Extracted Plain Text\]
    end
    
    subgraph Tom
        dcab(Decryption Algorithm)
        sk -.-> dcab
        c -.-> dcab --> ept
        ept[/Extracted Plain Text\]
    end

    style p fill:red
    style sk fill:yellow
    style ena fill:pink
    style c fill:skyblue
```

If Alice sends only the plain text encrypted with the symmetric key, Tom can stop the message and decrypt it using the key.

To stop this Alice uses a key exchange algorithm, which is exchanging the key, in this case from Alice to Bob.

### What's wrong if we exchange the key?
``` mermaid
flowchart
    subgraph Alice
        p[/Plain Text\]
        sk[/Symmetric Key\]
        ena(Encryption Algorithm)
        c[Cipher Text]
    
        sk --> ena
        p --> ena --> c

        keaA([Key Exchange Algorithm])
        sk --> keaA
    end

    subgraph Bob
        dca(Decryption Algorithm)
        keaB([Key Exchange Algorithm])

        c --> dca
        keaA --> |Wrapped Key| keaB
        
        keaB --> |Extracted Symmetric Key| dca
        dca --> ep
        ep[/Extracted Plain Text\]
    end
    
    subgraph Tom
        dcab(Decryption Algorithm)
        keaA -.-> keaT
        c -.-> dcab --> ept
        ept[/Extracted Plain Text\]

        keaT([Key Exchange Algorithm])
    end

    style p fill:red
    style sk fill:yellow
    style ena fill:pink
    style c fill:skyblue    
    style keaA fill:lightgreen
    style keaT fill:hotpink

```
If Alice exchanges the key Tom could exchange the key with Alice and every message tht Alice sends will be seen by Tom.Then Tom might exchange his own key with Bob and send his own messages to him.

To stop this Alice can sign the cipher text with her digital signature and send it to Bob.Bob will then verify the digital signature and see if the message came from Alice or not.

## Complete Flow Diagram

```mermaid
flowchart
    subgraph Alice
        pA[/Plain Text\]
        cA[Cipher Text]
        skA[/Symmetric Key\]
        eaA([Encryption <br> Algorithm])
        haA([Hashing <br> Algorithm])
        hA[Hash]
        dsA[Digital <br> Signature]
        keaA([Key Exchange <br> Algorithm])
        dsaA([Digital  Signature <br> Algorithm])

        pA --> eaA
        skA --> eaA
        skA --> keaA
        eaA --> cA
        cA --> haA
        haA --> hA
        hA --> dsaA
        dsaA --> dsA

    end

    subgraph Bob 

        cB[Ciper Text]
        h1B[Hash]
        dsB[Digital <br> Signature]
        skB[Symmetric <br> Key]
        ha1B([Hashing <br> Algorithm])
        hB[Hash]
        ve{Check if <br> the hash of <br> the Cipher text <br> and the hash sent <br> by Alice are the same}
        cm[\Correct Message!\]
        wm[\Wrong Message!\]
        dc[Decrypt the cipher text <br> using symmetric key]
        cA-->cB
        hA-->hB
        dsA-->dsB 
        keaA -- Symmetric <br> Key --> skB
        cB-->ha1B
        ha1B-->h1B
        h1B-->ve
        hB-->ve
        ve--Noo-->wm
        ve--Yes-->cm
        cm-->dc
     end

    style pA fill:red
    style cA fill:lightgreen
    style eaA fill:pink 
    style haA fill:orange 
    style skA fill:yellow
    style hA fill:lightgreen
    style dsA fill:lightgreen
    style hB fill:skyblue
    style dsB fill:skyblue
    style cB fill:skyblue
    style keaA fill:violet
    style skB fill:skyblue
    style ha1B fill:orange
    style h1B fill:yellow
    style ve fill:turquoise
    style cm fill:lightgreen
    style wm fill:red
    style dc fill:orange
    style dsaA fill:violet
```

In the diagram above Alice wants secret messages to Bob, but they don't want Tom (who wants to interfare with the secret messages) to get his hands on the message.
