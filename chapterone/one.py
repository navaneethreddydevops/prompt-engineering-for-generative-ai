from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    trust_remote_code=True,
    device_map="cpu",
    torch_dtype="auto",
    attn_implementation="eager",
)

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_length=2048,
    temperature=0.3,
    do_sample=False,
)

messages = [
    {"role": "user", "content": "Create a funny joke about chickens"},
]

response = generator(messages)
print(response[0]["generated_text"])
