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