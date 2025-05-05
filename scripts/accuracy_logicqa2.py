import json
import os

folder = '../data/responses/logicqa2/'

def load_ground_truth(logicqa_path):
    ground_truth_answers = []
    with open(logicqa_path, 'r') as f:
        for line in f:
            try:
                obj = json.loads(line.strip())
                answer = obj.get('label', '')
                if isinstance(answer, (int, float)):
                    answer = str(answer)
                elif not isinstance(answer, str):
                    continue
                answer = answer.strip().lower()
                if answer:
                    ground_truth_answers.append(answer)
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON line: {line.strip()} - Error: {e}")
    return ground_truth_answers

def load_predictions(predictions_path):
    predicted_answers = []
    with open(predictions_path, 'r') as f:
        predicted_data = json.load(f)
        for item in predicted_data:
            answer = item.get('label', '')
            if isinstance(answer, list):  # If the answer is a list, pick the first element
                answer = answer[0] if answer else ''
            if isinstance(answer, (int, float)):  # Convert numeric answers to strings
                answer = str(answer)
            elif not isinstance(answer, str):  # Skip non-string and non-numeric answers
                continue
            predicted_answers.append(answer.strip().lower())
    return predicted_answers

def compute_accuracy(rt, predictions_filename, result):

    pred = load_predictions(f"{folder}{predictions_filename}")
    gt = rt[:len(pred)]  # Ensure gt is the same length as pred
    print(f"Loaded {len(pred)} predictions from {predictions_filename}")
    if len(gt) != len(pred):
        raise ValueError(f"Length mismatch: {len(gt)} ground truth vs {len(pred)} predictions")

    correct = sum(1 for g, p in zip(gt, pred) if g == p)
    total = len(gt)
    accuracy = correct / total * 100

    # result = f"Accuracy: {accuracy:.2f}% ({correct}/{total} correct)\n"
    
    result[predictions_filename] = {
        "accuracy": round(accuracy, 2),
        "correct": correct,
        "total": total
    }

# Example usage
gt = load_ground_truth('../data/LogicQA2.jsonl')
# gt = gt[:20]
result = {}
compute_accuracy(gt, 'claude.json', result)
compute_accuracy(gt, 'gpt4o.json', result)
compute_accuracy(gt, 'mistral.json', result)

output_file = 'logicqa2_accuracy_results.json'

# Write results to JSON file
with open(output_file, 'w') as out_file:
    json.dump(result, out_file, indent=4)