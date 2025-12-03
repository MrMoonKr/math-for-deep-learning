## **1장. 실습 환경 구축 *( Setting the Stage )***  

- 1.1 도구 모음 설치 *( Installing the Toolkits )*  
  - 1.1.1 리눅스 *( Linux )*  
  - 1.1.2 맥OS *( macOS )*  
  - 1.1.3 윈도우 *( Windows )*  
    * 파이썬 *( Python )*  
    * IDE : 통합개발환경 *( VS Code )*  
      ```
      $ (.venv) python --version
      $ (.venv) pip --version
      ```

- 1.2 넘파이 *( NumPy )*  
  - 1.2.1 배열 정의 *( Defining Arrays )*
  - 1.2.2 데이터 형식 *( Data Types )*
  - 1.2.3 2차원 배열 *( 2D Arrays )*
  - 1.2.4 영 배열과 원 배열 *( Zeros and Ones )*
  - 1.2.5 고급 색인 조회 *( Advanced Indexing )*
  - 1.2.6 디스크 읽기와 쓰기 *( Reading and Writing to Disk )*

- 1.3 사이파이 *( SciPy )*

- 1.4 맷플롯립 *( Matplotlib )*

- 1.5 사이킷런 *( Scikit-Learn )*

- 1.6 요약 *( Summary )*

---

## 파이썬 실습 환경



---


## 패키지 설치

**다음과 같은 순서로 설치하세요.**
  
```
$ (.venv) pip install ipykernel numpy matplotlib scipy  
$ (.venv) pip install scikit-learn  
$ (.venv) pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
$ (.venv) pip install lightning
```

**모듈정보**
- numpy
  - [pypi](https://pypi.org/project/numpy/)  
    ```
    $ (.venv) pip install numpy
    ```
  - Fundamental Package for Array Computing in Python

- matplotlib
  - [pypi](https://pypi.org/project/matplotlib/)  
    ```
    $ (.venv) pip install matplotlib
    ```
  - Python Plotting Package

- scipy  
  - [pypi](https://pypi.org/project/scipy/)  
    ```
    $ (.venv) pip install scipy
    ```
  - Fundamental algorithms for scientific computing in Python

- scikit-learn
  - [pypi](https://pypi.org/project/scikit-learn/)  
    ```
    $ (.venv) pip install scikit-learn
    ```
  - A set of python modules for machine learning and data mining

- ipykernel
  - [pypi](https://pypi.org/project/ipykernel/)  
    ```
    $ (.venv) pip install ipykernel
    ```
  - [ipykernel](https://github.com/ipython/ipykernel)  
  - IPython Kernel for Jupyter

- PyTorch
  - [pypi](https://pypi.org/project/torch/)  
    ```
    $ (.venv) pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
    ```
  - [PyTorch](https://pytorch.org/)  
  - Tensors and Dynamic neural networks in Python with strong GPU acceleration
  - nvidia-smi v531.15
  - cuda-toolkit v12.8

- PyTorch Lightning
  - [pypi](https://pypi.org/project/lightning/)  
    ```
    $ (.venv) pip install lightning
    ```
  - [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/)  
  - The deep learning framework to pretrain, finetune and deploy AI models  
  - PyTorch Lightning is just organized PyTorch - Lightning disentangles PyTorch code to decouple the science from the engineering.
  - ...  

- ...
  - [pypi]()  
    ```
    $ (.venv) pip install ...
    ```
  - [...]()
  - ...  

---


## 라인 매직 명령어 *( Line Magic Commands )*  

| 순위  | 매직                        | 설명                                        |
| ---:  | ---                         | ---                                         |
| **1** | **`%matplotlib inline`**    | Matplotlib 그래프를 Notebook 내부에 출력    |
| **2** | **`%time`**                 | 단일 코드 실행 시간 측정 |
| **3** | **`%timeit`**               | 반복 실행 시간 측정(정확하고 신뢰도 높음) |
| **4** | **`%run <file.py>`**        | 외부 Python 스크립트 전체 실행 |
| **5** | **`%load <file.py>`**       | 파일 내용을 현재 셀로 불러오기 |
| **6** | **`%pwd`**                  | 현재 작업 디렉토리 출력 |
| **7** | **`%cd <path>`**            | 디렉토리 이동 |
| **8** | **`%ls`**                   | 현재 폴더 파일 목록 표시 |
| **9** | **`%pip install <pkg>`**    | pip 패키지 설치(Jupyter 공식 권장 방식) |
| **10** | **`%conda install <pkg>`** | conda 패키지 설치 |
| **11** | **`%who`**                 | 현재 세션의 변수 이름 목록 출력 |
| **12** | **`%whos`**                | 변수 목록 + 타입/크기/값 요약 출력(디버깅 매우 유용) |
| **13** | **`%history`**             | 실행 히스토리 전체 또는 범위별 출력 |
| **14** | **`%reset`**               | 변수 전체 초기화 (옵션 `-f` 강제 초기화) |
| **15** | **`%env`**                 | 환경 변수 조회/설정 |
| **16** | **`%config`**              | Jupyter 렌더링 및 백엔드 설정 |
| **17** | **`%autoreload`**          | 외부 Python 모듈 수정 시 자동으로 재로드 |
| **18** | **`%xmode`**               | 에러 출력 모드를 Plain/Context/Verbose로 변경 |
| **19** | **`%precision`**           | float 출력 자리수 조절 (예: numpy 결과 formatting) |
| **20** | **`%store`**               | Notebook 간 변수 저장 및 불러오기(세션 간 공유) |


## 셀 매직 명령어 *( Cell Magic Commands )*  

| 순위  | 매직                        | 설명 |
| ---   | ---                         | ---  |
| **1** | `%%time`                    | 셀 전체 실행 시간 측정  |
| **2** | `%%timeit`                  | 셀 전체 반복 실행 시간 측정 |
| **3** | `%%writefile filename`      | 셀 내용을 파일로 저장 |
| **4** | `%%capture`                 | 셀의 stdout/stderr 출력 숨기기 또는 변수로 저장 |
| **5** | `%%bash`                    | 셀을 Bash 스크립트로 실행 |
| **6** | `%%script <lang>`           | Bash/Python/Ruby 등 다른 인터프리터로 실행  |
| **7** | `%%html`                    | 셀을 HTML 렌더링  |
| **8** | `%%markdown`                | 셀을 Markdown 렌더링  |
| **9** | `%%latex`                   | 셀을 LaTeX 렌더링 |
| **10** | `%%javascript`             | 셀을 JS로 실행  |
| **11** | `%%svg`                    | SVG 렌더링  |
| **12** | `%%debug`                  | 이전 에러에 대한 디버깅 모드 실행 |
| **13** | `%%prun`                   | 셀 전체 프로파일링  |
| **14** | `%%cython`                 | Cython 코드 컴파일/실행 (확장 필요) |
| **15** | `%%perl` / `%%sh`          | Perl, Ruby, Shell 등으로 실행 (환경 필요) |



