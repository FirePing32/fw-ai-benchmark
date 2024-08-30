import os

user, input_tok, output_tok = 10, 1000, 500
deployment_id = ""
api_key = ""
proxy = ""

os.system(
    f"locust -t 2min -u {user} -r {user} -o {output_tok} -H {proxy} -p {input_tok} --model=llama3 --prompt-randomize --chat --provider openai -k {api_key} --header 'id:{deployment_id}'"
)