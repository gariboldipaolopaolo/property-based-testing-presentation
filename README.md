# 🚀 Property-Based Testing: A Practical Introduction  

## 📌 Overview  
This repository provides an introduction to **Property-Based Testing (PBT)** through **theory and hands-on examples**. It includes:  
- 📊 **Slides** covering the fundamental concepts of Property-Based Testing.  
- 🧑‍💻 **Code examples** with **three levels of difficulty**, demonstrating how to apply PBT.
- 🛠 **A runnable test suite** using `hypothesis` and `pytest` to explore edge cases automatically.  

## 🎯 What is Property-Based Testing?  
Property-Based Testing differs from traditional unit tests by focusing on **general properties** of the code rather than specific example-based cases. Instead of manually defining inputs and expected outputs, **PBT generates multiple random inputs**, helping to uncover unexpected behaviors and edge cases.  

## 📂 Repository Structure  
```
📂 property-based-testing  
 ├── 📜 slides/                 # Theoretical introduction (PDF)  
 ├── 📝 property-based-testing.py  # Code examples with 3 difficulty levels
 ├── 📄 README.md               # Project documentation
```

## 🚀 Getting Started  

### 1️⃣ Install Dependencies  
Before running the tests, install the required Python libraries:  
```sh
pip install hypothesis pytest
```

### 2️⃣ Run the Tests  
You can execute the property-based tests using `pytest`:  
```sh
python -m pytest main.py
```

### 3️⃣ Explore the Code  
The `property-based-testing.py` file contains **three levels of difficulty**:  
✅ **Basic**
✅ **Intermediate**  
✅ **Advanced**

## 🛠 Tools & Technologies  
- [Hypothesis](https://hypothesis.works/) – Python's leading Property-Based Testing library.  
- [Pytest](https://docs.pytest.org/) – A powerful testing framework for Python.  

## 📢 Contributing  
Feel free to fork this repository, suggest improvements, or submit PRs! 🚀  
