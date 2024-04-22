import json
import os
import argparse
from typical_prompt_gen import typical_response
from renellm_prompt_gen import renellm_response
from other_prompt_gen import other_prompt


def main(args):
    harmful_input = args.harmful_input

    # if args.gen_typical_prompt:
    #     typical_response(harmful_input)

    if args.gen_renellm_prompt:
        renellm_response(harmful_input)
        
    if args.other_prompt:
        other_prompt(harmful_input)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("--gen_typical_prompt", type=str, default=True, help="Generate typical prompt")
    parser.add_argument("--gen_renellm_prompt", type=str, default=True, help="Generate Renellm prompt")
    parser.add_argument("--other_prompt", type=str, default=True, help="Generate other prompt")
    parser.add_argument("--harmful_input", type=str, help="Input harmful sentence")

    args = parser.parse_args()
    main(args)