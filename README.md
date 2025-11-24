# 책 부록 소스 프로젝트 입니다

- 직무 교육( OJT, On the job Training )을 위해서 생성.  
- 진행중( WIP, Work on Progress ).  
  + ...


## 책 관련 링크  

<img src="https://nostarch.com/sites/default/files/styles/uc_product_full/public/Math%20for%20Deep%20Learning.jpg?itok=5yhX8Pha" alt="" height="256px" align="right">


- [Math for Deep Learning [ 원서 ]](https://nostarch.com/math-deep-learning)  

- [딥러닝을 위한 수학 [ 번역서 ]](https://jpub.tistory.com/1304)  

- [딥러닝을 위한 수학 [ 번역서 ]](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=298579204)  


## 시스템 환경  

- 시스템 ( Computer System )  

  - AMD Ryzen 9 7900X 12-Core Processor
  - 32G RAM
  - NVIDIA Geforce RTX 3060 12GB
  - SSD 2TB
  - Windows 11 64bit Korean

- 파이썬 ( Python 3.12 )  

  - [Python Download](https://www.python.org/downloads/)  
    - [v3.12.0 for Windows](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)  
    - [v3.11.9 for Windows](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)  

- 파이썬 가상환경 ( venv )

  > 윈도우즈 파워쉘 실행 정책 변경 필요할 수 있음
    ```
    $ Get-ExecutionPolicy
    $ Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
    $ Get-ExecutionPolicy
    ```
  > venv 환경 실행
    ```
    $ python -m venv .venv
    $ .venv/Scripts/Activate.ps1 
    $ (.venv-) python --version
    $ (.venv-) pip --version
    ```



## 의존 패키지

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


## 기타

- ...  

- ...  


---
---
---

# MathForDeepLearning
Source code for the book "Math for Deep Learning"

Source code is organized by chapter.  If you have questions
or comments, please contact me:

rkneuselbooks@gmail.com

**Updates**
- p 300, the last sentence of the penultimate paragraph should read "Here, t, an integer starting at *one*, is the timestep."
- The file *boston.py* in Chapter 2 was sampling the same person repeatedly at times (thanks to ikimmit for the catch!)
- The file *tutorial.pdf* is a beginner's guide to NumPy, SciPy, Matplotlib, and Pillow.
- p 29, the upper limit on randint should be 365, not 364 (code updated).
- p 198, the derivative of a matrix function should be scalar $\partial x$, not $\partial\mathbf{x}$.
- p 257, the line above Equation 10.10 should be $\left[\frac{\partial E}{\partial y_0}\sigma'(x_0)\ \frac{\partial E}{\partial y_1}\sigma'(x_1)\ \ldots\ \right]^\top$.
- Tweaked the Ch 10 code in *build_dataset.py* to conform to newer Keras versions

