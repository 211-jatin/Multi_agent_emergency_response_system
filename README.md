

## 🗂️ Project File Structure Explained

```
emergency-response-system/
├── README.md                  # Project overview and setup instructions
├── emergency_responce.py      # Main Python file with all agent logic
├── emergency_response.log     # Log file with runtime events and debug info
├── output.txt                 # Stores sample emergency response outputs
├── requirements.txt           # Python dependencies to run the project
```

### File Details:

* **`README.md`**: Summarized explanation of the project.
* **`emergency_responce.py`**: Main script that defines the EmergencyCoordinationSystem, agents, and the simulation.
* **`output.txt`**: Shows the result of running the system (sample output).
* **`emergency_response.log`**: Keeps logs for debugging and tracking.
* **`requirements.txt`**: Contains packages like `langchain`, `google-genai` to install via `pip`.

---

## ⚙️ How the System Works (Simple Explanation)

### Step-by-Step Flow:

1. **System Starts**

   * Initializes 5 AI agents using LangChain + Gemini Flash:

     * Dispatch Agent
     * Medical Agent
     * Resource Manager
     * Route Planner
     * Traffic Controller

2. **Simulation Begins**

   * A highway accident scenario is triggered.

3. **Agents Act in Order**

   * **Dispatch Agent**: Coordinates everything.
   * **Medical Agent**: Assesses injury severity.
   * **Resource Manager**: Allocates ambulances/helicopters.
   * **Route Planner**: Finds fastest routes.
   * **Traffic Controller**: Monitors and clears roadblocks.

4. **Shared Memory**

   * Agents update and access shared emergency status (resources, traffic, etc.).

5. **Response Complete**

   * Resources are dispatched, routes optimized, medical team alerted.

---

## 🔁 Emergency Response Workflow (Flowchart)

```
┌────────────────────────┐
│   Emergency Triggered  │
└────────────┬───────────┘
             │
             ▼
  ┌───────────────────────┐
  │   Dispatch Agent      │
  │ - Starts Coordination │
  └────────┬──────────────┘
           │
           ▼
 ┌────────────────────────┐
 │   Medical Agent        │
 │ - Assess injuries      │
 └────────┬───────────────┘
          │
          ▼
 ┌────────────────────────┐
 │  Resource Manager      │
 │ - Allocate resources   │
 └────────┬───────────────┘
          │
          ▼
 ┌────────────────────────┐
 │  Route Planner         │
 │ - Plan best route      │
 └────────┬───────────────┘
          │
          ▼
 ┌────────────────────────┐
 │  Traffic Controller    │
 │ - Monitor & reroute    │
 └────────┬───────────────┘
          │
          ▼
 ┌────────────────────────┐
 │ Emergency Resolved ✅  │
 └────────────────────────┘
```

---


