## 수 ( *Number* )  

- "1"
  - 하나 일  
  - 완전체  
  - 단위  
  - 객체  
    * 같다고 생각되는 것들의 각각을 말함
    * 분류 ( *Classify* )
    * 같은 속성, 같은 행동

- “1 = 1”
  - 자신은 자신과 같다

    $$
    a = a
    $$

  - 같다고 생각되는 것들이 서로 같다

    $$
    object = object
    $$

- 등식 ( *Equation* )
  - 2개의 수학적 표현이 같다
  - 항등식 : 언제나 성립

    $$
    (a+b)^2 = a^2 + 2ab + b^2
    $$

  - 방정식 : 특정값에서 성립

    $$
    2 \times x + 3 = 9 \\
    2x + 3 = 9 \\
    x^2 = 9 \\
    x^2 = -9
    $$

---

## “2 = 1 + 1”

- 1 옆에 1이 또 있다

  $$
  2 := 1 + 1
  $$

  > 2는 1의 다음수

- 3 = 2 + 1

  $$
  3 := 2 + 1 := 1 + 1 + 1
  $$

  > 3은 2의 다음수

- 10진법, 2진법, 8진법, 16진법

---


## 변수 ( *Variable* )  

### **변수의 기본 정의**

변수란 **값이 변할 수 있는 수(숫자)를 대신하여 사용되는 기호**이다.

가장 흔히 쓰는 기호:

$$
x, \; y, \; z, \; t, \; a, \; b, \; c, \; \theta, \; \lambda, \; \ldots
$$

---

### **변수는 “이름”이다**

변수는 숫자를 저장하는 **라벨(label)** 또는 **이름(name)** 과 비슷하다.

예:

$$
x = 3
$$

여기서 (x)는 “3이라는 값을 가진 이름”.

프로그래밍에서의 변수와 거의 동일한 개념이다.

---

### **수학에서 변수는 ‘임의의 값’을 나타냄**

수학에서 (x) 라고 하면 ‘어떤 특정한 수’가 아니라:

$$
\text{“어떤 수든 될 수 있는 하나의 값”}
$$

예:

$$
x + 2 = 7
$$

이 등식은 **(x)가 어떤 값을 가져야 성립하는가?**를 묻는 것이다.

---

### 4. **함수에서 변수는 입력값**

함수 $f(x)$ 에서 변수 $x$는 **입력**이다.

$$
f(x)=x^2+1
$$

이때

* $x$ : 독립변수
* $f(x)$ : 종속변수 ( $x$ 가 변하면 $f(x)$ 도 변함 )

---

### **변수는 수의 집합을 대표할 수 있다**

예를 들어,

$$
x \in \mathbb{R}
$$

이라는 말은 **“x는 실수 전체에서 임의의 값을 가질 수 있는 변수”** 라는 뜻.

---

### **대수학에서 변수는 ‘미지수(unknown)’의 역할**

방정식에서 변수는 아직 알려지지 않은 값을 의미한다.

예:

$$
2x - 1 = 9
$$

여기서 $x$ 는 **미지수**이며, 해는 $x=5$.

---

### **해석학·미분에서 변수는 극한을 취하는 대상**

예:

$$
\lim_{x\to 0}\frac{\sin x}{x} = 1
$$

여기서 $x$ 는 “0으로 가까워지는 변수”.

---

### **통계에서 변수는 ‘특성(feature)’**

예:

* 사람의 키 → 변수 $X$
* 시험 점수 → 변수 $Y$

통계에서는 변수를 **특성·속성**으로 본다.

---

### **확률에서 변수는 ‘확률변수( *random variable* )’**

확률에서 변수는 단순한 숫자가 아니라:

$$
X : \Omega \to \mathbb{R}
$$

이라는 **함수**로 정의된다.
(표본공간 → 실수)

즉, 변수는 어떤 사건에서 결과가 숫자로 나타나는 “규칙”이 된다.

---

### **변수는 매개변수( *parameter* )와 구분**

변수: 변하는 값
매개변수: 고정되어 있지만 상황을 조절하는 값

예:

$$
f(x)=ax + b
$$

* $x$ : 변수
* $a, b$ : 매개변수 (기울기, 절편)

---


## 스칼라의 연산들


### **스칼라의 사칙연산 (Arithmetic Operations)**


### ● 덧셈 (Addition)

$$
a + b
$$


### ● 뺄셈 (Subtraction)

$$
a - b
$$

### ● 곱셈 (Multiplication)

$$
a \times b
$$

### ● 나눗셈 (Division)

$$
\frac{a}{b}, \quad b \neq 0
$$



---

## 2. **거듭제곱 (Exponentiation)**

### ● 지수 (Power)

$$
a^n \quad ( \; n \in \mathbb{Z}, \mathbb{Q}, \mathbb{R} \; )
$$

예: $ a^2, \; a^{-1}, \; a^{1/2} = \sqrt{a}$

### ● 지수법칙 (Laws of Exponents)

$$
a^m a^n = a^{m+n}
$$
$$
(a^m)^n = a^{mn}
$$



---

## 3. **로그 연산 (Logarithmic Operations)**

### ● 로그 (Logarithm)

$$
\log_a b = x \quad \Leftrightarrow \quad a^x = b
$$

대표적으로 자연로그 ( $ ln x = \log_e x $ )

### ● 로그 법칙 (Logarithm Laws)

$$
\log(ab)=\log a + \log b
$$

$$
\log a^r = r\log a
$$



---

## 4. **절대값 (Absolute Value)**

$$
|a| =
\begin{cases}
\;  a, & a \ge 0 \\
\; -a, & a < 0
\end{cases}
$$

거리(distance)를 나타내는 개념.



---

## 5. **근 연산 (Roots)**

$$
\sqrt[n]{a} = a^{1/n}
$$

특히 ( $\sqrt{a}$ ) (square root)

---

## 6. **삼각함수 (Trigonometric Functions)**

(실수 스칼라에 대해서)

### ● 기본 삼각함수

$$
\sin x, \; \cos x, \; \tan x
$$

### ● 역삼각함수

$$
\arcsin x, \; \arccos x, \; \arctan x
$$

▶️ **키워드:** trigonometric functions, inverse trigonometric functions

---

## 7. **지수함수 (Exponential Function)**

$$
e^x
$$
성장/감소의 기본 모델.


---

## 8. **미분 (Differentiation)**

스칼라 변수 (x)에 대한 함수 (f(x))의 변화율.

예:

$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$


---

## 9. **적분 (Integration)**

스칼라 변수의 구간에서 면적 또는 누적량을 구함.

예:

$$
\int x^n dx = \frac{x^{n+1}}{n+1} + C
$$



---

## 10. **극한 (Limits)**

스칼라 값이 특정 값에 접근할 때 함수의 행동을 분석.

$$
\lim_{x \to a} f(x)
$$



---

## 11. **연속성 (Continuity)**

$$
\lim_{x\to a} f(x) = f(a)
$$



---

## 12. **대수적 성질 (Algebraic Properties)**

실수 스칼라는 다음 성질을 만족한다:

### ● 교환법칙 (Commutative Law)

$$
a+b=b+a,\quad ab=ba
$$

### ● 결합법칙 (Associative Law)

$$
(a+b)+c=a+(b+c)
$$

### ● 분배법칙 (Distributive Law)

$$
a(b+c)=ab+ac
$$


---

## 13. **복소수 연산 (Complex Number Operations)**

스칼라가 복소수일 때:

$$
z = a + bi
$$

### ● 켤레 (Conjugate)

$$
\overline{z}= a - bi
$$

### ● 절대값 (Magnitude)

$$
|z|=\sqrt{a^2+b^2}
$$

### ● 오일러 공식 (Euler's formula)

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$





---




