# Emergency Response Coordination System

A student project demonstrating multi-agent AI coordination using LangChain and Google's Gemini AI. This system simulates emergency response scenarios to showcase how AI agents can work together to solve complex real-world problems.

## About This Project

This is a personal learning project that I built to explore multi-agent AI systems and their applications in emergency management. The system uses five different AI agents that collaborate to handle emergency situations, demonstrating concepts like agent coordination, resource management, and decision-making.

## What It Does

The system simulates an emergency response scenario where multiple AI agents work together:

- **Dispatch Agent**: Acts as the main coordinator
- **Medical Agent**: Handles medical priorities and response
- **Resource Manager**: Manages available emergency resources
- **Route Planner**: Finds best routes for emergency vehicles
- **Traffic Controller**: Manages traffic flow and alternatives

## Technologies I Used

- **Python 3.12**: Main programming language
- **LangChain**: Framework for building AI agent systems
- **Google Gemini AI**: The AI model powering the agents
- **ReAct Pattern**: A reasoning framework for AI agents

## How to Run

### What You Need
```bash
pip install langchain
pip install langchain-google-genai
```

### Setup
1. Download the code file
2. Get a free Google AI API key from Google AI Studio
3. Replace the API key in the code:
```python
GOOGLE_API_KEY = "your-api-key-here"
```
4. Run it:
```bash
python emergency_response.py
```

## Sample Output

Here's what happens when I run the system with a highway accident scenario:

```
Emergency Response System Online
Agents: Dispatch, Resource, Route, Traffic, Medical
----------------------------------------
==================================================
Emergency Response Simulation
==================================================

        Highway 101 pe accident - Mile 45
        4 log injured (2 critical, 2 minor)
        3 cars + 1 truck involved
        Traffic jam ho gaya, alternate routes chahiye
        

Step 1: Dispatch
> Entering new AgentExecutor chain...
Thought: I need to request resources, get route information for alternate routes, 
and broadcast updates to the responding teams.

Action: request_resources
Action Input: "Multiple vehicle accident on Highway 101, mile marker 45. 
4 injured (2 critical, 2 minor). Requesting multiple ambulances..."

Observation: Only 5 ambulances available
Dispatch: Agent stopped due to iteration limit or time limit.

Step 2: Medical Assessment
> Entering new AgentExecutor chain...
Action: assess_medical_priority
Action Input: 4 injured in highway accident: 2 critical, 2 minor
Observation: Priority: High priority - Immediate dispatch needed

Medical: High priority medical response dispatched. Two critical and 
two minor injuries reported at the highway accident.

Step 3: Resources
> Entering new AgentExecutor chain...
Action: check_availability
Observation: Available - Ambulances: 5, Fire: 3, Helicopters: 2, Police: 8

Action: allocate_resources
Action Input: {"allocation": "highway accident: ambulances=2, helicopters=1"}
Resources: Agent stopped due to iteration limit or time limit.

Step 4: Route Planning
> Entering new AgentExecutor chain...
Action: calculate_route
Action Input: Highway 101 Mile 45
Observation: Fastest to Highway 101 Mile 45: Highway - ETA 11 mins

Action: check_traffic
Observation: Traffic on Highway - ETA 11 mins: heavy
Routes: Agent stopped due to iteration limit or time limit.

Step 5: Traffic Control
> Entering new AgentExecutor chain...
Action: monitor_traffic
Action Input: area: Highway 101 Mile 45
Observation: Monitoring area: Highway 101 Mile 45 - Status: normal

Traffic: I require further confirmation of the blockage on Highway 101 
at Mile 45 before I can suggest alternative routes.

==================================================
Response Complete!
==================================================
Resources left: {'ambulances': 5, 'fire_trucks': 3, 'helicopters': 2, 'police_units': 8}

Demo complete!
```

## What I Learned

Building this project taught me:

- **Multi-Agent Systems**: How different AI agents can work together
- **LangChain Framework**: Using tools and agent executors
- **API Integration**: Working with Google's Gemini AI
- **System Design**: Breaking complex problems into smaller parts
- **Error Handling**: Managing API limits and agent iterations
- **Real-world Applications**: How AI can solve practical problems

## Key Features I Implemented

### Agent Coordination
- Five specialized agents with different roles
- Inter-agent communication through broadcasts
- Coordinated response to emergency scenarios

### Resource Management
- Real-time tracking of emergency resources
- Automatic allocation based on priorities
- Resource availability monitoring

### Decision Making
- Priority-based medical assessments
- Route optimization considering traffic
- Alternative route suggestions

## Technical Challenges I Solved

1. **Agent Communication**: Getting agents to work together effectively
2. **Resource Tracking**: Managing state across multiple agents
3. **Error Handling**: Dealing with API limitations and parsing errors
4. **Realistic Simulation**: Creating believable emergency scenarios

## Future Improvements I'm Considering

- Add real-time data integration (traffic APIs, weather)
- Create a web interface for better visualization
- Implement more sophisticated resource allocation algorithms
- Add database storage for incident history
- Include more emergency scenarios (fire, natural disasters)

## Why I Built This

This project demonstrates my ability to:
- Work with modern AI frameworks and APIs
- Design systems that solve real-world problems
- Handle complex multi-component architectures
- Think about practical applications of AI technology
- Write clean, documented code

## Code Structure

The main file contains:
- `EmergencyCoordinationSystem` class that manages everything
- Individual agent setup with specialized tools
- Simulation methods for testing scenarios
- Resource management and tracking
- Logging and error handling

## Running Your Own Scenarios

You can modify the `simulate_emergency_scenario()` method to test different emergency situations. The system is designed to be flexible and handle various types of incidents.

---

**Note**: This is a simulation for learning purposes. Real emergency situations should always be reported to local emergency services.

**Contact**: Feel free to reach out if you have questions about the implementation or want to discuss the project!
