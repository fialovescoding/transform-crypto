``` mermaid
flowchart
a[Alice]
    b[Bob :blush:]
    p[/Plain Text\]
    prk[Private Key]
    puk[Public Key]
    t[Tom]
    c[Cipher Text]
    ea([Encryption <br> Algorithm])
    da([Decryption <br> Algorithm])
    cB[Cipher Text]
    daB([Decryption <br> Algorithm])
    ca[Cipher Text]
    a -->  p --> ea --> c --> b
    prk --> ea
    a --> prk
    c --> t
    b --> cB
    t --> ca
    style a fill:orange
    style b fill:turquoise
    style p fill:red
    style puk fill:yellow
    style prk fill:violet
    style ea fill:pink
    style t fill:skyblue
    style c fill:lightgreen
    style da fill:orange
    style cB fill:lightgreen
    style daB fill:orange
    style ca fill:lightgreen
```
