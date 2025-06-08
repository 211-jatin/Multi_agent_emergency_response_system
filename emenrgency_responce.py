import os
import logging
import time
from typing import Dict, List
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish
import random

# Basic logging setup
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EmergencyCoordinationSystem:
    def __init__(self):
        # Put your API key here
        GOOGLE_API_KEY = "api_key"
        
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.7,
            convert_system_message_to_human=True
        )
        
        self.agents = {}
        self.message_history = []
        # Track emergency resources
        self.emergency_status = {
            "active_incidents": [],
            "available_resources": {
                "ambulances": 5,
                "fire_trucks": 3,
                "helicopters": 2,
                "police_units": 8
            },
            "traffic_conditions": "normal"
        }
        
        self.setup_agents()
        logger.info("System is ready")
    
    def setup_agents(self):
        # Dispatch agent tools
        dispatch_tools = [
            Tool(name="request_resources", 
                 description="Request emergency resources", 
                 func=self.request_resources),
            Tool(name="get_route_info", 
                 description="Get route info for vehicles", 
                 func=self.get_route_info),
            Tool(name="broadcast_update", 
                 description="Broadcast updates to teams", 
                 func=self.broadcast_update)
        ]
        
        # Standard prompt template
        dispatch_prompt = PromptTemplate(
            input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
            template="""You are Emergency Dispatch Agent. Coordinate emergency responses.
            
            Tools available: {tools}
            Tool names: {tool_names}
            
            Format:
            Thought: What to do?
            Action: [tool name]
            Action Input: [input]
            Observation: [result]
            Thought: Final answer ready
            Final Answer: [response]
            
            Human: {input}
            {agent_scratchpad}"""
        )
        
        # Resource management tools
        resource_tools = [
            Tool(name="check_availability", 
                 description="Check resource availability", 
                 func=self.check_resource_availability),
            Tool(name="allocate_resources", 
                 description="Allocate resources to incidents", 
                 func=self.allocate_resources)
        ]
        
        # Route planning tools  
        route_tools = [
            Tool(name="calculate_route", 
                 description="Calculate fastest route", 
                 func=self.calculate_route),
            Tool(name="check_traffic", 
                 description="Check traffic conditions", 
                 func=self.check_traffic_conditions)
        ]
        
        # Traffic management
        traffic_tools = [
            Tool(name="monitor_traffic", 
                 description="Monitor traffic and blocks", 
                 func=self.monitor_traffic),
            Tool(name="suggest_alternative", 
                 description="Suggest alternative routes", 
                 func=self.suggest_alternative_route)
        ]
        
        # Medical response tools
        medical_tools = [
            Tool(name="assess_medical_priority", 
                 description="Assess medical priority", 
                 func=self.assess_medical_priority),
            Tool(name="coordinate_medical_response", 
                 description="Coordinate medical teams", 
                 func=self.coordinate_medical_response)
        ]
        
        # Creating all the agents here
        self.create_agent("dispatch", dispatch_tools, "Emergency Dispatch Coordinator")
        self.create_agent("resource", resource_tools, "Resource Manager")
        self.create_agent("route", route_tools, "Route Planner")
        self.create_agent("traffic", traffic_tools, "Traffic Controller")
        self.create_agent("medical", medical_tools, "Medical Coordinator")
        
        logger.info("All agents initialized")
    
    def create_agent(self, name: str, tools: List[Tool], role: str):
        prompt = PromptTemplate(
            input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
            template=f"""You are {role} in Emergency Response System.
            
            Available tools: {{tools}}
            Tool names: {{tool_names}}
            
            Format:
            Thought: What should I do?
            Action: [tool name] 
            Action Input: [input]
            Observation: [result]
            Thought: I know the answer
            Final Answer: [response]
            
            Situation: {{input}}
            {{agent_scratchpad}}"""
        )
        
        agent = create_react_agent(llm=self.llm, tools=tools, prompt=prompt)
        
        self.agents[name] = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            memory=ConversationBufferMemory(memory_key="chat_history"),
            max_iterations=3,
            handle_parsing_errors=True
        )
    
    def request_resources(self, request: str) -> str:
        logger.info(f"Resource request: {request}")
        
        # Simple resource allocation logic - checks what type of vehicle is needed
        if "ambulance" in request.lower():
            count = self.extract_number(request)
            available = self.emergency_status["available_resources"]["ambulances"]
            if available >= count:
                self.emergency_status["available_resources"]["ambulances"] -= count
                result = f"{count} ambulances dispatched"
            else:
                result = f"Only {available} ambulances available"
        elif "helicopter" in request.lower():
            if self.emergency_status["available_resources"]["helicopters"] > 0:
                self.emergency_status["available_resources"]["helicopters"] -= 1
                result = "Helicopter dispatched"
            else:
                result = "No helicopters available"
        else:
            result = "Request received, processing"
        
        return result
    
    def get_route_info(self, location: str) -> str:
        # Mock route data - in real system this would call GPS/Maps API
        routes = [
            f"Highway route to {location}: 12 mins",
            f"City route to {location}: 15 mins", 
            f"Bypass route to {location}: 18 mins"
        ]
        return "Routes: " + " | ".join(routes)
    
    def broadcast_update(self, message: str) -> str:
        self.message_history.append(f"BROADCAST: {message}")
        return f"Broadcasted: {message}"
    
    def check_resource_availability(self, resource_type: str) -> str:
        avail = self.emergency_status["available_resources"]
        return f"Available - Ambulances: {avail['ambulances']}, Fire: {avail['fire_trucks']}, Helicopters: {avail['helicopters']}, Police: {avail['police_units']}"
    
    def allocate_resources(self, allocation: str) -> str:
        return f"Allocated: {allocation}"
    
    def calculate_route(self, destination: str) -> str:
        eta = random.randint(8, 20)
        return f"Fastest to {destination}: Highway - ETA {eta} mins"
    
    def check_traffic_conditions(self, route: str) -> str:
        conditions = ["light", "moderate", "heavy"]
        condition = random.choice(conditions)
        return f"Traffic on {route}: {condition}"
    
    def monitor_traffic(self, area: str) -> str:
        return f"Monitoring {area} - Status: {self.emergency_status['traffic_conditions']}"
    
    def suggest_alternative_route(self, blocked_route: str) -> str:
        alternatives = ["Industrial route", "Riverside highway", "Downtown bypass"]
        alt = random.choice(alternatives)
        return f"Try {alt} instead (+5-7 mins)"
    
    def assess_medical_priority(self, situation: str) -> str:
        priorities = ["Critical", "High priority", "Medium", "Low"]
        priority = random.choice(priorities[:2])
        return f"Priority: {priority} - Immediate dispatch needed"
    
    def coordinate_medical_response(self, response_type: str) -> str:
        return f"Medical teams coordinated: {response_type}"
    
    def extract_number(self, text: str) -> int:
        import re
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else 1
    
    def simulate_emergency_scenario(self):
        print("=" * 50)
        print("Emergency Response Simulation")
        print("=" * 50)
        
        # Creating an accident scenario
        emergency_details = """
        Accident on Highway 101 - Mile 45
        4 people injured (2 critical, 2 minor)
        3 cars + 1 truck involved
        Traffic jam created, need alternate routes
        """
        
        print(emergency_details)
        
        # Step by step response - each agent handles their part
        print("\nStep 1: Dispatch")
        dispatch_resp = self.agents["dispatch"].invoke({
            "input": f"Emergency: {emergency_details} - coordinate response"
        })
        print(f"Dispatch: {dispatch_resp['output']}")
        
        time.sleep(1)
        
        print("\nStep 2: Medical Assessment") 
        medical_resp = self.agents["medical"].invoke({
            "input": "4 injured in highway accident: 2 critical, 2 minor"
        })
        print(f"Medical: {medical_resp['output']}")
        
        time.sleep(1)
        
        print("\nStep 3: Resources")
        resource_resp = self.agents["resource"].invoke({
            "input": "Need ambulances, helicopters for highway accident"
        })
        print(f"Resources: {resource_resp['output']}")
        
        time.sleep(1)
        
        print("\nStep 4: Route Planning")
        route_resp = self.agents["route"].invoke({
            "input": "Routes to Highway 101 Mile 45 for emergency vehicles"
        })
        print(f"Routes: {route_resp['output']}")
        
        time.sleep(1)
        
        print("\nStep 5: Traffic Control")
        traffic_resp = self.agents["traffic"].invoke({
            "input": "Highway 101 blocked at Mile 45, need alternatives"
        })
        print(f"Traffic: {traffic_resp['output']}")
        
        print("\n" + "="*50)
        print("Response Complete!")
        print("="*50)
        print(f"Resources left: {self.emergency_status['available_resources']}")

def main():
    try:
        system = EmergencyCoordinationSystem()
        
        print("Emergency Response System Online")
        print("Agents: Dispatch, Resource, Route, Traffic, Medical")
        print("-" * 40)
        
        system.simulate_emergency_scenario()
        
        print("\nDemo complete!")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Check your API key!")

# Run the system
if __name__ == "__main__":
    main()
