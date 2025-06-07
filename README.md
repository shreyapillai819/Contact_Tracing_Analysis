

# **Contact Tracing System** 🦠  

## **Description**  
This project is a **Contact Tracing System** that processes interaction logs to:  
✅ Identify **potentially infected individuals** based on a contagious period.  
✅ Detect **super spreaders** based on a contact threshold.  
✅ **Find all contacts** a given person met within a specific time window.  
✅ Generate reports and **visualize** the contact network.  

The system supports **manual input** and **predefined test cases** for evaluation.  

---

## **📂 Project Structure**  

```
/project_root
│── /src                      # Contains all source code files
│   │── contact_tracing.py     # Core logic (infection tracing, super spreaders, reports)
│   │── main.py                # Main entry point (User input & test execution)
│   │── test_cases.txt          # Predefined test cases (JSON format)
│   │── test_runner.py          # Automated test execution
│── /reports                  # Stores generated reports
│── /bin                      # (Optional) Stores compiled binaries if needed
│── /resume                   # Contains resume files
│── /venv                     # Virtual environment folder (dependencies)
│── README.md                 # Documentation (this file)
│── requirements.txt          # List of dependencies
```

---

## **📂 Explanation of All Folders**  

### **`/src` - Source Code Directory**
This folder contains the main program files.  

- `contact_tracing.py` → Implements **infection tracing**, **super spreader detection**, **contact search**, **report generation**, and **graph visualization**.  
- `main.py` → Entry point for **running the program**, handling **user input**, and displaying **results**.  
- `test_cases.txt` → Contains **predefined test cases** in JSON format.  
- `test_runner.py` → Automates **test execution** by comparing actual vs. expected results.

---

## **🛠️ Setting Up a Virtual Environment**  

To ensure that dependencies do not interfere with system-wide packages, create a **virtual environment (`venv`)** before running the program.  

### **1️⃣ Create a Virtual Environment**  
Run the following command inside the project directory:  

```sh
python3 -m venv venv
```

This will create a folder named `venv` that contains an isolated Python environment.

---

### **2️⃣ Activate the Virtual Environment**  
After creating the virtual environment, activate it:  

#### **For macOS/Linux:**
```sh
source venv/bin/activate
```

#### **For Windows:**
```sh
venv\Scripts\activate
```

You will see `(venv)` appear before your terminal prompt, indicating the virtual environment is active.

---

### **3️⃣ Install Dependencies**  
Once the virtual environment is activated, install all required dependencies:

```sh
pip install -r requirements.txt
```

This will install:  
- `networkx` → For contact tracing network analysis.  
- `matplotlib` → For visualizing the contact tracing network.  
- `jsonschema` → For validating test cases in JSON format.  

---

### **4️⃣ Running the Program in the Virtual Environment**  
Once the virtual environment is **activated**, run the program:

```sh
python src/main.py
```

---

### **5️⃣ Deactivate the Virtual Environment (When Done)**  
To exit the virtual environment, run:

```sh
deactivate
```

Your terminal will return to normal, and your system's global Python environment will be used again.

---

## **🏃 Running the Program**  

### **1️⃣ Run Manually (User Input Mode)**
To manually enter interaction data, **ensure the virtual environment is activated**, then run:  

```bash
python src/main.py
```

Follow the on-screen prompts to input test cases.  

### **2️⃣ Run with Predefined Test Cases**  
To execute the program using predefined test cases:  

```bash
python src/main.py
```
Choose **option 2** when prompted, then select a test case from the list.

---

## **🧪 Running Tests**  
To run all test cases and verify correctness, **ensure the virtual environment is activated**, then execute:  

```bash
python src/test_runner.py
```

✅ If all tests pass, you'll see **"All tests passed!"**  
❌ If any test fails, an error message will indicate what went wrong.  

---

## **🔎 Finding Contacts of a Person**  
To find all contacts a given person met within a time window:  

1. **Ensure the virtual environment is activated.**  
2. **Run the program:**  
   ```bash
   python src/main.py
   ```
3. **Enter test case manually or choose from predefined ones.**  
4. **When prompted, enter:**  
   - The **name of the person** whose contacts you want to find.  
   - The **time window (in hours).**  
5. The program will output all contacts within the given time window.

---

## **📄 Report Generation**  
After execution, a **JSON report** is generated at:  
```bash
reports/contact_tracing_report.json
```
This contains:  
- **List of infected individuals**  
- **Identified super spreaders**  

---

## **📊 Graph Visualization**  
To see the contact tracing network **graphically**, the program automatically displays a graph if interactions exist.  

📌 **Color Legend:**  
- 🔴 **Red**: Infected individuals  
- 🟠 **Orange**: Super spreaders  
- 🔵 **Blue**: Unaffected individuals  

---

