from agent import Agent
from toolbox import ToolBox
from input_process import OllamaModel
from tools import reverse_string, basic_calculator  

if __name__ == "__main__":

    tools = [basic_calculator, reverse_string]

    # Uncoment below to run with OpenAI
    # model_service = OpenAIModel
    # model_name = 'gpt-3.5-turbo'
    # stop = None

    # Uncomment below to run with Ollama
    model_service = OllamaModel
    model_name = "llama3.1"
    stop = "<|eot_id|>"

    agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

    while True:
        prompt = input("Ask me anything: ")
        if prompt.lower() == "exit":
            break

        agent.work(prompt)