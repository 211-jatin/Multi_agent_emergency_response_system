Here's a **clear and concise explanation** of how your **AI Multi-Agent Emergency Response System** works, along with a **flowchart**.

---

## 🔧 System Overview

### 🧠 Purpose:

Simulate an emergency scenario (e.g., highway accident) using **5 AI agents**, each handling a specific role using **LangChain** and **Gemini LLM**.

---

## 🤖 Agents and Roles

| Agent        | Role                                   |
| ------------ | -------------------------------------- |
| **Dispatch** | Central coordinator, triggers response |
| **Medical**  | Assesses injury severity & triage      |
| **Resource** | Allocates ambulances, helicopters      |
| **Route**    | Finds fastest emergency routes         |
| **Traffic**  | Monitors congestion, gives detours     |

---

## 📂 Project Files

| File                     | Purpose             |
| ------------------------ | ------------------- |
| `emergency_response.py`  | Main system script  |
| `README.md`              | Project explanation |
| `output.txt`             | Simulation output   |
| `requirements.txt`       | Dependencies list   |
| `emergency_response.log` | Logs for debugging  |

---

## ⚙️ System Flowchart

```plaintext
          [Start System]
                │
                ▼
     ┌────────────────────────┐
     │ Dispatch Agent receives│
     │ emergency report       │
     └──────────┬─────────────┘
                ▼
     ┌────────────────────────┐
     │ Medical Agent assesses │
     │ injury severity        │
     └──────────┬─────────────┘
                ▼
     ┌────────────────────────┐
     │ Resource Agent checks  │
     │ and allocates vehicles│
     └──────────┬─────────────┘
                ▼
     ┌────────────────────────┐
     │ Route Agent finds      │
     │ fastest path           │
     └──────────┬─────────────┘
                ▼
     ┌────────────────────────┐
     │ Traffic Agent suggests │
     │ alternative routes     │
     └──────────┬─────────────┘
                ▼
     ┌────────────────────────┐
     │ Response Complete      │
     │ Resources updated      │
     └────────────────────────┘
```

---

## 🚨 Sample Simulation

* **Scenario**: Highway 101 accident (4 injured)
* **Agents Act**:

  * **Dispatch** triggers coordination
  * **Medical** prioritizes victims
  * **Resource** assigns ambulances & helicopters
  * **Route** finds best path
  * **Traffic** checks congestion, gives detour

---

## 🏁 How to Run

```bash
pip install -r requirements.txt
python emergency_response.py
```
