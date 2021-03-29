# C++

**Question 1:** What is the **sizeof** of an empty class? Follow-up: 1) why not zero? 2) what if I add a constructor and a destructor? 3) what if the destructor is virtual? 4) what if I add an int and a double? 5) what if I add an int and a double? (剑指Offer)
<details>
<summary>Answer: </summary> 
(Usually) 1 Byte.

An object has to occupy some physical memory space, otherwise when you instantiate it you wouldn't be able to use it. The size of an empty class is usually 1 byte, but it depends on the compiler and system.

If we add a constructor and a destructor, the **sizeof** will still be one byte. If the destructor is virtual, the **sizeof** will be 8 bytes (in a x386-64 machine, which is 64-bit), since a **vpointer** will be added to point to a **vtable**.

If we add an int, the size will be 4 (in a x386-64 machine), but if we add one more double, the size will be 16, although a double takes 8 bytes and an int take 4 bytes. This is because of **padding**, i.e., shorter types will be padded to align with the longest type.
</details>
<br>

**Question 2:** What's wrong with the following code? (剑指Offer)
```
class A {
private:
    int value;
public:
    A(int n) { value = n; }
    A(A other) { value = other.value; }

    void Print() {std::cout << value << std::endl; }
};

int _tmain(int argc, _TCHAR* argv[]) {
    A a = 10;
    A b = a;
    b.Print();

    return 0;
}
```
<details>
<summary>Answer: </summary> 

Should be
```
A(const A& other)
```
</details>
<br>

**Question 3:** Explain **value type** and **reference type**. (剑指Offer)
<details>
<summary>Answer: </summary> 

</details>
<br>

**Question 3:** Implement a singleton class. (剑指Offer)
<details>
<summary>Answer: </summary> 

</details>
<br>