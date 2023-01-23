# Hash Chain Benchmarks

Running the `hash_chain` on a M1 Macbook in python. Data sourced from running `%timeit` inside a jupyter notebook. Because hash functions run in constant time, the time to complete a hash chain is linear in the length of the chain.

<!--
```python notebook
for i in range(1, 22):
    %timeit hash_chain(2**i, random_bytes)
```
-->

## SHA3-256

| Hash Chain Length | Speed             |
| ----------------- | ----------------- |
| $2^0$             | 768 ns ± 6.7 ns   |
| $2^1$             | 1.55 µs ± 11.1 ns |
| $2^2$             | 2.76 µs ± 43.1 ns |
| $2^3$             | 5.2 µs ± 67.1 ns  |
| $2^4$             | 9.94 µs ± 50.9 ns |
| $2^5$             | 19.8 µs ± 43.3 ns |
| $2^6$             | 39.2 µs ± 172 ns  |
| $2^7$             | 77.2 µs ± 414 ns  |
| $2^8$             | 154 µs ± 1.14 µs  |
| $2^9$             | 307 µs ± 2.23 µs  |
| $2^{10}$          | 627 µs ± 6.36 µs  |
| $2^{11}$          | 1.24 ms ± 8.59 µs |
| $2^{12}$          | 2.48 ms ± 33 µs   |
| $2^{13}$          | 4.94 ms ± 33.7 µs |
| $2^{14}$          | 9.95 ms ± 70.9 µs |
| $2^{15}$          | 20.1 ms ± 73.5 µs |
| $2^{16}$          | 39.4 ms ± 124 µs  |
| $2^{17}$          | 80.6 ms ± 413 µs  |
| $2^{18}$          | 161 ms ± 1.39 ms  |
| $2^{19}$          | 317 ms ± 4.48 ms  |
| $2^{20}$          | 645 ms ± 5.36 ms  |
| $2^{21}$          | 1.29 s ± 5.88 ms  |

## BLAKE2s

| Hash Chain Length | Speed              |
| ----------------- | ------------------ |
| $2^{1}$           | 734 ns ± 1.07 ns   |
| $2^{2}$           | 1.18 µs ± 0.819 ns |
| $2^{3}$           | 1.96 µs ± 1.01 ns  |
| $2^{4}$           | 3.7 µs ± 6.03 ns   |
| $2^{5}$           | 6.8 µs ± 3 ns      |
| $2^{6}$           | 13.7 µs ± 17.9 ns  |
| $2^{7}$           | 27.2 µs ± 113 ns   |
| $2^{8}$           | 53.9 µs ± 84.2 ns  |
| $2^{9}$           | 109 µs ± 106 ns    |
| $2^{10}$          | 210 µs ± 466 ns    |
| $2^{11}$          | 438 µs ± 1.5 µs    |
| $2^{12}$          | 843 µs ± 635 ns    |
| $2^{13}$          | 1.68 ms ± 1.66 µs  |
| $2^{14}$          | 3.51 ms ± 7.83 µs  |
| $2^{15}$          | 6.72 ms ± 3.99 µs  |
| $2^{16}$          | 13.4 ms ± 4.52 µs  |
| $2^{17}$          | 26.9 ms ± 35.3 µs  |
| $2^{18}$          | 54.1 ms ± 17.9 µs  |
| $2^{19}$          | 112 ms ± 155 µs    |
| $2^{20}$          | 217 ms ± 1.17 ms   |
| $2^{21}$          | 438 ms ± 4.86 ms   |

<!-- Below is the python code used to plot the results.

```python
# Total number of hashes completed
hash_chain_length = 2 ** np.arange(1, 22)

# Time recorded in seconds
time = np.array([
    1.55 * (10**(-6)),
    2.76 * (10**(-6)),
    5.2 * (10**(-6)),
    9.94 * (10**(-6)),
    19.8 * (10**(-6)),
    39.2 * (10**(-6)),
    77.2 * (10**(-6)),
    154 * (10**(-6)),
    307 * (10**(-6)),
    627 * (10**(-6)),
    1.24 * (10**(-3)),
    2.48 * (10**(-3)),
    4.94 * (10**(-3)),
    9.95 * (10**(-3)),
    20.1 * (10**(-3)),
    39.4 * (10**(-3)),
    80.6 * (10**(-3)),
    161 * (10**(-3)),
    317 * (10**(-3)),
    645 * (10**(-3)),
    1.29,
])

plt.plot(hash_chain_length, time)
plt.show()
``` -->
