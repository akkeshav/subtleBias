import argparse
import utils
import variable_util

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subtle bias")
    parser.add_argument('--evaluatee_model', type=str, required=True, choices=['gpt4', 'llama', 'mixtral'],
                        help='choose evaluatee model')
    parser.add_argument('--task', type=str, required=True, choices=variable_util.tasks, help='choose task')
    parser.add_argument('--evaluator_model', type=str, required=True, choices=['gpt4', 'llama', 'mixtral'],
                        help='choose evaluator model')

    evaluatee_model = parser.parse_args().evaluatee_model
    evaluator_model = parser.parse_args().evaluator_model
    task = parser.parse_args().task

    utils.get_evaluation(task, evaluatee_model, evaluator_model)
    utils.get_evaluation_analysis(task, evaluatee_model, evaluator_model)
    utils.get_percentage_per_identity(task, evaluatee_model, evaluator_model)
