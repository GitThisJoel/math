from collections import defaultdict


class Prime:
    seq: list[int] = []
    curr_prime = -1

    def __init__(self) -> None:
        pass

    def is_prime(self, n: int) -> bool:
        if n == 2:
            return True
        elif n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def next_prime(self) -> int:
        self.curr_prime += 1
        while not self.is_prime(self.curr_prime):
            self.curr_prime += 1
        return self.curr_prime

    def prime_sequence(self, length: int) -> list[int]:
        seq = []
        while len(seq) < length:
            seq.append(self.next_prime())
        return seq

    def prime_sequence_upto(self, upper: int) -> list[int]:
        if upper < 2:
            return []

        seq = []
        self.curr_prime = 1
        while self.curr_prime < upper:
            seq.append(self.next_prime())
        return seq[:-1]

    def goldbach_conjecture(self, e: int) -> tuple[int, int]:
        """
        The Goldbach Conjecture states that for every even number larger than 4,
        can be written as the sum of two primes p + q.

        param: n
        """

        if e % 2 == 1 or e < 4:
            print(f"error: input {e=} is not even or smaller than 4.")
            return -1, -1
        seq = self.prime_sequence_upto(e)
        for p in seq:
            q = e - p
            if self.is_prime(q):
                break
        assert p + q == e
        return p, q

    def decomposition(self, n: int) -> dict[int, int]:
        if n < 1:
            return {}

        comp = defaultdict(lambda: 0)
        self.curr_prime = 2
        while n > 1:
            while n % self.curr_prime == 0:
                n //= self.curr_prime
                comp[self.curr_prime] += 1
            self.next_prime()
        return dict(comp)

    def fancy_decompostion(self, n: int, decomp: dict[int, int] | None = None) -> str:
        if decomp is None:
            decomp = self.decomposition(n)

        str_decomp = "+".join(
            f"{x}^{p}" if p > 1 else str(x) for x, p in decomp.items()
        )
        return f"{n}={str_decomp}"

    def first_factor(self, n: int) -> int:
        """
        Return the first factor of a number `n`.
        """

        if n < 2:
            return n

        self.curr_prime = 2
        while n % self.curr_prime != 0:
            self.next_prime()
        return self.curr_prime


if __name__ == "__main__":
    prime = Prime()

    l = 10
    print(f"prime sequence of length {l}")
    seq = prime.prime_sequence(l)
    print(seq)
    assert all(prime.is_prime(x) for x in seq)

    print()

    u = 15
    print(f"prime sequence with upper limit {u}")
    seq = prime.prime_sequence_upto(u)
    print(seq)
    assert all(prime.is_prime(x) for x in seq)

    print()

    e = 112
    print(f"goldbach conjecture with {e=}")
    p, q = prime.goldbach_conjecture(e)
    if p != -1 and q != -1:
        print(f"{p} + {q} = {e}")

    ed2 = e // 2
    print(ed2)
    print(f"{prime.is_prime(ed2)=}")

    print()

    print("prime decomposition")
    decomp = prime.decomposition(180)
    fancy_decomp = prime.fancy_decompostion(180)
    print(fancy_decomp)
    print()

    n = 178
    print(f"first factor of {n}")
    first = prime.first_factor(n)
    print(f"first factor = {first}")
