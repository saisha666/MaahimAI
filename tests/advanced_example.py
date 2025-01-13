from maahimai import MaahimAI
    
def advanced(): 
    maahimai = MaahimAI(
        agent_file="agents.yaml",
        framework="autogen",
        topic="create a movie script about dog in moon"
    )
    maahimai.run()

if __name__ == "__main__":
    advanced()