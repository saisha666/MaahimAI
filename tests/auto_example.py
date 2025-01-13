from maahimai import MaahimAI
    
def auto(): 
    maahimai = MaahimAI(
        agent_file="agents.yaml",
        auto=True,
        topic="create a movie script about dog in moon"
    )
    maahimai.run()

if __name__ == "__main__":
    auto()