import json
import matplotlib.pyplot as plt
import os

folder = "../data/responses/"
subfolder = ["logicbench/irr/","logicbench/exp-3/", "logicqa/", "logicqa2/"]
perplexity_file = "result.json"
accuracy_file = "accuracy_results.json"

def load_data(perplexity_path, accuracy_path):
    # Load perplexity data
    with open(perplexity_path, 'r') as f:
        perplexity_data = json.load(f)
    
    # Load accuracy data
    with open(accuracy_path, 'r') as f:
        accuracy_data = json.load(f)
    
    return perplexity_data, accuracy_data

def plot_accuracy_vs_perplexity(perplexity_data, accuracy_data, experiment_name):
    models = []
    perplexities = []
    accuracies = []
    os.makedirs("../plots", exist_ok=True)  # Create directory for plots if it doesn't exist
    # Extract data for plotting
    for model, perplexity_info in perplexity_data.items():
        if model in accuracy_data:  # Ensure the model exists in both files
            models.append(model)
            perplexities.append(perplexity_info["perplexity"])
            accuracies.append(accuracy_data[model]["accuracy"])
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(perplexities, accuracies, color='blue', label='Models')
    
    # Annotate points with model names
    for i, model in enumerate(models):
        plt.annotate(model, (perplexities[i], accuracies[i]), textcoords="offset points", xytext=(5, 5), ha='center')
    
    plt.title("Accuracy vs Perplexity")
    plt.xlabel("Perplexity")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"../plots/accuracy_vs_perplexity_{experiment_name}.png")  # Save the plot with the first model name
    plt.show()

def main():
    for sub in subfolder:
        perplexity = f"{folder}{sub}{perplexity_file}"
        accuracy = f"{folder}{sub}{accuracy_file}"
        print(f"Loading data from {perplexity} and {accuracy}")
        
        # Load data
        perplexity_data, accuracy_data = load_data(perplexity, accuracy)
        
        # Plot data
        # print(f"Plotting data for {sub.split('/')}")
        exp_name = sub.split("/")[0] if len(sub.split("/")) == 2  else sub.split("/")[1]
        plot_accuracy_vs_perplexity(perplexity_data, accuracy_data, exp_name)  # Use the first part of the subfolder name as the experiment name

if __name__ == "__main__":
    main()