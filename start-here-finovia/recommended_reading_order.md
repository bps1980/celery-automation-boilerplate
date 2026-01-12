# Recommended Reading Order  
### How to explore the ecosystem in the most useful sequence

This reading order helps you understand the **public ecosystem** without exposing any private Finovia logic.

---

## 1️⃣ Start with the Conceptual Layer

### **Finovia Overview (public-safe)**
High-level explanation of incentives, flows, and value movement.  
Does *not* reveal private protocol logic.

---

## 2️⃣ Explore Execution Concepts

### **mini-execution-engine**
- deterministic state  
- event-driven execution  
- contract runtime patterns  

This gives you a feel for how execution works in adjacent systems.

---

## 3️⃣ Understand Backend Structure

### **modular-api-router-tree**
- DTO-driven contracts  
- explicit routing  
- backend clarity  

This models the service boundaries used in Finovia-adjacent systems.

---

## 4️⃣ Learn About State Machines & Pipelines

### **sqlite-pipeline-template**
- state transitions  
- processors  
- pipeline flows  

This mirrors internal processing patterns.

---

## 5️⃣ See Automation in Action

### **celery-automation-boilerplate**
- distributed tasks  
- scheduling  
- orchestration  

This shows how automation layers interact with backend systems.

---

## 6️⃣ Explore Operator UX

### **posovia-ui-mock**
- dashboards  
- workflows  
- operator-first design  

This reflects the UI philosophy around Finovia.

---

## 7️⃣ Look at Edge Automation

### **selenium-anti-detection-starter**
- browser automation  
- modular flows  

This represents external automation edges.

---

## Summary

This order moves from:

**concept → execution → backend → pipelines → automation → UI → edge**

…mirroring the architecture of the ecosystem.
