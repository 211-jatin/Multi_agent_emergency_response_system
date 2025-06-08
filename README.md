# Emergency Response Coordination System

A multi-agent AI system designed to coordinate emergency responses using LangChain and Google's Gemini AI. The system simulates real-world emergency scenarios and demonstrates how multiple specialized agents can work together to manage crisis situations.

## Project Overview

This Emergency Response Coordination System uses five specialized AI agents that collaborate to handle emergency situations efficiently:

- **Dispatch Agent**: Central coordinator for emergency responses
- **Medical Agent**: Handles medical assessments and response coordination
- **Resource Manager**: Manages allocation of emergency resources
- **Route Planner**: Calculates optimal routes for emergency vehicles
- **Traffic Controller**: Monitors traffic conditions and suggests alternatives

## System Architecture

```
Emergency Coordination System
├── Dispatch Agent (Central Coordinator)
├── Medical Agent (Medical Response)
├── Resource Manager (Resource Allocation)
├── Route Planner (Navigation)
└── Traffic Controller (Traffic Management)
```

## Technologies Used

- **Python 3.12**
- **LangChain**: Multi-agent framework
- **Google Gemini AI**: Large Language Model
- **ReAct Pattern**: Reasoning and Acting framework
- **Custom Tools**: Emergency-specific functionality

## Features

### Core Capabilities
- **Multi-Agent Coordination**: Five specialized agents working in harmony
- **Real-time Resource Management**: Track and allocate emergency resources
- **Route Optimization**: Calculate fastest routes considering traffic
- **Priority Assessment**: Medical triage and priority assignment
- **Traffic Management**: Monitor conditions and suggest alternatives
- **Broadcast System**: Inter-agent communication

### Emergency Resources Tracked
- Ambulances (5 available)
- Fire Trucks (3 available)
- Helicopters (2 available)
- Police Units (8 available)

## Installation & Setup

### Prerequisites
```bash
pip install langchain
pip install langchain-google-genai
pip install python-dotenv
```

### Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/yourusername/emergency-response-system
cd emergency-response-system
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure API Key
```python
# Replace with your Google AI API key
GOOGLE_API_KEY = "your-google-ai-api-key-here"
```

4. Run the system
```bash
python emergency_response.py
```

## Sample Execution Output

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

## Agent Details

### Dispatch Agent
- **Role**: Central emergency coordinator
- **Tools**: 
  - `request_resources`: Request emergency resources
  - `get_route_info`: Get route information for vehicles
  - `broadcast_update`: Broadcast updates to teams

### Medical Agent
- **Role**: Medical response coordinator
- **Tools**:
  - `assess_medical_priority`: Assess medical priority levels
  - `coordinate_medical_response`: Coordinate medical teams

### Resource Manager
- **Role**: Emergency resource allocation
- **Tools**:
  - `check_availability`: Check resource availability
  - `allocate_resources`: Allocate resources to incidents

### Route Planner
- **Role**: Navigation and route optimization
- **Tools**:
  - `calculate_route`: Calculate fastest routes
  - `check_traffic`: Check traffic conditions

### Traffic Controller
- **Role**: Traffic management and flow control
- **Tools**:
  - `monitor_traffic`: Monitor traffic and blocks
  - `suggest_alternative`: Suggest alternative routes

## System Capabilities

### Emergency Scenario Handling
The system demonstrates handling of a complex highway accident:
- **Incident**: Multi-vehicle accident on Highway 101
- **Casualties**: 4 injured (2 critical, 2 minor)
- **Resources**: Automatic allocation of ambulances and helicopters
- **Coordination**: Real-time communication between agents

### Resource Management
- Dynamic resource tracking and allocation
- Priority-based resource distribution
- Resource availability monitoring

### Intelligent Routing
- Real-time traffic condition assessment
- Alternative route suggestions
- ETA calculations for emergency vehicles

## Future Enhancements

- **Real-time Data Integration**: Connect with actual traffic and emergency APIs
- **Geographic Information System**: Integrate mapping services
- **Machine Learning Models**: Predictive resource allocation
- **Mobile App Interface**: Field responder mobile application
- **Database Integration**: Historical incident tracking
- **Weather Integration**: Weather-based response modifications

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LangChain** for the multi-agent framework
- **Google AI** for Gemini language model
- **Emergency Response Teams** for inspiration

## Contact

For questions or support, please open an issue on GitHub or contact the development team.

---

**Note**: This is a simulation system for demonstration purposes. For actual emergency situations, please contact your local emergency services (911, 108, etc.).
