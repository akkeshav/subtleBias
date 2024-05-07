import argparse
import utils
import variable_util
import tqdm
import time


def save_raw_data(task_name, model):
    category = variable_util.categories
    themes = variable_util.all_themes

    theme_list = {cat: [] for cat in category}
    prompts = {cat: [] for cat in category}
    answer_responses = {cat: [] for cat in category}

    for cat in tqdm(category):
        for theme in tqdm(themes):
            time.sleep(3)
            prompt, answer = utils.get_answer_bias(f'{variable_util.task_dict[task_name]}{theme}.', cat, 0.2, model)

            prompts[cat].append(prompt)
            answer_responses[cat].append(answer)
            theme_list[cat].append(theme)

    try:
        utils.save_raw_data(answer_responses, task_name, theme_list, prompts, model)
    except Exception as e:
        print("An error during occurred during file saving occurred:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subtle bias")
    parser.add_argument('--model', type=str, required=True, choices=['gpt4', 'llama', 'mixtral'], help='choose model')
    parser.add_argument('--task', type=str, required=True, choices=['gpt4', 'llama', 'mixtral'], help='choose task')

    model = parser.parse_args().model
    task = parser.parse_args().task

    save_raw_data(task, model)
    utils.save_analysis_semantic(task, model)
