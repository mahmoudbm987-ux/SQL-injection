# **SQL Injection Detection & Exploitation Lab Report** 

_Cybersecurity Assessment & Technical Vulnerability Report_ 

|**Project Title**|SQL Injection Detection &<br>Exploitation Tool|**Environment**|Local Testing Lab<br>(VS Code)|
|---|---|---|---|
|**Target Technology**|Python, Flask, SQLite3|**Category**|Web Application<br>Security|



## **1. Executive Summary** 

This lab project demonstrates the mechanisms of **SQL Injection (SQLi)** vulnerabilities within web applications. It features an intentionally vulnerable Python Flask web application and an automated scanning/ exploitation script designed to identify and exploit SQLi entry points. Additionally, it highlights standard remediation techniques using parameterized queries to secure applications effectively against database tampering and authentication bypass. 

## **2. Technical Stack** 

**Python 3 Flask Web Framework SQLite3 Database Requests Module** 

## **3. Project Architecture & Implementation** 

### **A. Vulnerable Application** **<mark>(</mark>** **<mark>`app.py` )</mark>** 

The application simulates an authentication portal using dynamic SQL string formatting without sanitization or input validation: 

```
# Unsafe Query Construction (Vulnerable)
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

### **B. Automated Scanner & Exploiter** **<mark>(</mark>** **<mark>`sqli_scanner.py` )</mark>** 

The scanner tool tests HTTP POST endpoints by sending structured SQLi payloads into the authentication input fields: 

- 

- 

   - <mark>`' OR '1'='1`</mark> — Standard authentication bypass payload. 

   - <mark>`' OR 1=1 --`</mark> — Comment-based query truncation payload. 

- <mark>`' UNION SELECT 1, 'admin', '123' --`</mark> — Union-based extraction payload. 

## **4. Execution & Results** 

During local execution, the scanner successfully interacted with the Flask web server running at <mark>`http:// 127.0.0.1:5000/` :</mark> 

- **Server Launch:** Activated <mark>`app.py`</mark> backend listener on port 5000. 

- 

- **Payload Injection:** Dispatched payloads via automated HTTP POST requests using <mark>`sqli_scanner.py` .</mark> 

- **Outcome:** The system validated injected payloads, enabling unauthorized authentication bypass without valid database credentials. 

## **5. Mitigation & Prevention (Secure Coding)** 

To prevent SQL Injection vulnerabilities, dynamic string formatting in database queries must be completely removed. Developers should implement **Parameterized Queries (Prepared Statements)** where data is separated from code execution: 

```
# Secure Implementation (Parameterized Query)
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

By decoupling user inputs from SQL execution logic, the database engine treats all input parameters strictly as data values, neutralizing malicious payload execution. 

SQL Injection Detection & Exploitation Report • Generated for Technical Project Submission 

