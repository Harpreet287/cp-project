import json
folder = '../data/responses/logicbench/irr/'

def compute_accuracy(ground_truth_path, predictions_path, results):
    # Load ground truth answers
    with open(ground_truth_path, 'r') as f:
        ground_truth_data = json.load(f)
    
    ground_truth_answers = []
    for item in ground_truth_data["data_samples"]:
        for qa in item['qa_pairs']:
            ground_truth_answers.append(qa['answer'].strip().lower())
    ground_truth_answers = ground_truth_answers[:20]

    # Load predicted answers
    with open(f"{folder}/{predictions_path}", 'r') as f:
        predicted_data = json.load(f)

    predicted_answers = []
    for item in predicted_data:
        for qa in item['qa_pairs']:
            predicted_answers.append(qa['answer'].strip().lower())

    # Check length
    if len(ground_truth_answers) != len(predicted_answers):
        raise ValueError(f"Length mismatch: {len(ground_truth_answers)} ground truth vs {len(predicted_answers)} predictions")

    # Compute accuracy
    correct = sum(gt == pred for gt, pred in zip(ground_truth_answers, predicted_answers))
    total = len(ground_truth_answers)
    accuracy = correct / total * 100

    # Store result in dictionary
    results[predictions_path] = {
        "accuracy": round(accuracy, 2),
        "correct": correct,
        "total": total
    }

# Example usage
output_file = 'irr_accuracy_results.json'
results = {}

compute_accuracy('../data/irr.json', 'gpt4o.json', results)
compute_accuracy('../data/irr.json', 'mistral.json', results)
compute_accuracy('../data/irr.json', 'claude.json', results)

# Write results to JSON file
with open(output_file, 'w') as out_file:
    json.dump(results, out_file, indent=4)
