# Winternitz Signatures (one-time signatures)

## **Notebooks**

- [Naive 4 bit Winternitz Signatures](4_bit_winternitz.ipynb): Simple example implementation of Winternitz one-time signatures for 4 bit numbers (signatures **can** be forged)
- [Secure 4 bit Winternitz Signatures](4_bit_winternitz_secure.iynb): Simple example implementation of Winternitz one-time signatures for 4 bit numbers (signatures **cannot** be forged)
- [256 bit Winternitz Signatures](256_bit_winternitz.ipynb): Example implementation of Winternitz one-time signatures for 256 bit message hashes

### **Interface Images**

- [Generate Keypair](images/GENERATE_KEYS_interface.png)
- [Sign Message](images/SIGN_interface.png)
- [Verify Signature](images/VERIFY_interface.png)

### **References**:

<!-- Shorter Signatures for Hash-Based Signature Schemes -->

- [A Certified Digital Signature by Ralph C. Merkle](https://link.springer.com/content/pdf/10.1007/0-387-34805-0_21.pdf): Contains implementation of Winternitz one-time signatures. <!-- located at 5. The Winternitz Improvement-->
- [Updated W-OTS](https://eprint.iacr.org/2011/191.pdf): Winternitz one-time signatures using a parameterized family of functions
- [W-OTS+](https://eprint.iacr.org/2017/965.pdf): Shorter Signatures for Hash-Based Signature Schemes
- [Hash-Based Signatures Part I: One-Time Signatures (OTS)](https://cryptoservices.github.io/quantum/2015/12/04/one-time-signatures.html): Extremely helpful blog post by David Wong on the topic

<!-- TODO: LOOK INTO THESE PAPERS -->
<!-- Johannes Buchmann, Erik Dahmen, and Andreas H ̈ulsing. XMSS - a prac-
tical forward secure signature scheme based on minimal security assump-
tions. In Bo-Yin Yang, editor, Post-Quantum Cryptography, volume 7071
of Lecture Notes in Computer Science, pages 117–129. Springer Berlin /
Heidelberg, 2011. -->
<!-- Johan H ̊astad, Russell Impagliazzo, Leonid A. Levin, and Michael Luby. A
pseudorandom generator from any one-way function. SIAM J. Comput.,
28:1364–1396, March 1999. -->
