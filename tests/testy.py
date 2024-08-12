import gymnasium as gym

def main():
    env = gym.make('CartPole-v1', render_mode="human")
    
    num_episodes = 5
    
    for episode in range(num_episodes):
        observation = env.reset()
        done = False
        
        while not done:
            env.render()
            action = env.action_space.sample()
            
            # Use the updated return values
            observation, reward, terminated, truncated, info = env.step(action)
            
            # Update done based on termination or truncation
            done = terminated or truncated
            
        print(f"Episode {episode + 1} finished")

    env.close()

if __name__ == "__main__":
    main()
