# Cryptography for Kids

Refer to [Digital Certificate](https://www.bing.com/videos/riverview/relatedvideo?&q=digital+certificate&adlt=strict&mid=8030B3595712EB787C998030B3595712EB787C99&&FORM=GVRPTV)

## Introduction

A few years back, me and my friends wanted to plan about our gifts for our other friend, Advika's birthday. We wanted to communicate in secret so that Advika wouldn't know about our plans.That day I asked my father what we could do and he told me about cryptography and then me and my friends used the shift code to talk about it.This code involves encrypting the message using a key. The key is a number, for example if the key is 3 then, A will become X.Then I started learning more about cryptography I explored many topics like Post Quantum Cryptoghraphy, [Diffie-Hellman](https://www.bing.com/videos/riverview/relatedvideo?&q=diffie+hellman&adlt=strict&mid=9C33D774D1A6FBE6CC9D9C33D774D1A6FBE6CC9D&&FORM=VRDGAR),RSA and more.
 
**Below is the shift for shift 3**

| Plain Character | Cipher Character |
| --- | --- |
| A | X |
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


```mermaid
flowchart
    subgraph Alice
        pA[/Plain Text\]
        cA[Cipher Text]
        skA[/Symmetric Key/]
        eaA([Encryption <br> Algorithm])
        haA([Hashing <br> Algorithm])
        hA[Hash]
        dsA[Digital <br> Signature]
        keaA([Key Exchange <br> Algorithm])

        pA --> eaA
        skA --> eaA
        skA --> keaA
        eaA --> cA
        cA --> haA
        haA --> hA
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
    style skA fill:skyblue
    style hA fill:lightgreen
    style dsA fill:lightgreen
    style hB fill:skyblue
    style dsB fill:skyblue
    style cB fill:skyblue
    style keaA fill:violet
    style skB fill:skyblue
    style ha1B fill:orange
    style h1B fill:yellow
    style ve fill:violet
    style cm fill:lightgreen
    style wm fill:red
    style dc fill:orange
```